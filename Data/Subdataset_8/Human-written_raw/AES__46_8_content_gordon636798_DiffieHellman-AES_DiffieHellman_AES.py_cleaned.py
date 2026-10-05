
import random
from gmpy2 import *
from Crypto.Cipher import AES
import hashlib
a=mpz(11)
q=mpz(1040699159)
print('a :',a,', q :',q)
data = 'I love ncyucsie åå»~~(â§êªâ¦)'
print('Plain :'+data+'\n')
class user:
    def __init__(self,name,a,q):
        self.name = name
        self.a = a
        self.q = q
        temp = sum([ord(i) for i in name])
        self.__X = mpz_random(random_state(temp),q)
        self.Y = powmod(self.a,self.__X,self.q)
        self.__key = {}
        print(self.name+'\'s master key :',self.__X)
    def commonKey(self, _user, Yb):
        key = powmod(Yb,self.__X,self.q)
        key = int(key).to_bytes(len(key)
        key = hashlib.sha256(key)
        key = key.digest()
        print('\nCommon key for '+ self.name+' and ' + _user.name +': \n'+ key.hex())
        self.__key[_user.name] = key
    def AES_encrypt(self, _user, data):
        data = data.encode('utf-8')
        padding = 16 - len(data) % 16
        if padding == 0 :
            padding = 16
        P = bytes([padding])
        data += padding*(P)
        cryptor = AES.new(self.__key[_user.name],AES.MODE_CBC , 16*'\x00')
        cip = cryptor.encrypt(data)
        print('\ncipher : \n'+ cip.hex())
        return [cip , self.name]
    def AES_decrypt(self, cip):
        data,name = cip[0],cip[1]
        cryptor = AES.new(self.__key[name], AES.MODE_CBC,16*'\x00')
        plain = cryptor.decrypt(data)
        plain = plain[:(len(plain)-plain[-1])]
        plain = plain.decode('utf-8')
        print('\nplain from ' +name+' : \n'+ plain)
        return plain
Alice = user('Alice', a , q)
Bob = user('Bob', a , q)
Alice.commonKey(Bob,Bob.Y)
Bob.commonKey(Alice,Alice.Y)
cip = Alice.AES_encrypt(Bob,data)
plain = Bob.AES_decrypt(cip)