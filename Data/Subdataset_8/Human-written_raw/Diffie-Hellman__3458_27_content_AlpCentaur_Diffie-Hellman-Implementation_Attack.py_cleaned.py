import hashlib
import ssl
from binascii import unhexlify, hexlify
import struct as struc
import math
from multiprocessing import Pool
import sys
Prime = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
Generator = 2
A = int(sys.argv[1],16)
B = int(sys.argv[2],16)
def GenerateSharedKey(e , pk_victim):
    sharedsecVictim = '{:x}'.format(pow(pk_victim, e, Prime))
    hashVictim = hashlib.sha512(sharedsecVictim.encode())
    keyVictim = hashVictim.hexdigest()
    return keyVictim
class DiffieHellAttack:
    def __init__(self):
        self.prime = Prime
        self.generator = Generator
    def BirthdayAttack(self, pk_victim1, pk_victim2 , numberCPUs, collisionnumber):
        Iterationnumber = numberCPUs * 2
        def generatesharedkeypk1(x):
            return GenerateSharedKey(x,pk_victim1)
        def generatesharedkeypk2(x):
            return GenerateSharedKey(x,pk_victim2)
        z = True
        comparetable1 = []
        comparetable2 = []
        i = 1
        while z == True:
            i += Iterationnumber
            comparetable1.append(generatesharedkeypk1(i))
            comparetable2.append(generatesharedkeypk2(i+1))
            l = len(comparetable2)
            for n in range(l - 1):
                if comparetable1[n][:collisionnumber] == comparetable2[l-1][:collisionnumber]:
                    out11 = comparetable1[n]
                    out12 = comparetable2[l-1]
                    outnum1 = (n+1) * 2 + 1
                    outnum2 = (l ) * 2 + 2
                    z = False
            for m in range(l - 1):
                if comparetable2[m][:collisionnumber] == comparetable1[l - 1][:collisionnumber]:
                    out21 = comparetable1[l-1]
                    out22 = comparetable2[m]
                    outnum2 = (m+1) * 2  + 2
                    outnum1 = (l ) * 2 + 1
                    z = False
        return outnum1, outnum2
if __name__ == '__main__':
    print( )
    print( )
    print('Starting the Birthday Attack to get the first 7 characters equal..')
    print('If you would like to try more characters with a stronger machine..')
    print('Look in the __main__ function at the end of code and change according to the comment')
    DHA = DiffieHellAttack()
    outnum1, outnum2 = DHA.BirthdayAttack(A, B , 1 , 7)
    print('The private key for the exchange with Alice:', hex(outnum1))
    print('The generated public key for Alice', GenerateSharedKey(outnum1 , A))
    print('The private key for the exchange with Bob:', hex(outnum2))
    print('The generated public key for Bob', GenerateSharedKey(outnum2, B))