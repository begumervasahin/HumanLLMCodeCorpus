
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, binascii, argparse, itertools
key='%^*%
def start(bot, update):
    u=update.message.text
    if u[0]=='~':
        m=decrypt(u,key)
    else:
        m=encrypt(u,key)
    bot.sendMessage(chat_id=update.message.chat.id, text=m)
def encrypt(msg, key):
    '''Return cipher text'''
    msg= (binascii.hexlify(msg.encode('utf-8'))).decode('utf-8')
    msg= xor_str(msg, key)
    cipher= (binascii.hexlify(msg.encode())).decode()
    cipher="~%s" %cipher
    return cipher
def decrypt(cipher, key):
    '''Return plain text message'''
    cipher=cipher[1:]
    cipher = (binascii.unhexlify(cipher.encode())).decode()
    msg = xor_str(cipher, key)
    msg = (binascii.unhexlify(msg.encode('utf-8'))).decode('utf-8')
    return msg
def xor_str(a, b):
    '''Return the xor of the two strings a and b
    The length of the output string is the same as that of first string,
    which means that if second string is shorter than first, it'll be repeated
    over.'''
    xorred = ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return xorred
def main():
    updater = Updater("TOKEN")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler([Filters.text], start))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()