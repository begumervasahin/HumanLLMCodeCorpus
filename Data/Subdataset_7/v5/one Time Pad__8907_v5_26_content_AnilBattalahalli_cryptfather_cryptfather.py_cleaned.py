import logging
import binascii
import argparse
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
b1 = '%^*%'
def fonk1(bot, update):
    b2 = update.message.text
    if b2.startswith('~'):
        b3 = fonk3(b2)
        bot.sendMessage(b4 = update.message.chat.id, text=b3)
    else:
        b5 = fonk2(b2)
        bot.sendMessage(b4 = update.message.chat.id, text=b5)
def fonk2(message):
    b6 = binascii.hexlify(message.encode('utf-8')).decode('utf-8')
    b5 = fonk4(b6, b1)
    b7 = binascii.hexlify(b5.encode()).decode()
    return "~" + b7
def fonk3(b8):
    b8 = b8[1:]
    b8 = binascii.unhexlify(b8.encode()).decode()
    b3 = fonk4(b8, b1)
    return binascii.unhexlify(b3.encode('utf-8')).decode('utf-8')
def fonk4(a, b):
    return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, itertools.cycle(b))])
def fonk5():
    b9 = Updater("TOKEN")
    b10 = b9.dispatcher
    b10.add_handler(CommandHandler("start", start))
    b10.add_handler(CommandHandler("help", help))
    b10.add_handler(MessageHandler([Filters.text], start))
    b9.start_polling()
    b9.idle()
if b11 = = '__main__':
    fonk5()