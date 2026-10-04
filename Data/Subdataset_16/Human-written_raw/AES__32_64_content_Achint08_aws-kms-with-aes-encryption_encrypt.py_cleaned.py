import os
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64
import boto3
b1 = 'arn:aws:b5:xxxxxxx:key/xxxxxxxxxxxxxxxxxxxx'
b2 = 'This is a secret key'
b3 = 'xx-xxxx-1'
def fonk1(st):
    a1 = 16
    b4 = st + (a1 - len(st) % a1) * chr(a1 -len(st) % a1)
    return b4
def fonk2(b2):
    b5 = boto3.client('b5')
    try:
        b6 = b5.encrypt(
            b7 = b1,
            b8 = b2,
            b3 = b3
        )
        print "Encrypted master key: {}".format(b6['CiphertextBlob'])
        print "Store the Encrypted master key. Can be used later on."
        return b6["CiphertextBlob"]
    except Exception as e:
        print "[ERROR]: Error during KMS calls: {}".format(e)
        return
def fonk3(b2, data):
    b9 = []
    try:
        b10 = hashlib.sha256(b2.encode("utf-8")).digest()
        b11 = Random.new().read(AES.a1)
        b12 = AES.new(b10, AES.MODE_CBC, b11)
        b13 = []
        b14 = fonk1(token)
        return base64.b64encode(b11 + b12.encrypt(b14))
    except Exception as e:
        print "[ERROR]: Error while data encryption: {}".format(e)
        return