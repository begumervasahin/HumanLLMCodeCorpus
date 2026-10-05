import os
import sys
import getopt
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
logger.addHandler(consoleHandler)
DEFAULT_BUFFER_SIZE = 2048
def xor(plaintext, key):
    if len(plaintext) != len(key):
        raise IndexError('Plaintext and key should be the same size')
    return bytes(map(lambda x, y: x ^ y, plaintext, key))
if __name__ == '__main__':
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'db:', ['decrypt', 'buffer-size='])
    except getopt.GetoptError as err:
        logger.error('Error getting command line options: %s', err.msg)
        sys.exit(2)
    BUFFER_SIZE = DEFAULT_BUFFER_SIZE
    decrypting = False
    for opt, arg in opts:
        if opt in ('-d', '--decrypt'):
            decrypting = True
        elif opt in ('-b', '--buffer-size'):
            BUFFER_SIZE = int(arg)
    for filename in args:
        if not decrypting:
            fcipher_name = filename + '.otp'
            fkey_name = filename + '.otpk'
            with open(filename, 'rb') as fplain, open(fcipher_name, 'wb') as fcipher, open(fkey_name, 'wb') as fkey:
                while True:
                    buffer_plain = fplain.read(BUFFER_SIZE)
                    if not buffer_plain:
                        break
                    buffer_key = os.urandom(len(buffer_plain))
                    fcipher.write(xor(buffer_plain, buffer_key))
                    fkey.write(buffer_key)
        else:
            fplain_name = os.path.splitext(filename)[0]
            fkey_name = fplain_name + '.otpk'
            with open(filename, 'rb') as fcipher, open(fplain_name, 'wb') as fplain, open(fkey_name, 'rb') as fkey:
                while True:
                    buffer_cipher = fcipher.read(BUFFER_SIZE)
                    if not buffer_cipher:
                        break
                    fplain.write(xor(buffer_cipher, fkey.read(len(buffer_cipher)))))