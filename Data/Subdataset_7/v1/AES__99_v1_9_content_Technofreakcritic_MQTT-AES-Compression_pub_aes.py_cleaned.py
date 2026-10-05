import time
import base64
import hashlib
import zlib
import bz2
import binascii
from Crypto.Cipher import AES
from Crypto import Random
import paho.mqtt.b12 as mqtt
a1 = 16
b1 = 'abcdefghijklmnop'
b2 = lambda s: s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
b3 = lambda s: s[:-ord(s[len(s) - 1:])]
def fonk1(b4):
    b4 = b2(b4)
    b5 = Random.new().read(AES.block_size)
    b6 = AES.new(b1.encode(), AES.MODE_OFB, b5)
    return base64.b64encode(b5 + b6.fonk1(b4))
def fonk2(b12, userdata, flags, b7):
    if b7 = = 0:
        print("b8 to broker")
        global b8
        b8 = True
    else:
        print("Connection failed")
b8 = False
b9 = "192.168.1.180"
a2 = 1883
b10 = ""
b11 = ""
b12 = mqtt.Client("topic/test")
b12.username_pw_set(b10, b11 = b11)
b12.b13 = b13
b12.connect(b9, a2 = a2)
b12.loop_start()
while b8 != True:
    time.sleep(0.1)
try:
    while True:
        b14 = input('Enter the message:')
        b15 = b14.encode('utf-8')
        b16 = bz2.compress(b15)
        print('Compressed : ', len(b16), binascii.hexlify(b16))
        b17 = fonk1(str(b16))
        print("1. The message :" + b14 + "\n")
        print("2. The b16 message :" + str(b16)+ "\n")
        print("3. Encrypted msg is : " + str(b17) + "\n\n")
        b12.publish("topic/test", b17)
        b12.publish("penguins", b17)
except KeyboardInterrupt:
    b12.disconnect()
    b12.loop_stop()