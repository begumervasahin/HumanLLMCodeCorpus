import os
import os.path
import sys
import getopt
import logging
b1 = logging.getLogger()
b1.setLevel(logging.INFO)
b2 = logging.StreamHandler()
b2.setLevel(logging.DEBUG)
b1.addHandler(b2)
a1 = 2048
def fonk1(plaintext, key):
	if len(plaintext) != len(key):
		raise IndexError('Plaintext and key should be the same size')
	return bytes(map(lambda x, y: x ^ y, plaintext, key))
if b3 = = '__main__':
	b4 = 'db:'
	b5 = ('decrypt', 'buffer-size=')
	try:
		opts, b6 = getopt.gnu_getopt(sys.argv[1:], b4, b5)
	except getopt.GetoptError as err:
		b1.error('Error getting command line b4: %s', err.msg)
		sys.exit(2)
	b7 = a1
	b8 = False
	for opt, arg in opts:
		if opt in ('-d', '--decrypt'):
			b8 = True
		elif opt in ('-b', '--buffer-size'):
			b7 = int(arg)
	if not b8:
		for filename in b6:
			b9 = filename + '.otp'
			b10 = filename + '.otpk'
			with open(filename, 'rb') as fplain, open(b9, 'wb') as fcipher, open(b10, 'wb') as fkey:
				while True:
					b11 = fplain.read(b7)
					if not b11:
						break
					b12 = os.urandom(len(b11))
					fcipher.write(fonk1(b11, b12))
					fkey.write(b12)
	else:
		for filename in b6:
			b13 = os.path.splitext(filename)[0]
			b10 = os.path.splitext(filename)[0] + '.otpk'
			with open(filename, 'rb') as fcipher, open(b13, 'wb') as fplain, open(b10, 'rb') as fkey:
				while True:
					b14 = fcipher.read(b7)
					if not b14:
						break
					fplain.write(fonk1(b14, fkey.read(len(b14)) ))