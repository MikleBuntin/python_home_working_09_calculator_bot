import telebot
from telebot import TeleBot

# t.me/BuntinMA_calculator_Bot.
bot = telebot.TeleBot('5533837130:AAGroDJvDdmvAH1Dzrf1xNZzFKplyL7FA9A')
@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f"Вы прислали: {msg.text}")


bot.polling()