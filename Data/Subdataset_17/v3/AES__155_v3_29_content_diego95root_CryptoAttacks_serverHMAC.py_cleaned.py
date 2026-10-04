from flask import Flask, request
import time
import hashlib
app = Flask(__name__)
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))
def hmac_sha1(key, message):
    block_size = 64
    if len(key) > block_size:
        key = hashlib.sha1(key.encode()).digest()
    else:
        key = key.encode().ljust(block_size, b'\x00')
    o_key_pad = xor_bytes(key, b'\x5c' * block_size)
    i_key_pad = xor_bytes(key, b'\x36' * block_size)
    inner_hash = hashlib.sha1(i_key_pad + message.encode()).digest()
    return hashlib.sha1(o_key_pad + inner_hash).hexdigest()
def hmac_sha256(key, message):
    block_size = 64
    if len(key) > block_size:
        key = hashlib.sha256(key.encode()).digest()
    else:
        key = key.encode().ljust(block_size, b'\x00')
    o_key_pad = xor_bytes(key, b'\x5c' * block_size)
    i_key_pad = xor_bytes(key, b'\x36' * block_size)
    inner_hash = hashlib.sha256(i_key_pad + message.encode()).digest()
    return hashlib.sha256(o_key_pad + inner_hash).hexdigest()
def secure_compare(s1, s2):
    return s1 == s2
def insecure_compare(s1, s2):
    s2 = s2.ljust(len(s1), "\x00")
    for x, y in zip(s1, s2):
        time.sleep(0.002)
        if x != y:
            return False
    return True
@app.route('/get', methods=['GET'])
def get_hmac():
    file_name = request.args.get('file')
    return hmac_sha1("myKeyIsL337", file_name) + "\n"
@app.route('/retrieve', methods=['GET'])
def check_signature():
    file_name = request.args.get('file')
    signature = request.args.get('signature')
    computed_hmac = hmac_sha1("myKeyIsL337", file_name)
    if insecure_compare(computed_hmac, signature):
        return "Signature authenticated!\n", 200
    else:
        return "Message was modified, WARNING!\n", 500
if __name__ == "__main__":
    app.run()