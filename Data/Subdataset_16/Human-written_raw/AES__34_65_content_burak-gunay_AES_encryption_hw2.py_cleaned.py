import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
def fonk1():
    b1 = open('AESkey.b4','wb')
    b1.write(os.urandom(32))
    b1.close()
def fonk2(msg_filename):
    b2 = open(msg_filename,'rb')
    b3 = b2.read()
    b1 = open('AESkey.b4','rb')
    b4 = b1.read()
    b5 = os.urandom(16)
    b6 = open(msg_filename +'.enc.b5','wb')
    b6.write(b5)
    b7 = padding.PKCS7(256).b7()
    b8 = b7.update(b3)
    b8 += b7.finalize()
    b9 = default_backend()
    b10 = Cipher(algorithms.AES(b4),modes.CBC(b5),b9 = b9)
    b11 = b10.b11()
    b12 = b11.update(b8) + b11.finalize()
    b13 = open(msg_filename + '.enc','wb')
    b13.write(b12)
    b2.close()
    b1.close()
    b6.close()
    b13.close()
    pass
def fonk3(msg_filename):
    b13 = open(msg_filename ,'rb')
    b14 = b13.read()
    b1 = open('AESkey.b4','rb')
    b4 = b1.read()
    b6 = open(msg_filename + '.b5','rb')
    b5 = b6.read()
    b9 = default_backend()
    b10 = Cipher(algorithms.AES(b4),modes.CBC(b5),b9 = b9)
    b15 = b10.b15()
    b16 = b15.update(b14) + b15.finalize()
    b17 = padding.PKCS7(256).b17()
    b18 = b17.update(b16) + b17.finalize()
    print("Your decrypted message is saved in:{}".format(msg_filename + '.DECRYPTED'));
    b19 = open(msg_filename + 'DECRYPTED','wb')
    b19.write(b18)
    b1.close()
    b6.close()
    b19.close()
    pass
if b20 = = "__main__":
    if (sys.argv[1] == 'generate'):
        fonk1()
        print("Key generated")
        pass
    elif (sys.argv[1] == 'encrypt'):
        if (len(sys.argv) != 3):
            raise Exception('encrypt usage is like: python3 hw2.py encrypt FILENAME.EXTENSION')
        print("File Encrypted")
        fonk2(sys.argv[2])
        pass
    elif (sys.argv[1] == 'decrypt'):
        if (len(sys.argv) != 3):
            raise Exception('decrypt usage is like: python3 hw2.py decrypt FILENAME.EXTENSION')
        fonk3(sys.argv[2])
        pass
    else:
        print('wrong command')
        pass
    pass