# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hello")
    markup = types.ReplyKeyboardMarkup()
    
    markup.row('/help')
    bot.send_message(message.chat.id, "What you need?", reply_markup=markup)

@bot.message_handler(commands = ['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Can i help you?")

@bot.message_handler ( func = lambda  message : True, content_types = ['text'] )
def echo_all ( message ):
    bot.reply_to (message, message.text)




# markup = types.ReplyKeyboardMarkup(row_width=2)
# itembtn1 = types.KeyboardButton('/start')
# markup.add(itembtn1)
# bot.send_message(bot.message.chat_id, "Choose one letter:", reply_markup=markup)

if __name__ == '__main__':
     bot.polling(none_stop=True)