import telebot
from telebot import types
import time
import os

TOKEN = 'token @botfather'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Привет отправь мне любой код на python, и я его упакую в файл')

@bot.message_handler(content_types=['text'])
def pack_to_py(message):
	with open(str(message.chat.id) + '.py', 'w', encoding='utf-8') as msg_file:
		msg_file.write(message.text)
	doc = open(str(message.chat.id) + ".py", 'rb')
	cap = "`python " + str(message.chat.id) + ".py`"
	bot.send_document(message.chat.id, doc, caption=cap, parse_mode="Markdown")

bot.polling(none_stop=True)
