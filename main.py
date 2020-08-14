#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python script about beach occupation status (in real time).

Get information about beach occupation from the specific API available for the general public,
process the information creating a specific map, and send the result via telegram to the user
that has requested it.

__author__ = "Juan Cerdeño"
__copyright__ = "Copyright 2020, Juan Cerdeño"
__license__ = "Affero GPL 3.0"
__version__ = "0.1"
__url__ = https://www.github.com/ajuancer/sunSandSpace
__status__ = "Development"
"""

import io
import json
from datetime import datetime

import requests
from matplotlib import pyplot as plt
from telegram import (KeyboardButton,
                      ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, CallbackQueryHandler)

API_URL = 'https://playasapi.ctic.es/v1/zones'


class Beach(object):
    """
    Beach object containing all information about a given beach.
    """

    def __init__(self, data, sectors):
        """
        The constructor for Beach class.
        :param data: JSON-formatted data from the CTIC API (except sectors info).
        :param sectors: Array of Sectors objects containing specific sectors info.
        """
        self.__dict__ = data
        self.sectors = sectors


class Sector(object):
    """
    Sector object containing all info. available for a specific sector of a given beach.
    """

    def __init__(self, data):
        """
        The constructor for Sector class.
        :param data: All the JSON-formatted data available for that sector.
        """
        self.__dict__ = data


def get_data(path):
    """
    Function responsible for data standardization.
    Performs:
     - server connection.
     - sectors cords dict.
     - object creation.
    :param path: The path (or URL) of the server.
    :return: An array of Beach objects containing all the available information.
             If no sectors info. is detected, None is returned.
    """
    json_response = requests.get(path).text
    json_data = json.loads(json_response)
    json_beaches = []
    for item in json_data:
        json_sectors = []
        for sector_info in item['sectors']:
            json_sectors.append(Sector(sector_info))
        if item.pop('sectors', None):
            json_beaches.append(Beach(item, json_sectors))
        else:
            return None
    return json_beaches


# /!\ Should get sector coords (polygon or point), temp solution with extra file.
# Constant coords instead of given ones (Beach.point) due to plot method system.
def plot_info(img_path, beach_info):
    """
    Plots occupation info. of a specific beach on a map.
    :param img_path: The path (or URL) of the map located file.
    :param beach_info: The Beach-formatted info. of the specific beach.
    :return: The generated image on memory buffer
    """
    # Basic color palette (from green (0) to red (-1)).
    colours = ['#25f047af', '#9df025af', '#def025af', '#f0d125af', '#f09a25af', '#f06325af', '#f03725af']
    # tmp
    lims = None
    sectors_coords = None
    with open('info.json', 'r') as f:
        data = json.load(f)
        for beach_json in data['beach']:
            if int(beach_json['id']) == beach_info.id:
                lims = [float(i) for i in beach_json['coords']]
                sectors_coords = beach_json['sectors']
    # tmp
    fig, ax = plt.subplots(figsize=(8, 4))
    bk_img = plt.imread(img_path)
    ax.set_xlim(lims[0], lims[1])
    ax.set_ylim(lims[3], lims[2])
    for sector in beach_info.sectors:
        # tmp
        sector_point = None
        for item in sectors_coords:
            if str(item['id']) == str(sector.id):
                sector_point = [float(coord) for coord in item['coords'].split(", ")]
        # tmp
        if sector_point:
            colour_i = int(
                (sector.estimatedOccupation / 100) * len(colours) - 1 if sector.estimatedOccupation != 0 else 0)
            ax.plot(sector_point[1], sector_point[0], 'o', color=colours[colour_i], markersize=32)
            plt.annotate(str(sector.estimatedOccupation) + '%',
                         (sector_point[1] - .00002, sector_point[0] - .0001), color='#f9f9f9')
    ax.axis('off')
    plt.figtext(0.001, .06, datetime.now().strftime(f' {beach_info.name} occupation status at %m/%d/%Y, %H:%M'),
                fontsize=7, ha='left',
                weight='light', backgroundcolor='#fff')
    plt.figtext(0.001, 0.02, ' By @SunSandSpace_bot (t.me/sunSandSpace_bot).', fontsize=7,
                weight='light', backgroundcolor='#fff')
    plt.figtext(0.999, 0.065, 'Data: CC BY 4.0, Gijón Local Council. ', fontsize=7,
                ha='right', weight='light', backgroundcolor='#fff')
    plt.figtext(0.999, 0.02, 'Map: ODbL v1.0, OpenStreetMap Foundation. ',
                fontsize=7, ha='right', weight='light', backgroundcolor='#fff')
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    ax.imshow(bk_img, extent=lims, aspect='auto', origin='lower')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300)
    buf.seek(0)
    return buf


def get_beach_info(beach_id, beaches_info):
    """
    Searches for all the available info. of the specified beach.
    :param beach_id: The ID of the beach to look for.
    :param beaches_info: An array of Beach objects that contains all info.
    :return: the image generated and the beach available info. None if no beach is returned.
    """
    beach_occupation_plotted = None
    requested_beach = None
    for beach_info in beaches_info:
        if beach_info.id == beach_id:
            requested_beach = beach_info
            beach_occupation_plotted = plot_info(get_beach_map(beach_id), beach_info)
    return beach_occupation_plotted, requested_beach


def get_beach_map(beach_id):
    """
    Performs the search of the beach map.
    :param beach_id: The ID of the beach.
    :return: The path to the map location. If the beach is not identified, None.
    """
    if beach_id == 1:
        return 'img/san_lorenzo_2300.png'
    elif beach_id == 2:
        return 'img/poniente_2300.png'
    elif beach_id == 3:
        return 'img/arbeyal_2300.png'
    else:
        return None


def bot_start(update, context):
    """
    Define /start function. Used when stating conversation.
    :param update: Telegram needed param.
    :param context: Telegram needed param.
    """
    update.message.reply_text('¡Hola!')
    update.message.reply_text('Dime una playa🏖️, y miro a ver cuanta gente hay.',
                              reply_markup=beach_markup)


def bot_help(update, context):
    """
    Define /help command. Basic explication about bot usage
    :param update: Telegram
    :param context: Telegram
    """
    update.message.reply_text('Elije una de las playas que te muestro debajo. Pulsa sobre la que prefieras, '
                              'y te diré cuanta gente hay ahora mismo.')
    update.message.reply_text('O si quieres información general, escribe /general')
    update.message.reply_text('Si tienes problemas, puedes entrar a https://playas.ctic.es/ '
                              'y ver la ocupación de arenales tu mismo', reply_markup=beach_markup)


def bot_more_info(update, context):
    """
    Define /info command. More info about the project is given.
    :param update:
    :param context:
    :return:
    """
    update.message.reply_text('*Sobre el proyecto*: Son un bot al que le encanta la playa. Puedo saber cuanta gente '
                              'hay de 11:00 a 19:00 de la tarde. Si me preguntas, te contestaré.',
                              parse_mode='markdown')
    update.message.reply_text('*Sobre la epidemia*: Puedes obtener más información en fuentes oficiales, por ejemplo:'
                              '\n- [Web del Gobierno de Asturias sobre COVID19](coronavirus.asturias.es)'
                              '\n- [Twitter de AsturSalud](www.twitter.com/astursalud),'
                              '\no seguir a mi amigo [@asturianBot](www.twitter.com/asturianBot) en twitter.',
                              parse_mode='markdown', disable_web_page_preview=True)
    update.message.reply_text('*Sobre mi*: Si tienes curiosidad por saber más sobre mi, echa un ojo [aquí]('
                              'ajuancer.github.io/sunSandSpace)', parse_mode='markdown')


def bot_beach_markup_handler(update, context):
    """
    Define beach markup handler.
    :param update: Telegram
    :param context: Telegram
    :return:
    """
    query = update.callback_query
    query.answer()
    beach_info = get_beach_info(int(query.data), get_data(API_URL))
    update.callback_query.edit_message_text(
        f'Por lo que veo, la {beach_info[1].name} está ocupada un {str(round(beach_info[1].averageEstimatedOccupation))}%')
    query.message.reply_photo(beach_info[0], caption='Para ser más concretos, la cosa se ve asi.')


def bot_situacion(update, context):
    """
    Define /situacion command. Request beach keyboard.
    :param update: Telegram
    :param context: Telegram
    """
    update.message.reply_text('Pulsa sobre la playa que quieras', reply_markup=beach_keyboard_markup)


def bot_typed_input(update, context):
    """
    Define any text other than command handler.
    :param update: Telegram
    :param context: Telegram
    """
    text = update.message.text.lower()
    context.user_data['choice'] = text
    beaches_info = get_data(API_URL)
    for beach_info in beaches_info:
        if text in beach_info.name.lower() and len(text) > 7:
            beach_info = get_beach_info(int(beach_info.id), beaches_info)
            update.message.reply_text(f'Por lo que veo, la {beach_info[1].name} está ocupada un '
                                      f'{str(round(beach_info[1].averageEstimatedOccupation))}%')
            update.message.reply_photo(beach_info[0], caption='Para ser más concretos, la cosa se ve asi.')
            return
    update.message.reply_text('Lo siento, no se que playa dices')
    bot_general(update, context)


def bot_general(update, context):
    """
    Define /general command. Gives general ingo about all beaches. bot_typed_input ends here.
    :param update: Telegram
    :param context: Telegram
    """
    beaches_info = get_data(API_URL)
    status_str = 'Ha vista general, te puedo decir que '
    for beach_info in beaches_info[:-1]:
        status_str += [
            f' la {beach_info.name} está ocupada en un {str(round(beach_info.averageEstimatedOccupation))}%, ' if not round(
                beach_info.averageEstimatedOccupation) == 0 else f'la {beach_info.name} está vacia, '][0]
    status_str = f'{status_str}y la ' + [
        f'{beaches_info[-1].name} está ocupada en un {str(round(beaches_info[-1].averageEstimatedOccupation))}%' if not round(
            beaches_info[-1].averageEstimatedOccupation) == 0 else f'la {beaches_info[-1].name} está vacia'][0]
    update.message.reply_text(status_str)
    update.message.reply_text('Para más info, selecciona una de las playas', reply_markup=beach_keyboard_markup)


def bot_license(update, context):
    """
    Define /license command. Specifies all legal-related info.
    :param update: Telegram.
    :param context: Telegram.
    """
    update.message.reply_text('Para informarte, utilizo la información del [Ayuntamiento de Gijón](www.gijon.es), '
                              'bajo licencia [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Los mapas '
                              'sobre los que dibujo son de la [OpenStreetMap Foundation](https://osmfoundation.org/), '
                              'y se encuentran licenciados bajo [ODbL v1.0]('
                              'https://opendatacommons.org/licenses/odbl/).', parse_mode='markdown',
                              disable_web_page_preview=True)
    update.message.reply_text('Todo lo que te haya escrito está bajo licencia [CC BY-NC 4.0]('
                              'https://creativecommons.org/licenses/by-nc/4.0/)', parse_mode='markdown',
                              disable_web_page_preview=True)


if __name__ == "__main__":
    tm_token = 'BOT_TOKEN'
    updater = Updater(tm_token, use_context=True)
    dp = updater.dispatcher

    beach_menu = []
    beach_keyboard = []
    for beach in get_data(API_URL):
        beach_menu.append([InlineKeyboardButton(beach.name, callback_data=beach.id)])
        beach_keyboard.append([KeyboardButton(beach.name)])
    beach_keyboard_markup = ReplyKeyboardMarkup(beach_keyboard, one_time_keyboard=True)
    beach_markup = InlineKeyboardMarkup(beach_menu)

    dp.add_handler(CallbackQueryHandler(bot_beach_markup_handler))
    dp.add_handler(CommandHandler('start', bot_start))
    dp.add_handler(CommandHandler('help', bot_help))
    dp.add_handler(CommandHandler('info', bot_more_info))
    dp.add_handler(CommandHandler('situacion', bot_situacion))
    dp.add_handler(CommandHandler('general', bot_general))
    dp.add_handler(CommandHandler('license', bot_license))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), bot_typed_input))

    updater.start_polling()
    updater.idle()
