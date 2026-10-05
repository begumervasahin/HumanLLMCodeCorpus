
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, binascii, argparse, itertools
b1 = '%^*%
def fonk1(bot, update):
    b2 = update.message.text
    if b2[0]=='~':
        b3 = fonk3(b2,b1)
    else:
        b3 = fonk2(b2,b1)
    bot.sendMessage(b4 = update.message.chat.id, text=b3)
def fonk2(b5, b1):
    '''Return b6 text'''
    b5 = (binascii.hexlify(b5.encode('utf-8'))).decode('utf-8')
    b5 = fonk4(b5, b1)
    b6 = (binascii.hexlify(b5.encode())).decode()
    b6 = "~%s" %b6
    return b6
def fonk3(b6, b1):
    '''Return plain text message'''
    b6 = b6[1:]
    b6 = (binascii.unhexlify(b6.encode())).decode()
    b5 = fonk4(b6, b1)
    b5 = (binascii.unhexlify(b5.encode('utf-8'))).decode('utf-8')
    return b5
def fonk4(a, b):
    '''Return the xor of the two strings a and b
    The length of the output string is the same as that of first string,
    which means that if second string is shorter than first, it'll be repeated
    over.'''
    b7 = ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return b7
def fonk5():
    b8 = Updater("TOKEN")
    b9 = b8.dispatcher
    b9.add_handler(CommandHandler("start", start))
    b9.add_handler(CommandHandler("help", help))
    b9.add_handler(MessageHandler([Filters.text], start))
    b8.start_polling()
    b8.idle()
if b10 = = '__main__':
    fonk5()