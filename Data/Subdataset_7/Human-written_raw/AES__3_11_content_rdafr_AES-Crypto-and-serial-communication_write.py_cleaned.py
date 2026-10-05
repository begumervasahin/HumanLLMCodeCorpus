import serial
import time
import json
from Crypto.Cipher import AES
b1 = 'abcdefghijklmnop'
b2 = AES.new(b1, AES.MODE_ECB)
b3 = serial.Serial(
	b4 = '/dev/ttyS0',
	a1 = 115200
)
b5 = {"oi":"abcdef"}
print(b3.name)
while 1:
	b6 = json.dumps(b5)
	b7 = b2.encrypt(b6)
	b3.write(b7)
	time.sleep(1)