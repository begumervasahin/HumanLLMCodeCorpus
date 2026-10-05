import serial
import time
import json
from Crypto.Cipher import AES
b1 = 'abcdefghijklmnop'
b2 = '/dev/ttyS0'
a1 = 115200
b3 = {"oi": "abcdef"}
b4 = AES.new(b1, AES.MODE_ECB)
b5 = serial.Serial(port=b2, baudrate=a1)
print("Serial port name:", b5.name)
try:
    while True:
        b6 = json.dumps(b3)
        b7 = b4.encrypt(b6.encode())
        b5.write(b7)
        time.sleep(1)
except KeyboardInterrupt:
    b5.close()
    print("Serial connection closed. Exiting.")
except Exception as e:
    print("An error occurred:", str(e))