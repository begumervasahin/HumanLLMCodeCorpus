
import logging
import binascii
import argparse
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
key = '%^*%'
def start(bot, update):
    user_message = update.message.text
    if user_message.startswith('~'):
        decrypted_message = decrypt(user_message, key)
    else:
        encrypted_message = encrypt(user_message, key)
    bot.sendMessage(chat_id=update.message.chat.id, text=decrypted_message)
def encrypt(msg, key):
    hex_msg = (binascii.hexlify(msg.encode('utf-8'))).decode('utf-8')
    encrypted_msg = xor_str(hex_msg, key)
    cipher = (binascii.hexlify(encrypted_msg.encode())).decode()
    cipher = "~" + cipher
    return cipher
def decrypt(cipher, key):
    cipher = cipher[1:]
    cipher = (binascii.unhexlify(cipher.encode())).decode()
    msg = xor_str(cipher, key)
    msg = (binascii.unhexlify(msg.encode('utf-8'))).decode('utf-8')
    return msg
def xor_str(a, b):
    xor_result = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return xor_result
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