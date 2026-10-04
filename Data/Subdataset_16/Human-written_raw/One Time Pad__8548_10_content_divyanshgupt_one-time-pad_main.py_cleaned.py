import sys
from takeinput import takeinput
import crypt
b1 = sys.argv
b3,directory,b2 = takeinput(b1)
if b3 = ="encrypt":
    try:
        crypt.encrypt(directory,b2)
        print("Encrypted")
    except:
        print("error during encryption")
elif b3 = ="decrypt":
    try:
        crypt.decrypt(directory,b2)
        print("Decrypted")
    except:
        print('error during decryption')
else:
    print("error: can't understand input")