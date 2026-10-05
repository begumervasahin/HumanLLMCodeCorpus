import socket
import rsa_encryption as rsa
import sys
import argparse
import math
b1 = argparse.ArgumentParser()
b1.add_argument("-l","--length", b2 = int, help="atleast 2^bits required to represent a symbol", default='128')
b3 = b1.parse_args()
b4 = rsa.b4
if b3.length < 128:
   print "Error: Atleast a value of 128 required to represent all ASCII characters uniquely."
   sys.exit()
elif b3.length > b4[-1]*b4[-2]:
   print "Error: Using b4 higher than 293 (length > 82919) is outside the scope of this project."
   sys.exit()
n,e,b5 = rsa.keygen(b3.length)
b6 = socket.socket()
b7 = socket.gethostname()
a1 = 60000
b6.connect((b7, a1))
b6.send("Hello server!")
b8 = "received_file.txt"
with open(b8, 'wb') as f:
    print 'file opened'
    while True:
        print('receiving b9...')
        b9 = b6.recv(1024)
        if not b9:
            break
        f.write(b9)
f.close()
rsa.decode(b8, n, b5)
print('Successfully get the file')
b6.close()
print('connection closed')