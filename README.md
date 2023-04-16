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

Create a service:

```text
[Unit]
Description=Telegram snapshot bot
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=vista
ExecStart=/home/vista/Projects/webcam/telegramBot

[Install]
WantedBy=multi-user.target
```

## 2. Useful links

- [Pyinstaller usage](https://pyinstaller.org/en/stable/usage.html)
- [Telegram send_photo API](https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.sendPhoto)
- [MJPG-Streamer setup example](https://www.sigmdel.ca/michel/ha/rpi/streaming_en.html)
- [Raspberr pi using usb webcam tutorial](https://raspberrypi-guide.github.io/electronics/using-usb-webcams)
