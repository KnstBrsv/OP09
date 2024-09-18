import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я первый тренировочный бот Константина!')
    greeting_thread = threading.Thread(target=send_greeting, args=(message.chat.id,))
    greeting_thread.start()


@bot.message_handler(commands=['greet'])
def greet_message(message):
    list = ['русском: Привет! Как дела?', 'английском: Hello! How are you?', 'немецком: Hallo! Wie geht es dir?',
            'французском: Bonjour! Comment allez-vous?', 'испанском: ¡Hola! ¿Cómo estás?']
    random_grtns = random.choice(list)
    bot.reply_to(message, f'Приветствие на {random_grtns}')


def get_greeting():
    greetings = {"09:00": "Good morning!",
                 "14:20": "Guten Tag!",
                 "19:00": "Bonne soirée!",
                 "23:00": "¡Buenos notches!"}
    now = datetime.datetime.now().strftime("%H:%M")
    if now in greetings:
        return greetings[now]
    else:
        return None


def send_greeting(chat_id):
    while True:
        if get_greeting() is not None:
            bot.send_message(chat_id, get_greeting())
        time.sleep(60)


bot.polling(non_stop=True)
