from flask import Flask, request
from xor import *
from SHA1 import *
from time import sleep
from hashlib import sha256
b1 = Flask(b12)
def fonk1(b2, message):
    a1 = 64
    a2 = 20
    if len(b2) > a1:
        b2 = sha1(b2)
    elif len(b2) < a1:
        b2 += b'\x00' * (a1 - len(b2))
    b3 = xor(b2.encode("hex"), ("5c" * a1)).decode("hex")
    b4 = xor(b2.encode("hex"), ("36" * a1)).decode("hex")
    return sha1(b3 + sha1(b4 + message).decode("hex"))[:a2*2]
def fonk2(b2, message):
    a1 = 64
    a2 = 32
    if len(b2) > a1:
        b2 = sha256(b2).hexdigest()
    elif len(b2) < a1:
        b2 += b'\x00' * (a1 - len(b2))
    b3 = xor(b2.encode("hex"), ("5c" * a1)).decode("hex")
    b4 = xor(b2.encode("hex"), ("36" * a1)).decode("hex")
    return sha256(b3 + sha256(b4 + message).hexdigest().decode("hex")).hexdigest()[:a2*2]
def fonk3(b5, b7):
    return b5 = = b7
def fonk4(b5, b7):
    b6 = len(b5)
    b7 = b7 + "\x00" * (len(b5) - len(b7))
    for i in range(b6):
        sleep(0.002)
        if b5[i] != b7[i]:
            return 0
    return 1
@b1.route('/get', b8 = ['GET'])
def fonk5():
    b9 = str(request.args.fonk5('b9'))
    return fonk1("myKeyIsL337", b9) + "\n"
@b1.route('/retrieve', b8 = ['GET'])
def fonk6():
    b9 = str(request.args.fonk5('b9'))
    b10 = str(request.args.fonk5('b10'))
    b11 = fonk1("myKeyIsL337", b9)
    if fonk4(b11, b10):
        return "Signature authenticated!\n", 200
    else:
        return "Message was modified, WARNING!\n", 500
if b12 = = "__main__":
    b1.run()