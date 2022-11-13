import telebot
from telebot import TeleBot

# t.me/BuntinMA_calculator_Bot.
bot = telebot.TeleBot('5533837130:AAGroDJvDdmvAH1Dzrf1xNZzFKplyL7FA9A')


def summator(text):
    lst = text.split()
    if len(lst) == 2 and lst[0].isdigit and lst[1].isdigit:
        return str(int(lst[0]) + int(lst[1]))
    return "error"


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summator(msg.text))


bot.polling()