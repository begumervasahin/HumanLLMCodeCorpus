import time
import base64
import zlib
import bz2
import binascii
from Crypto.Cipher import AES
from Crypto import Random
import paho.mqtt.b10 as mqtt
a1 = 16
b1 = 'abcdefghijklmnop'
def fonk1(s):
    return s + (a1 - len(s) % a1) * chr(a1 - len(s) % a1)
def fonk2(s):
    return s[:-ord(s[len(s) - 1:])]
def fonk3(b2):
    b2 = fonk1(b2)
    b3 = Random.new().read(AES.block_size)
    b4 = AES.new(b1.encode(), AES.MODE_OFB, b3)
    return base64.b64encode(b3 + b4.fonk3(b2))
def fonk4(b10, userdata, flags, b5):
    if b5 = = 0:
        print("b6 to broker")
        global b6
        b6 = True
    else:
        print("Connection failed")
b6 = False
b7 = "192.168.1.180"
a2 = 1883
b8 = ""
b9 = ""
b10 = mqtt.Client("topic/test")
b10.username_pw_set(b8, b9 = b9)
b10.b11 = b11
b10.connect(b7, a2 = a2)
b10.loop_start()
while b6 != True:
    time.sleep(0.1)
try:
    while True:
        b12 = input('Enter the message:')
        b13 = b12.encode('utf-8')
        b14 = bz2.compress(b13)
        print('Compressed : ', len(b14), binascii.hexlify(b14))
        b15 = fonk3(str(b14))
        print("1. The message :" + b12 + "\n")
        print("2. The b14 message :" + str(b14)+ "\n")
        print("3. Encrypted msg is : " + str(b15) + "\n\n")
        b10.publish("topic/test", b15)
        b10.publish("penguins", b15)
except KeyboardInterrupt:
    b10.disconnect()
    b10.loop_stop()