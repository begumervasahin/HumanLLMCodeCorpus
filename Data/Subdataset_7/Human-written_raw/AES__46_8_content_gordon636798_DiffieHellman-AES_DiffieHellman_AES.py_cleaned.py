
import random
from gmpy2 import *
from Crypto.Cipher import AES
import hashlib
b1 = mpz(11)
b2 = mpz(1040699159)
print('b1 :',b1,', b2 :',b2)
b3 = 'I love ncyucsie åå»~~(â§êªâ¦)'
print('Plain :'+b3+'\n')
class class1:
    def fonk1(self,b4,b1,b2):
        self.b4 = b4
        self.b1 = b1
        self.b2 = b2
        b5 = sum([ord(i) for i in b4])
        self.b6 = mpz_random(random_state(b5),b2)
        self.b7 = powmod(self.b1,self.b6,self.b2)
        self.b8 = {}
        print(self.b4+'\'s master b9 :',self.b6)
    def fonk2(self, _user, Yb):
        b9 = powmod(Yb,self.b6,self.b2)
        b9 = int(b9).to_bytes(len(b9)
        b9 = hashlib.sha256(b9)
        b9 = b9.digest()
        print('\nCommon b9 for '+ self.b4+' and ' + _user.b4 +': \n'+ b9.hex())
        self.b8[_user.b4] = b9
    def fonk3(self, _user, b3):
        b3 = b3.encode('utf-8')
        b10 = 16 - len(b3) % 16
        if b10 = = 0 :
            b10 = 16
        b11 = bytes([b10])
        b3 += b10*(b11)
        b12 = AES.new(self.b8[_user.b4],AES.MODE_CBC , 16*'\x00')
        b13 = b12.encrypt(b3)
        print('\ncipher : \n'+ b13.hex())
        return [b13 , self.b4]
    def fonk4(self, b13):
        b3,b4 = b13[0],b13[1]
        b12 = AES.new(self.b8[b4], AES.MODE_CBC,16*'\x00')
        b14 = b12.decrypt(b3)
        b14 = b14[:(len(b14)-b14[-1])]
        b14 = b14.decode('utf-8')
        print('\nplain from ' +b4+' : \n'+ b14)
        return b14
b15 = class1('b15', b1 , b2)
b16 = class1('b16', b1 , b2)
b15.fonk2(b16,b16.b7)
b16.fonk2(b15,b15.b7)
b13 = b15.fonk3(b16,b3)
b14 = b16.fonk4(b13)