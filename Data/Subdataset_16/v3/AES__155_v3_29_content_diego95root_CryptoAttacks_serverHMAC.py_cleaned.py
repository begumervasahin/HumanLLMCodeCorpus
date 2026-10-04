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
    else:
        b2 = b2.encode().ljust(a1, b'\x00')
    b3 = fonk1(b2, b'\x5c' * a1)
    b4 = fonk1(b2, b'\x36' * a1)
    b5 = hashlib.sha1(b4 + message.encode()).digest()
    return hashlib.sha1(b3 + b5).hexdigest()
def fonk3(b2, message):
    a1 = 64
    if len(b2) > a1:
        b2 = hashlib.sha256(b2.encode()).digest()
    else:
        b2 = b2.encode().ljust(a1, b'\x00')
    b3 = fonk1(b2, b'\x5c' * a1)
    b4 = fonk1(b2, b'\x36' * a1)
    b5 = hashlib.sha256(b4 + message.encode()).digest()
    return hashlib.sha256(b3 + b5).hexdigest()
def fonk4(b6, b7):
    return b6 = = b7
def fonk5(b6, b7):
    b7 = b7.ljust(len(b6), "\x00")
    for x, y in zip(b6, b7):
        time.sleep(0.002)
        if x != y:
            return False
    return True
@b1.route('/get', b8 = ['GET'])
def fonk6():
    b9 = request.args.get('file')
    return fonk2("myKeyIsL337", b9) + "\n"
@b1.route('/retrieve', b8 = ['GET'])
def fonk7():
    b9 = request.args.get('file')
    b10 = request.args.get('b10')
    b11 = fonk2("myKeyIsL337", b9)
    if fonk5(b11, b10):
        return "Signature authenticated!\n", 200
    else:
        return "Message was modified, WARNING!\n", 500
if b12 = = "__main__":
    b1.run()