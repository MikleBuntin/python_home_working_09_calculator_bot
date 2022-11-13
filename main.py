import telebot
from telebot import TeleBot
from telebot import types
import calculator


# t.me/BuntinMA_calculator_Bot.
bot = telebot.TeleBot('5533837130:AAGroDJvDdmvAH1Dzrf1xNZzFKplyL7FA9A')

def summator(msg: telebot.types.Message):
    lst = msg.split()
    if len(lst) == 2 and lst[0].isdigit and lst[1].isdigit:
        return str(int(lst[0]) + int(lst[1]))
    return "error"

help = "/start - начало программы; \n /help - помощь; \n "
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Привет!".format(message.from_user))
    bot.send_message(message.chat.id, help)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "/help"):
        bot.send_message(message.chat.id, help)

    else:
        bot.send_message(message.chat.id, text=calculator(message.text))



        # bot.send_message(message.chat.id, text="Странная команда...")



bot.polling()