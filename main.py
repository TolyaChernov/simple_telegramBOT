import random

import requests  # # pip install requests
import telebot
from bs4 import BeautifulSoup as BS  # # pip install beautifulsoup4
from telebot import types

from telegram_key import key
from utils import f_meth, f_pos

bot = telebot.TeleBot(key)


def anekdot():
    """ Вывод текста из html страницы """
    url = "https://www.anekdot.ru/last/anekdot/"
    r = requests.get(url)
    html = BS(r.content, "html.parser")

    temp = html.find_all("div", class_="text")
    anekdots_list = []
    for i in temp:
        anekdots_list.append(i.get_text(strip=True, separator=" "))
    random.shuffle(anekdots_list)
    return anekdots_list[0]


def pos(name: str):
    """
    Вывод информации из БД

    Args:
        name (str):

    """
    result = f_pos(name)
    try:
        return result
    except IndexError:
        pass


def meth(name: str):
    """
    Вывод информации из БД

    Args:
        name (str):

    """
    result = f_meth(name)
    try:
        return result
    except IndexError:
        pass


@bot.message_handler(commands=["start"])
def start(message: str):
    """
    Запуск телеграмм бота

    Args:
        message (str):

    """
    print(message, type(message))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Положение при сварке")
    btn2 = types.KeyboardButton("Способы сварки")
    btn3 = types.KeyboardButton("Анекдот")
    markup.add(btn1, btn2, btn3)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nСджелай свой выбор"
    bot.send_message(
        message.chat.id,
        send_mess,
        parse_mode="html",
        reply_markup=markup)


@bot.message_handler(content_types=["text"])
def mess(message: str):
    """
    Ответ на запросы из тгбота

    Args:
        message (str):

    """
    get_message_bot = message.text.strip().lower()

    lst_meth = ["mma", "tig", "mig/mag"]
    lst_pos = ["pa", "pb", "pc", "pd", "pe", "pf", "pg"]

    if get_message_bot == "анекдот":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Положение при сварке")
        btn2 = types.KeyboardButton("Способы сварки")
        btn3 = types.KeyboardButton("Анекдот")
        markup.add(btn1, btn2, btn3)

        mess_anekdot = anekdot()

        bot.send_message(
            message.chat.id,
            f"{mess_anekdot}",
            parse_mode="html",
            reply_markup=markup,
        )
        print(
            message.from_user.first_name,
            message.from_user.last_name,
            "- раздел анекдоты",
        )

    elif get_message_bot == "способы сварки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("MMA")
        btn2 = types.KeyboardButton("TIG")
        btn3 = types.KeyboardButton("MIG/MAG")
        btn4 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(
            message.chat.id,
            f"Цифровое обозначение это классификация способов сварки в соответствии с ISO 4063. \nTIG  это 141 \nMMA это 111 \nMIG это 131 \nMAG это 135",
            parse_mode="html",
            reply_markup=markup,
        )
        print(
            message.from_user.first_name,
            message.from_user.last_name,
            "- раздел способы сварки",
        )

    elif get_message_bot in lst_meth:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("MMA")
        btn2 = types.KeyboardButton("TIG")
        btn3 = types.KeyboardButton("MIG/MAG")
        btn4 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4)

        text = get_message_bot
        print(text)
        mess = meth(text)

        bot.send_message(
            message.chat.id,
            f"Ответ на запрос: \n {mess}",
            parse_mode="html",
            reply_markup=markup,
        )
        print(
            message.from_user.first_name,
            message.from_user.last_name,
            "- раздел способы сварки",
        )

    elif get_message_bot == "положение при сварке":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton("PA")
        btn2 = types.KeyboardButton("PB")
        btn3 = types.KeyboardButton("PC")
        btn4 = types.KeyboardButton("PD")
        btn5 = types.KeyboardButton("PE")
        btn6 = types.KeyboardButton("PF")
        btn7 = types.KeyboardButton("PG")
        btn8 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

        bot.send_message(
            message.chat.id,
            f"Выберите интересующее Вас положение при сварке",
            parse_mode="html",
            reply_markup=markup,
        )
        print(
            message.from_user.first_name,
            message.from_user.last_name,
            "- раздел положение при сварке",
        )

    elif get_message_bot in lst_pos:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton("PA")
        btn2 = types.KeyboardButton("PB")
        btn3 = types.KeyboardButton("PC")
        btn4 = types.KeyboardButton("PD")
        btn5 = types.KeyboardButton("PE")
        btn6 = types.KeyboardButton("PF")
        btn7 = types.KeyboardButton("PG")
        btn8 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

        text = get_message_bot
        print(text)
        mess = pos(text)

        bot.send_message(
            message.chat.id,
            f"Ответ на запрос: \n {mess}",
            parse_mode="html",
            reply_markup=markup,
        )
        print(
            message.from_user.first_name,
            message.from_user.last_name,
            "- раздел положение при сварке",
        )

    elif get_message_bot == "старт":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Положение при сварке")
        btn2 = types.KeyboardButton("Способы сварки")
        btn3 = types.KeyboardButton("Анекдот")
        markup.add(btn1, btn2, btn3)
        send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nЧто Вас интересует?"
        bot.send_message(
            message.chat.id, send_mess, parse_mode="html", reply_markup=markup
        )
        print(
            message.from_user.first_name,
            message.from_user.last_name,
            "- старт")

    elif get_message_bot == "назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Положение при сварке")
        btn2 = types.KeyboardButton("Способы сварки")
        btn3 = types.KeyboardButton("Анекдот")
        markup.add(btn1, btn2, btn3)
        send_mess = f"Что Вас интересует?"
        bot.send_message(
            message.chat.id, send_mess, parse_mode="html", reply_markup=markup
        )
        print(
            message.from_user.first_name,
            message.from_user.last_name,
            "- назад")

    else:
        bot.send_message(message.chat.id, "Извините. ", parse_mode="html")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Положение при сварке")
        btn2 = types.KeyboardButton("Способы сварки")
        btn3 = types.KeyboardButton("Анекдот")
        markup.add(btn1, btn2, btn3)
        final_message = "Произошла ошибка"
        bot.send_message(
            message.chat.id, final_message, parse_mode="html", reply_markup=markup
        )
        print(
            message.from_user.first_name,
            message.from_user.last_name,
            "- ошибка")


bot.polling(none_stop=True)
