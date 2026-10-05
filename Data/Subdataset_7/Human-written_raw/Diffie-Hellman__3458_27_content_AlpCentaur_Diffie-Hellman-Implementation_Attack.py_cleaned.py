import hashlib
import ssl
from binascii import unhexlify, hexlify
import struct as struc
import math
from multiprocessing import Pool
import sys
b1 = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
a1 = 2
b2 = int(sys.argv[1],16)
b3 = int(sys.argv[2],16)
def fonk1(e , pk_victim):
    b4 = '{:x}'.format(pow(pk_victim, e, b1))
    b5 = hashlib.sha512(b4.encode())
    b6 = b5.hexdigest()
    return b6
class class1:
    def fonk2(self):
        self.b7 = b1
        self.b8 = a1
    def fonk3(self, pk_victim1, pk_victim2 , numberCPUs, collisionnumber):
        b9 = numberCPUs * 2
        def fonk4(x):
            return fonk1(x,pk_victim1)
        def fonk5(x):
            return fonk1(x,pk_victim2)
        b10 = True
        b11 = []
        b12 = []
        a2 = 1
        while b10 = = True:
            a2 += b9
            b11.append(fonk4(a2))
            b12.append(fonk5(a2+1))
            b13 = len(b12)
            for n in range(b13 - 1):
                if b11[n][:collisionnumber] == b12[b13-1][:collisionnumber]:
                    b14 = b11[n]
                    b15 = b12[b13-1]
                    b16 = (n+1) * 2 + 1
                    b17 = (b13 ) * 2 + 2
                    b10 = False
            for m in range(b13 - 1):
                if b12[m][:collisionnumber] == b11[b13 - 1][:collisionnumber]:
                    b18 = b11[b13-1]
                    b19 = b12[m]
                    b17 = (m+1) * 2  + 2
                    b16 = (b13 ) * 2 + 1
                    b10 = False
        return b16, b17
if b20 = = '__main__':
    print( )
    print( )
    print('Starting the Birthday Attack to get the first 7 characters equal..')
    print('If you would like to try more characters with a stronger machine..')
    print('Look in the __main__ function at the end of code and change according to the comment')
    b21 = class1()
    b16, b17 = b21.fonk3(b2, b3 , 1 , 7)
    print('The private key for the exchange with Alice:', hex(b16))
    print('The generated public key for Alice', fonk1(b16 , b2))
    print('The private key for the exchange with Bob:', hex(b17))
    print('The generated public key for Bob', fonk1(b17, b3))