#! /usr/bin/python

import telebot
import requests
from PIL import Image
from io import BytesIO

bot = telebot.TeleBot("your_telegram_bot_token")


def take_photo():
    response = requests.get('http://localhost:8084/?action=snapshot')
    return Image.open(BytesIO(response.content))


@bot.message_handler(commands=['snapshot'])
def send_photo(message):
    print('[INFO] Sending snapshot...')
    try:
        bot.send_photo(message.chat.id, take_photo())
        print('[INFO] Snapshot sended!')
    except:
        print('[ERROR] Failed to send snapshot!')


print('[INFO] Telegram bot listening...')
bot.polling()
