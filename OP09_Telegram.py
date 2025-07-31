# Telegram bot
import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('7763593032:AAH9nUfnF94Cop22CPlBir1-2DIxMdAQGOg')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Это тестовое сообщение от чатБота")
    # Ниже прописываем поток
    # Thread — функция, которая создает поток,
    # target — то, куда будет сохраняться название функции, которую мы запускаем в потоке,
    # send_reminders — используемая функция,
    # args — аргументы, которые надо передать.
    reminder_thread = threading.Thread(target=send_reminder, args=(message.chat.id,)) # Запятая нужна потому что обычно все аргументы передаются в виде картежа.
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = ['**Гидра — потенциально бессмертное существо**',
            '**Крионика — путь к технологическому бессмертию**',
            '**Информационное бессмертие через цифровизацию сознания**']
    random_fact = random.choice(list)
    bot.reply_to(message, f"Привет! Лови факт о бессмертии {random_fact}")

def send_reminder(chat_id):
    first_rem = "09:00"
    second_rem = "14:00"
    end_rem = "18:00"
    while True: # Запускаем бесконечный цикл который будет работать постоянно
        # datetime - это встроенный модуль Python для работы с датой и временем
        # datetime.now() - метод, который возвращает объект datetime с текущими
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Тестовое напоминание")
            time.sleep(61) # интервал проверки условия
        time.sleep(1) # интервал работы цикла while чтобы запросы были не постоянными а 1 раз в секунду


bot.polling(none_stop=True)





