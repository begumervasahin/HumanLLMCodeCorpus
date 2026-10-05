from flask import Flask, request
from xor import xor
from SHA1 import sha1
from hashlib import sha256
from time import sleep
b1 = Flask(b14)
def fonk1(b2, message):
    a1 = 64
    a2 = 20
    if len(b2) > a1:
        b2 = sha1(b2.encode()).digest()
    elif len(b2) < a1:
        b2 += b'\x00' * (a1 - len(b2))
    b3 = xor(b2.hex(), ("5c" * a1)).decode("hex")
    b4 = xor(b2.hex(), ("36" * a1)).decode("hex")
    b5 = sha1(b4 + sha1(b4 + message.encode()).digest()).digest()
    b6 = sha1(b3 + b5).hexdigest()
    return b6[:a2 * 2]
def fonk2(b2, message):
    a1 = 64
    a2 = 32
    if len(b2) > a1:
        b2 = sha256(b2.encode()).hexdigest()
    elif len(b2) < a1:
        b2 += b'\x00' * (a1 - len(b2))
    b3 = xor(bytes.fromhex(b2), (b"\x5c" * a1))
    b4 = xor(bytes.fromhex(b2), (b"\x36" * a1))
    b5 = sha256(b4 + sha256(b4 + message.encode()).hexdigest().encode()).digest()
    b6 = sha256(b3 + b5).hexdigest()
    return b6[:a2 * 2]
def fonk3(b7, b9):
    return b7 = = b9
def fonk4(b7, b9):
    b8 = len(b7)
    b9 = b9 + "\x00" * (len(b7) - len(b9))
    for i in range(b8):
        sleep(0.002)
        if b7[i] != b9[i]:
            return False
    return True
@b1.route('/get', b10 = ['GET'])
def fonk5():
    b11 = str(request.args.fonk5('b11'))
    return fonk1("myKeyIsL337", b11) + "\n"
@b1.route('/retrieve', b10 = ['GET'])
def fonk6():
    b11 = str(request.args.fonk5('b11'))
    b12 = str(request.args.fonk5('b12'))
    b13 = fonk1("myKeyIsL337", b11)
    if fonk4(b13, b12):
        return "Signature authenticated!\n", 200
    else:
        return "Message was modified, WARNING!\n", 500
if b14 = = "__main__":
    b1.run()