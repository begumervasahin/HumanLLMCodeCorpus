import serial
import time
import json
from Crypto.Cipher import AES
key = 'abcdefghijklmnop'
cipher = AES.new(key, AES.MODE_ECB)
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=115200
)
j = {"oi": "abcdef"}
while True:
    try:
        msg = json.dumps(j)
        cm = cipher.encrypt(msg.encode())
        ser.write(cm)
        time.sleep(1)
    except KeyboardInterrupt:
        ser.close()
        print("Serial connection closed. Exiting.")
        break
    except Exception as e:
        print("An error occurred:", str(e))