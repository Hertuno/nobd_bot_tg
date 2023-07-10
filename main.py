import os
import configparser
import telebot
from telebot import types
from telebot.util import quick_markup


config = configparser.ConfigParser()
config.read("settings.ini")
token = config["Telegram"]["token"]
bot = telebot.TeleBot(token)
listDirMenu = os.listdir('menu')


def readInfoTxt(catalog):
    Info = False
    with open(catalog+"/info.txt", "r") as infoRaw:
        Info = infoRaw.readlines()
    return Info


def gen_markup():
    menuDict = {}
    markupRow = {}

    for dir in listDirMenu:
        menuInfo = readInfoTxt("menu/"+dir)
        menuDict[dir] = menuInfo

    for menuPoint in menuDict:
        markupRow[menuPoint] = {'callback_data': menuPoint}

    markup = quick_markup(markupRow, int(config["Menu"]["menuRows"])) 
    return markup


def back_keyboard():
    return types.InlineKeyboardMarkup(keyboard=[[types.InlineKeyboardButton(text='⬅', callback_data='back')]])


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    aboutInfo = readInfoTxt("start")
    with open("start"+"/photo.jpg", "rb") as photoRaw:
        bot.send_photo(message.chat.id, photoRaw)
    if aboutInfo:
        for info in aboutInfo:
            bot.send_message(message.chat.id, info, reply_markup=gen_markup())


@bot.callback_query_handler(func=lambda c: c.data == 'back')
def back_callback(call: types.CallbackQuery):
    aboutInfo = readInfoTxt("start")
    with open("start"+"/photo.jpg", "rb") as photoRaw:
        bot.send_photo(call.message.chat.id, photoRaw)
    if aboutInfo:
        for info in aboutInfo:
            bot.send_message(call.message.chat.id, info, reply_markup=gen_markup())


@bot.callback_query_handler(func=lambda c: c.data in listDirMenu)
def menu_callback(call: types.CallbackQuery):
    menuInfo = readInfoTxt("menu/"+call.data)
    with open("menu/"+call.data+"/photo.jpg", "rb") as photoRaw:
        bot.send_photo(call.message.chat.id, photoRaw)
    if menuInfo:
        for info in menuInfo:
            bot.send_message(call.message.chat.id, info, reply_markup=back_keyboard())


bot.infinity_polling()