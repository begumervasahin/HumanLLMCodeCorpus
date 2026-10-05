import logging
import binascii
import argparse
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
ENCRYPTION_KEY = '%^*%'
def start(bot, update):
    user_message = update.message.text
    if user_message.startswith('~'):
        decrypted_message = decrypt_message(user_message)
        bot.sendMessage(chat_id=update.message.chat.id, text=decrypted_message)
    else:
        encrypted_message = encrypt_message(user_message)
        bot.sendMessage(chat_id=update.message.chat.id, text=encrypted_message)
def encrypt_message(message):
    hex_message = binascii.hexlify(message.encode('utf-8')).decode('utf-8')
    encrypted_message = xor_strings(hex_message, ENCRYPTION_KEY)
    encrypted_hex = binascii.hexlify(encrypted_message.encode()).decode()
    return "~" + encrypted_hex
def decrypt_message(ciphertext):
    ciphertext = ciphertext[1:]
    ciphertext = binascii.unhexlify(ciphertext.encode()).decode()
    decrypted_message = xor_strings(ciphertext, ENCRYPTION_KEY)
    return binascii.unhexlify(decrypted_message.encode('utf-8')).decode('utf-8')
def xor_strings(a, b):
    return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, itertools.cycle(b))])
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