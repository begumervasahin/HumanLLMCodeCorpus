
import serial
import time
import json
from Crypto.Cipher import AES
encryption_key = 'abcdefghijklmnop'
cipher = AES.new(encryption_key, AES.MODE_ECB)
serial_port = '/dev/ttyS0'
baud_rate = 115200
ser = serial.Serial(port=serial_port, baudrate=baud_rate)
json_data = {"oi": "abcdef"}
try:
    while True:
        json_string = json.dumps(json_data)
        encrypted_message = cipher.encrypt(json_string.encode())
        ser.write(encrypted_message)
        time.sleep(1)
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed. Exiting.")
except Exception as e:
    print("An error occurred:", str(e))