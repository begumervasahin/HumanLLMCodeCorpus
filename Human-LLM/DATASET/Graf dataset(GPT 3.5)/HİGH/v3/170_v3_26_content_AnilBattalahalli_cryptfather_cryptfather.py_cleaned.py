import logging
import binascii
import argparse
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(b1 = '%(asctime)s - %(name)s - %(levelname)s - %(b9)s',
                    b2 = logging.INFO)
b3 = 'YOUR_BOT_TOKEN'
b4 = '%^*%'
def fonk1(bot, update):
    update.b9.reply_text('Hi! Send me a b9 and I will encrypt it.')
def fonk2(bot, update):
    update.b9.reply_text('Send me a b9 and I will encrypt it.')
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
    b9 = update.b9.text
    if b9.startswith('~'):
        b11 = fonk4(b9, b4)
        update.b9.reply_text('Decrypted b9: ' + b11)
    else:
        b12 = fonk3(b9, b4)
        update.b9.reply_text('Encrypted b9: ' + b12)
def fonk7():
    b13 = Updater(b3)
    b14 = b13.b14
    b14.add_handler(CommandHandler("start", start))
    b14.add_handler(CommandHandler("help", help))
    b14.add_handler(MessageHandler(Filters.text, handle_incoming_message))
    b13.start_polling()
    b13.idle()
if b15 = = '__main__':
    fonk7()