import telebot

bot = telebot.TeleBot("7763593032:AAH9nUfnF94Cop22CPlBir1-2DIxMdAQGOg")

@bot.message_handler(commands=['start'])
def send_wel(mes1):
    bot.reply_to(mes1, 'Привет это бот домашнего задания по созданию Телеграм Бота. Если хочешь узнать как мной управлять набери - "/help"')

@bot.message_handler(commands=['help'])
def send_help(mes2):
    bot.reply_to(mes2, '1) Хочишь получить текст, введи - "Текст" без ковычек'
                       '\n2)Хочешь получить фотку, введи - "Фото"'
                       '\n3)Хочешь получить видеофайл, введи - "Видео"'
                       '\n4)Хочешь просмотреть видео в интернете, введи - "Интер"'
                 )
@bot.message_handler(func=lambda message: True)
def send_text(mes_res):
    send_telega = mes_res.text
    if send_telega.lower() == "видео":
        with open('C:/Users/Anton_B/Documents/Python от Zerocoder/s_DR.mp4', 'rb') as video_telega:
            bot.send_video(mes_res.chat.id, video_telega)
    elif send_telega.lower() == "фото":
        with open('C:/Users/Anton_B/Documents/Python от Zerocoder/Лайка.jpg', 'rb') as foto_telega:
            bot.send_photo(mes_res.chat.id, foto_telega)
    elif send_telega.lower() == "текст":
        bot.reply_to(mes_res, '- Роза Львовна, а когда наступает старость?'
                              '\n- Когда косметичка превращается в аптечку...')
    elif send_telega.lower() == "интер":
        file_id = "1ddr_KGv1buViBMXgVfu3y7X0th9CBpma"
        video_url = f"https://drive.google.com/uc?export=download&id={file_id}"
        bot.send_video(mes_res.chat.id, video_url)
    else:
        bot.reply_to(mes_res, 'Я же не искуственный Антилект чтоб угадать чего ты хочешь, я весьма ограничен, так что следуй инструкциям')

bot.polling()