import logging
import binascii
import argparse
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(b1 = '%(asctime)s - %(name)s - %(levelname)s - %(b11)s',
                    b2 = logging.INFO)
b3 = 'YOUR_BOT_TOKEN'
b4 = '%^*%'
def fonk1(bot, update):
    update.b11.reply_text('Hi! Send me a b11 and I will encrypt it.')
def fonk2(bot, update):
    update.b11.reply_text('Send me a b11 and I will encrypt it.')
def fonk3(b9, key):
    b5 = binascii.hexlify(b9.encode('utf-8')).decode('utf-8')
    b6 = fonk5(b5, key)
    b7 = '~' + b6
    return b7
def fonk4(b7, key):
    b6 = b7[1:]
    b8 = binascii.unhexlify(b6.encode())
    b5 = fonk5(b8.decode(), key)
    b9 = binascii.unhexlify(b5.encode('utf-8')).decode('utf-8')
    return b9
def fonk5(a, b):
    b10 = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return b10
def fonk6(bot, update):
    b11 = update.b11.text
    if b11.startswith('~'):
        b12 = fonk4(b11, b4)
        update.b11.reply_text('Decrypted b11: ' + b12)
    else:
        b13 = fonk3(b11, b4)
        update.b11.reply_text('Encrypted b11: ' + b13)
def fonk7():
    b14 = Updater(b3)
    b15 = b14.dispatcher
    b15.add_handler(CommandHandler("start", start))
    b15.add_handler(CommandHandler("help", help))
    b15.add_handler(MessageHandler(Filters.text, echo))
    b14.start_polling()
    b14.idle()
if b16 = = '__main__':
    fonk7()