
import logging
import binascii
import argparse
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
b1 = '%^*%'
def fonk1(bot, update):
    b2 = update.message.text
    if b2.startswith('~'):
        b3 = fonk3(b2, b1)
    else:
        b4 = fonk2(b2, b1)
    bot.sendMessage(b5 = update.message.chat.id, text=b3)
def fonk2(b9, b1):
    b6 = (binascii.hexlify(b9.encode('utf-8'))).decode('utf-8')
    b7 = fonk4(b6, b1)
    b8 = (binascii.hexlify(b7.encode())).decode()
    b8 = "~" + b8
    return b8
def fonk3(b8, b1):
    b8 = b8[1:]
    b8 = (binascii.unhexlify(b8.encode())).decode()
    b9 = fonk4(b8, b1)
    b9 = (binascii.unhexlify(b9.encode('utf-8'))).decode('utf-8')
    return b9
def fonk4(a, b):
    b10 = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return b10
def fonk5():
    b11 = Updater("TOKEN")
    b12 = b11.dispatcher
    b12.add_handler(CommandHandler("start", start))
    b12.add_handler(CommandHandler("help", help))
    b12.add_handler(MessageHandler([Filters.text], start))
    b11.start_polling()
    b11.idle()
if b13 = = '__main__':
    fonk5()