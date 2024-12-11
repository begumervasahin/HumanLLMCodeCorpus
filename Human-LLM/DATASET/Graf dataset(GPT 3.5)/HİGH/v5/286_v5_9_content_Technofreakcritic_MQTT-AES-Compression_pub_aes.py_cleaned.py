import time
import base64
import binascii
import bz2
import zlib
from Crypto.Cipher import AES
from Crypto import Random
import paho.mqtt.b11 as mqtt
import key_gen as kg
a1 = 16
b1 = 'abcdefghijklmnop'
b2 = False
b3 = "192.168.1.180"
a2 = 1883
b4 = ""
b5 = ""
b6 = "topic/test"
def fonk1(s):
    return s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
def fonk2(s):
    return s[:-ord(s[len(s) - 1:])]
def fonk3(b7):
    b7 = fonk1(b7)
    b8 = Random.new().read(AES.block_size)
    b9 = AES.new(b1.encode(), AES.MODE_OFB, b8)
    return base64.b64encode(b8 + b9.fonk3(b7))
def fonk4(b11, userdata, flags, b10):
    if b10 = = 0:
        print("b2 to broker")
        global b2
        b2 = True
    else:
        print("Connection failed")
b11 = mqtt.Client(b6)
b11.username_pw_set(b4, b12 = b5)
b11.b13 = b13
b11.connect(b3, b14 = a2)
b11.loop_start()
while not b2:
    time.sleep(0.1)
try:
    while True:
        b15 = input('Enter the message:')
        b16 = bz2.compress(b15.encode('utf-8'))
        print('Compressed: ', len(b16), binascii.hexlify(b16))
        b17 = fonk3(str(b16))
        print("1. The message: " + b15 + "\n")
        print("2. The b16 message: " + str(b16)+ "\n")
        print("3. Encrypted message: " + str(b17) + "\n\n")
        b11.publish("topic/test", b17)
        b11.publish("penguins", b17)
except KeyboardInterrupt:
    b11.disconnect()
    b11.loop_stop()