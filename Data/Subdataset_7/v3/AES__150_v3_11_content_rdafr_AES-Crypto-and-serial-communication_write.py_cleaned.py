import serial
import time
import json
from Crypto.Cipher import AES
b1 = 'abcdefghijklmnop'
b2 = AES.new(b1, AES.MODE_ECB)
b3 = '/dev/ttyS0'
a1 = 115200
b4 = serial.Serial(port=b3, baudrate=a1)
b5 = {"oi": "abcdef"}
try:
    while True:
        b6 = json.dumps(b5)
        b7 = b2.encrypt(b6.encode())
        b4.write(b7)
        time.sleep(1)
except KeyboardInterrupt:
    b4.close()
    print("Serial connection closed. Exiting.")
except Exception as e:
    print("An error occurred:", str(e))