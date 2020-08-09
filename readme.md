# SunSandSpace

![SunSandSpace icon](https://raw.githubusercontent.com/ajuancer/sunSandSpace/master/docs/resources/img/logo_v1.png | width=80)**SunSandSpace** is a [Telegram](https://www.telegram.org) bot that checks the Gijón beaches occupation, making easier to choose the perfect place for maintaining social distancing, one measure suggested<sup>[1][fn1]</sup> to reduce the spread of COVID-19<sup>[2][fn2]</sup>.

The project contains these files:

- [`main.py`](https://github.com/ajuancer/master/main.py): File containing almost all the program.
- [`img`](https://github.com/ajuancer/master/img): Dir with the needed images. They are beaches maps obtained from [OpenStreetMap](https://www.openstreetmap.org).
- [`info.json`](https://github.com/ajuancer/master/info.json): JSON file containing the limit coords for each image in the `/img` dir. This is a _temp patch_ to cover some missing info of the official API. 

## I want to use it!

Till the moment, you can't talk to SunSandSpace. A version for the general public hopefully will be available soon. If you're a programmer, you can run it on your personal server (or PC). If you need help, don't doubt [contacting me](https://ajuancer.github.io).

A preview of the bot is available at the [official page](https://ajuancer.github.io/sunSandSpace).

## Contribute.

You can fork this project. Feel free to [contact me](https://ajuancer.github.io). 

### The dependences are:

- Telegram module.
- The requests module.
- Matplotlib.

### The API:

This bot uses the official API maintained by the Gijón Local Council, available [here](https://www.gijon.es/es/datos/ocupacion_playas).

## License.

This project is under the [GNU Affero Public License v3.0 -or later-.](https://www.gnu.org/licenses/agpl-3.0.en.html)

![Affero GNU license icon](https://www.gnu.org/graphics/agplv3-155x51.png)

## More info.

You can [mail me](https://ajuancer.github.io) if you want to know more information, want to contribute or any other thing.

------

[fn1]: [Centers for Disease Control and Prevention](https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/social-distancing.html), Centers for Disease Control and Prevention, 2020.

[fn2]: [Coronavirus disease (COVID-19) pandemic](https://www.who.int/emergencies/diseases/novel-coronavirus-2019), WHO, 2020

