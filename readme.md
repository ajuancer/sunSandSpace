# SunSandSpace
<img src="docs/resources/img/logo_v1.png" alt="Project logo" align="left" width="80"> **SunSandSpace** is a [Telegram](https://www.telegram.org) bot that checks the Gijón beaches occupation, making easier to choose the perfect place for maintaining social distancing, one measure suggested<sup>[1]</sup> to reduce the spread of COVID-19<sup>[2]</sup>. You can see him in action [here](https://ajuancer.github.io/sunSandSpace/resources/video/test_v0_0.mp4)

The project contains these files:

- [`main.py`](main.py): File containing almost all the program.
- [`img`](img): Dir with the needed images. They are beaches maps obtained from [OpenStreetMap](https://www.openstreetmap.org).
- [`info.json`](info.json): JSON file containing the limit coords for each image in the `/img` dir. This is a _temp patch_ to cover some missing info of the official API. 

## I want to use it!

Till the moment, you can't talk to SunSandSpace. A version for the general public hopefully will be available soon. If you're a programmer, you can run it on your personal server (or PC). If you need help, don't doubt [contacting me](https://ajuancer.github.io).

A preview of the bot is available at the [official page](https://ajuancer.github.io/sunSandSpace).

## Contribute.

You can fork this project. Feel free to [contact me](https://ajuancer.github.io) if you have need help. 

### 1. The dependences are:

- [python-telegram-bot](https://python-telegram-bot.org/), wrapper to communicate with the [Telegram API](https://core.telegram.org/api).
- The [requests](https://pypi.org/project/requests/) module, to stablish the communication with the [beach occupation API](https://www.gijon.es/es/datos/ocupacion_playas).
- [Matplotlib](https://matplotlib.org/), to graph the information on the maps.

### 2. The API:

This bot uses the official API maintained by the Gijón Local Council. You can check the structure of the data  [here](https://www.gijon.es/es/datos/ocupacion_playas), and get the info  [here](https://playasapi.ctic.es/v1/zones).

### 3. Installation.

1. Create a new bot through Telegram [@botfather](https://t.me/botfather) and get the **access token**. You can see a tutorial [here](https://core.telegram.org/bots#6-botfather). _**Remember to keep it private**_
2. Clone this repository. Make sure `main.py` is located in the same dir where `img` is located. Or change it on the `main.py` file.
3. Download the dependences. You can use `install -r requirements.txt` to install the libraries listed above.
4. Replace the var `tm_token` with the access token you obtained in step #1.
5. Run the code.

## License.

This project is under the [GNU Affero Public License v3.0 -or later-.](https://www.gnu.org/licenses/agpl-3.0.en.html)

![Affero GNU license icon](https://www.gnu.org/graphics/agplv3-155x51.png)

## More info.

You can [mail me](https://ajuancer.github.io) if you want to know more information, want to contribute or any other thing.

------

[1]: [Social Distancing: Keep a Safe Distance to Slow the Spread.](https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/social-distancing.html), Centers for Disease Control and Prevention, 2020.

[2]: [Coronavirus disease (COVID-19) pandemic](https://www.who.int/emergencies/diseases/novel-coronavirus-2019), WHO, 2020

