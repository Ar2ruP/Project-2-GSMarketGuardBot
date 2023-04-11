import telebot

bot = telebot.TeleBot('Telegram API')


@bot.message_handler(commands=['start'])
def start(message):
    if '#Продам' or '#Куплю' or '#Обміняю' or '#Послуга' not in message:
        bot.delete_message(message.chat.id, message.id)


bot.polling()
