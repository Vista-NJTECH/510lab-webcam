#! /usr/bin/python

import telebot
import requests
from PIL import Image
from io import BytesIO

bot = telebot.TeleBot("telebot_token")


def take_photo(cam):
    host = "172.18.192.245"
    if cam == 2:
        host = "172.18.192.199"
    path = "http://{}:8084/?action=snapshot".format(host)
    response = requests.get(path)
    return Image.open(BytesIO(response.content))


def send_photo(msg, cam):
    print('[INFO] Sending snapshot...')
    try:
        bot.send_photo(msg.chat.id, take_photo(cam))
        print('[INFO] Snapshot sent!')
    except:
        bot.send_message(msg.chat.id, "Snapshot failed!")
        print('[ERROR] Snapshot failed!')


@bot.message_handler(commands=['snapshot'])
def send_photo_handler(msg):
    send_photo(msg, 1)


@bot.message_handler(commands=['snapshot2'])
def send_photo_handler(msg):
    send_photo(msg, 2)


print('[INFO] Telegram bot listening...')

bot.polling()
