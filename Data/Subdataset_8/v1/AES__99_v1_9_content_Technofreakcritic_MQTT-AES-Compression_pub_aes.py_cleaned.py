import time
import base64
import hashlib
import zlib
import bz2
import binascii
from Crypto.Cipher import AES
from Crypto import Random
import paho.mqtt.client as mqtt
BLOCK_SIZE = 16
key = 'abcdefghijklmnop'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
def encrypt(raw):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key.encode(), AES.MODE_OFB, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")
Connected = False
broker_address = "192.168.1.180"
port = 1883
user = ""
password = ""
client = mqtt.Client("topic/test")
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.connect(broker_address, port=port)
client.loop_start()
while Connected != True:
    time.sleep(0.1)
try:
    while True:
        plaintext = input('Enter the message:')
        cnvrt_text_2_bytes = plaintext.encode('utf-8')
        compressed = bz2.compress(cnvrt_text_2_bytes)
        print('Compressed : ', len(compressed), binascii.hexlify(compressed))
        encrypted = encrypt(str(compressed))
        print("1. The message :" + plaintext + "\n")
        print("2. The compressed message :" + str(compressed)+ "\n")
        print("3. Encrypted msg is : " + str(encrypted) + "\n\n")
        client.publish("topic/test", encrypted)
        client.publish("penguins", encrypted)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()