import os
import configparser
from telebot import types, TeleBot

def readInfoTxt(catalog):
    infoRaw = open(catalog+"/info.txt", "r")
    Info = infoRaw.readlines()
    infoRaw.close()
    return Info
   
# Берем токен из настроек и подключаемся к боту
config = configparser.ConfigParser()
config.read("settings.ini")
APIToken = config["Telegram"]["token"]
bot = TeleBot(APIToken)

# Читаем пункты меню
listDirMenu = os.listdir('menu')
for dir in listDirMenu:
    menuInfo = readInfoTxt(dir)
    menuDict = {dir:menuInfo}
keyboardForChat = []


def menu_keyboard():
    for menuPoint in menuDict.keys():
        keyboardForChat.append(types.InlineKeyboardButton(text=menuPoint, callback_data=menuPoint))
    return types.InlineKeyboardMarkup(keyboard=[keyboardForChat])


def back_keyboard():
    return types.InlineKeyboardMarkup(keyboard=[[types.InlineKeyboardButton(text='⬅', callback_data='back')]])


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    aboutInfo = readInfoTxt("start")
    bot.reply_to(message, aboutInfo, reply_markup=menu_keyboard())


@bot.callback_query_handler(func=lambda c: c.data == 'back')
def back_callback(call: types.CallbackQuery):
    aboutInfo = readInfoTxt("About")
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=aboutInfo, reply_markup=menu_keyboard())


@bot.callback_query_handler(func=lambda c: c.data in menuDict.keys())
def menu_callback(call: types.CallbackQuery):
    menuInfo = readInfoTxt("menu/"+call.text)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=menuInfo, reply_markup=back_keyboard())

bot.infinity_polling()