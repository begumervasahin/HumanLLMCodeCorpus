from flask import Flask, request
import time
import hashlib
b1 = Flask(b12)
def fonk1(a, b):
    return bytes(x ^ y for x, y in zip(a, b))
def fonk2(b2, message):
    a1 = 64
    if len(b2) > a1:
        b2 = hashlib.sha1(b2.encode()).digest()
    elif len(b2) < a1:
        b2 = b2.encode() + b'\x00' * (a1 - len(b2))
    else:
        b2 = b2.encode()
    b3 = fonk1(b2, b'\x5c' * a1)
    b4 = fonk1(b2, b'\x36' * a1)
    return hashlib.sha1(b3 + hashlib.sha1(b4 + message.encode()).digest()).hexdigest()
def fonk3(b2, message):
    a1 = 64
    if len(b2) > a1:
        b2 = hashlib.sha256(b2.encode()).digest()
    elif len(b2) < a1:
        b2 = b2.encode() + b'\x00' * (a1 - len(b2))
    else:
        b2 = b2.encode()
    b3 = fonk1(b2, b'\x5c' * a1)
    b4 = fonk1(b2, b'\x36' * a1)
    return hashlib.sha256(b3 + hashlib.sha256(b4 + message.encode()).digest()).hexdigest()
def fonk4(b5, b7):
    return b5 = = b7
def fonk5(b5, b7):
    b6 = len(b5)
    b7 = b7 + "\x00" * (len(b5) - len(b7))
    for i in range(b6):
        time.sleep(0.002)
        if b5[i] != b7[i]:
            return 0
    return 1
@b1.route('/get', b8 = ['GET'])
def fonk6():
    b9 = str(request.args.fonk6('b9'))
    return fonk2("myKeyIsL337", b9) + "\n"
@b1.route('/retrieve', b8 = ['GET'])
def fonk7():
    b9 = str(request.args.fonk6('b9'))
    b10 = str(request.args.fonk6('b10'))
    b11 = fonk2("myKeyIsL337", b9)
    if fonk5(b11, b10):
        return "Signature authenticated!\n", 200
    else:
        return "Message was modified, WARNING!\n", 500
if b12 = = "__main__":
    b1.run()