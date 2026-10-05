import serial
import time
import json
from Crypto.Cipher import AES
AES_KEY = 'abcdefghijklmnop'
SERIAL_PORT = '/dev/ttyS0'
BAUD_RATE = 115200
JSON_DATA = {"oi": "abcdef"}
aes_cipher = AES.new(AES_KEY, AES.MODE_ECB)
serial_connection = serial.Serial(port=SERIAL_PORT, baudrate=BAUD_RATE)
print("Serial port name:", serial_connection.name)
try:
    while True:
        json_string = json.dumps(JSON_DATA)
        encrypted_message = aes_cipher.encrypt(json_string.encode())
        serial_connection.write(encrypted_message)
        time.sleep(1)
except KeyboardInterrupt:
    serial_connection.close()
    print("Serial connection closed. Exiting.")
except Exception as e:
    print("An error occurred:", str(e))