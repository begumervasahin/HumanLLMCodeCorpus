import sys
import getopt
import os
from Crypto.Hash import SHA256, MD5, SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
blockSize = 1024*1024
def very_sign(hash, input_file, sign_file, file_publickey):
    print "Hash mode:", hash
    if hash != "SHA256" and hash != "MD5" and hash != "SHA" and hash != "SHA1" and hash != "SHA-1":
        print "Available modes: SHA256, MD5, SHA."
        print "Choose again!"
        sys.exit()
    if(hash == "SHA256"):
        hash = SHA256
    elif (hash == "MD5"):
        hash = MD5
    elif (hash == "SHA" or hash == "SHA1" or hash == "SHA-1"):
        hash = SHA
    myHash = hash.new()
    with open(input_file, "rb") as fin:
        while True:
            block = fin.read(blockSize)
            if len(block) == 0:
                break
            myHash.update(block)
    hash = myHash
    with open(sign_file, "rb") as fin2:
        signature = fin2.read()
    print "Signature get:", signature
    if os.path.isfile(file_publickey):
        with open(file_publickey, "r") as fin3:
            public_key = RSA.importKey(fin3.read())
    else:
        print "Public key doesn't exist... Task failed.....!!"
        return False
    check = PKCS1_v1_5.new(public_key)
    result = check.verify(hash, signature)
    print "Verify check:", result
    return result
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h:")
    except getopt.GetoptError:
        print "very_sign.py -h <hash> <file_input> <ten_file_chua_chu_ky> <file_publickey>"
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            hash = arg.upper()
    if(len(args) != 3):
        print "very_sign.py -h <hash> <fileinput> <file_signed> <file_publickey>"
        sys.exit(2)
    input_file = args[0]
    file_signed = args[1]
    file_publickey = args[2]
    flag = very_sign(hash, input_file, file_signed, file_publickey)
    print "Verify result:", flag
    return flag
if __name__ == "__main__":
    main(sys.argv[1:])