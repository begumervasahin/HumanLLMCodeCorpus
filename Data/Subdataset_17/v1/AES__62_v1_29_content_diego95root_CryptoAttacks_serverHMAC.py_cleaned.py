from flask import Flask, request
import time
import hashlib
app = Flask(__name__)
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))
def HMAC_sha1(key, message):
    blockSize = 64
    if len(key) > blockSize:
        key = hashlib.sha1(key.encode()).digest()
    elif len(key) < blockSize:
        key = key.encode() + b'\x00' * (blockSize - len(key))
    else:
        key = key.encode()
    o_key_pad = xor(key, b'\x5c' * blockSize)
    i_key_pad = xor(key, b'\x36' * blockSize)
    return hashlib.sha1(o_key_pad + hashlib.sha1(i_key_pad + message.encode()).digest()).hexdigest()
def HMAC_sha256(key, message):
    blockSize = 64
    if len(key) > blockSize:
        key = hashlib.sha256(key.encode()).digest()
    elif len(key) < blockSize:
        key = key.encode() + b'\x00' * (blockSize - len(key))
    else:
        key = key.encode()
    o_key_pad = xor(key, b'\x5c' * blockSize)
    i_key_pad = xor(key, b'\x36' * blockSize)
    return hashlib.sha256(o_key_pad + hashlib.sha256(i_key_pad + message.encode()).digest()).hexdigest()
def compare_good(s1, s2):
    return s1 == s2
def compare_bad(s1, s2):
    length = len(s1)
    s2 = s2 + "\x00" * (len(s1) - len(s2))
    for i in range(length):
        time.sleep(0.002)
        if s1[i] != s2[i]:
            return 0
    return 1
@app.route('/get', methods=['GET'])
def get():
    file = str(request.args.get('file'))
    return HMAC_sha1("myKeyIsL337", file) + "\n"
@app.route('/retrieve', methods=['GET'])
def check():
    file = str(request.args.get('file'))
    signature = str(request.args.get('signature'))
    hmac_good = HMAC_sha1("myKeyIsL337", file)
    if compare_bad(hmac_good, signature):
        return "Signature authenticated!\n", 200
    else:
        return "Message was modified, WARNING!\n", 500
if __name__ == "__main__":
    app.run()