import time
import base64
import binascii
import bz2
import zlib
from Crypto.Cipher import AES
from Crypto import Random
import paho.mqtt.client as mqtt
import key_gen as kg
BLOCK_SIZE = 16
KEY = 'abcdefghijklmnop'
Connected = False
BROKER_ADDRESS = "192.168.1.180"
PORT = 1883
USER = ""
PASSWORD = ""
CLIENT_ID = "topic/test"
def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
def unpad(s):
    return s[:-ord(s[len(s) - 1:])]
def encrypt(raw):
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(KEY.encode(), AES.MODE_OFB, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")
client = mqtt.Client(CLIENT_ID)
client.username_pw_set(USER, password=PASSWORD)
client.on_connect = on_connect
client.connect(BROKER_ADDRESS, port=PORT)
client.loop_start()
while not Connected:
    time.sleep(0.1)
try:
    while True:
        plaintext = input('Enter the message:')
        compressed = bz2.compress(plaintext.encode('utf-8'))
        print('Compressed: ', len(compressed), binascii.hexlify(compressed))
        encrypted = encrypt(str(compressed))
        print("1. The message: " + plaintext + "\n")
        print("2. The compressed message: " + str(compressed)+ "\n")
        print("3. Encrypted message: " + str(encrypted) + "\n\n")
        client.publish("topic/test", encrypted)
        client.publish("penguins", encrypted)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()