# Raspbery pi webcam

## 1. Development

Install packages:

```sh
pip install -r requirements.txt
```

Build binary:

```sh
pyinstaller --onefile --distpath . telegramBot.py
```

Execute binary:

```sh
./telegramBot
```

## 2. Useful links

- [Pyinstall usage](https://pyinstaller.org/en/stable/usage.html)
- [Telegram send photo API](https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.sendPhoto)
- [MJPG-Streamer setup](https://www.sigmdel.ca/michel/ha/rpi/streaming_en.html)
- [Raspberr pi useing usb webcams tutorial](https://raspberrypi-guide.github.io/electronics/using-usb-webcams)
