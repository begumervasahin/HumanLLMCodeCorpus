
import serial
import time
import json
from Crypto.Cipher import AES
encryption_key = 'abcdefghijklmnop'
cipher = AES.new(encryption_key, AES.MODE_ECB)
serial_port = '/dev/ttyS0'
baud_rate = 115200
serial_connection = serial.Serial(port=serial_port, baudrate=baud_rate)
json_data = {"oi": "abcdef"}
print("Serial port name:", serial_connection.name)
while True:
    try:
        json_string = json.dumps(json_data)
        encrypted_message = cipher.encrypt(json_string.encode())
        serial_connection.write(encrypted_message)
        time.sleep(1)
    except KeyboardInterrupt:
        serial_connection.close()
        print("Serial connection closed. Exiting.")
        break
    except Exception as e:
        print("An error occurred:", str(e))