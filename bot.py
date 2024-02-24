import time

import telebot
import sqlite3


bot = telebot.TeleBot('6844456223:AAGARA98_HQ4Y1aEWNrh5pHfYJAP4yJYEmY')


@bot.message_handler(commands=["start"])
def start(message):
    """
    The function connects to database 'db/database'
    if server is down ->
    this function sends ping result in Telegram
    :param message: [str] user message
    :return: None
    """
    bot.send_message(message.chat.id, "Начинаю проверку серверов, если что-то не так я сообщу...")
    db = sqlite3.connect('db/database.db')
    while True:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM urls")
        items = cursor.fetchall()
        if items:
            for address in items:
                bot.send_message(message.chat.id, "сервер: " + address[0] + " упал")
        time.sleep(30)


bot.polling()
