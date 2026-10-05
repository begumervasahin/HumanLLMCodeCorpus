import logging
import binascii
import argparse
import itertools
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
TOKEN = 'YOUR_BOT_TOKEN'
KEY = '%^*%'
def start(bot, update):
    update.message.reply_text('Hi! Send me a message and I will encrypt it.')
def help(bot, update):
    update.message.reply_text('Send me a message and I will encrypt it.')
def encrypt_message(message, key):
    msg_hex = binascii.hexlify(message.encode('utf-8')).decode('utf-8')
    cipher_hex = xor_strings(msg_hex, key)
    cipher = '~' + cipher_hex
    return cipher
def decrypt_message(cipher, key):
    cipher_hex = cipher[1:]
    cipher_bytes = binascii.unhexlify(cipher_hex.encode())
    msg_hex = xor_strings(cipher_bytes.decode(), key)
    message = binascii.unhexlify(msg_hex.encode('utf-8')).decode('utf-8')
    return message
def xor_strings(a, b):
    xor_result = ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, itertools.cycle(b))])
    return xor_result
def handle_incoming_message(bot, update):
    message = update.message.text
    if message.startswith('~'):
        decrypted_message = decrypt_message(message, KEY)
        update.message.reply_text('Decrypted message: ' + decrypted_message)
    else:
        encrypted_message = encrypt_message(message, KEY)
        update.message.reply_text('Encrypted message: ' + encrypted_message)
def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_incoming_message))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()