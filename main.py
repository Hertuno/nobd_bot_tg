import telebot
from telebot.types import ReplyKeyboardMarkup
from datetime import time

try:
    # Берем токен из настроек и подключаемся к боту
    with open("Настройки.txt", "r") as n:
        APIToken = n.read()
    bot = telebot.TeleBot(APIToken, threaded=False)
    # Читаем пункты меню "Возможности" и описание самого меню
    row_for_keyboard = []
    with open("Пункты.txt", "r") as p:
        for line in p.readlines():
            row_for_keyboard.append(line)
    with open("Возможности.txt", "r") as v:
        skills_description = v.read()
    # Загружаем сами возможности
    skill_list = []
    keys = 1
    while keys < 12:
        with open("Возможности/" + str(keys) + ".txt", "r") as k:
            skill_list.append(k.read())
            keys = keys + 1
except Exception as error:
    print(error)

def gen_keyboard_markup(keyboard_type):
    try:
        menu_keyboard = ReplyKeyboardMarkup(True, True)
        if keyboard_type == "main_menu":
            menu_keyboard.row('📨КОНТАКТЫ', '🧩ВОЗМОЖНОСТИ')
        elif keyboard_type == "back_to_menu":
            menu_keyboard.row('◀️НАЗАД В МЕНЮ')
        elif keyboard_type == "back_to_skills":
            menu_keyboard.row('◀️НАЗАД К ВОЗМОЖНОСТЯМ')
        elif keyboard_type == "skills_menu":
            for row in row_for_keyboard:
                menu_keyboard.row(row)
            menu_keyboard.row('◀️НАЗАД В МЕНЮ')
    except Exception as error:
        print(error)
    finally:
        return menu_keyboard


def shorter_message(text):
    short_text = text.split('@--')
    return short_text


@bot.message_handler(commands=['start'])
def chat_commands(message):
    try:
        if message.text == "/start":
            print("bot.chat_commands😝Мне написали /start")
            bot.send_message(message.chat.id, "*️⃣Добро пожаловать!",
                             reply_markup=gen_keyboard_markup("main_menu"))
        else:
            pass
    except Exception as errorException:
        print(errorException)


@bot.message_handler(content_types=['text'])
def start(message):  # основная функция не важна
    try:
        if message.text == '📨КОНТАКТЫ':
            bot.send_photo(message.chat.id, open('Изображения/Контакты.jpg', 'rb'),
                           reply_markup=gen_keyboard_markup("back_to_menu"))
        elif message.text == '🧩ВОЗМОЖНОСТИ' or message.text == '◀️НАЗАД К ВОЗМОЖНОСТЯМ':
            bot.send_message(message.chat.id, skills_description,
                             reply_markup=gen_keyboard_markup("skills_menu"))
        elif message.text == '◀️НАЗАД В МЕНЮ':
            bot.send_message(message.chat.id, "Хотели что-то еще?",
                             reply_markup=gen_keyboard_markup("main_menu"))
        elif message.text in row_for_keyboard[0]:
            final_message = shorter_message(skill_list[0])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[1]:
            final_message = shorter_message(skill_list[1])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[2]:
            final_message = shorter_message(skill_list[2])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[3]:
            final_message = shorter_message(skill_list[3])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[4]:
            final_message = shorter_message(skill_list[4])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[5]:
            final_message = shorter_message(skill_list[5])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[6]:
            final_message = shorter_message(skill_list[6])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[7]:
            final_message = shorter_message(skill_list[7])
            for skill in final_message:
                bot.send_message(message.chat.id, skill)
            bot.send_photo(message.chat.id, open('Изображения/Схема.jpg', 'rb'),
                           reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[8]:
            final_message = shorter_message(skill_list[8])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[9]:
            final_message = shorter_message(skill_list[9])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                             reply_markup=gen_keyboard_markup("back_to_skills"))
        elif message.text in row_for_keyboard[10]:
            final_message = shorter_message(skill_list[10])
            for skill in final_message:
                bot.send_message(message.chat.id, skill,
                                 reply_markup=gen_keyboard_markup("back_to_skills"))
        else:
            bot.send_message(message.chat.id, "*️⃣Добро пожаловать!",
                             reply_markup=gen_keyboard_markup("main_menu"))
    except Exception as error_exception:
        print(error_exception)


while True:
    try:
        bot.polling(none_stop=True, timeout=123)
    except Exception as error:
        print(error)
        time.sleep(5)
    finally:
        print("bot.infinity_polling Пробую еще раз")
