import telebot

bot = telebot.TeleBot('5708418251:AAGDY-47o-ytYu4qjZ95eD2LFAyecMNLR8g')


@bot.message_handler(commands=['start'])
def start(message):
    if '#Продам' or '#Куплю' or '#Обміняю' or '#Послуга' not in message:
        bot.delete_message(message.chat.id, message.id)


bot.polling()
