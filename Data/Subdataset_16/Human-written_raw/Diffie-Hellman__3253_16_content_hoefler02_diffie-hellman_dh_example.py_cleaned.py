from Crypto.Util.number import getStrongPrime, getPrime
from dh_client import DH_Client
from random import randint
from faker import Faker
b1 = getStrongPrime(512)
b2 = randint(2, b1 - 2)
b3 = DH_Client('Alice', b2, b1)
b4 = DH_Client('Bob', b2, b1)
print('Secure communication established between %s and %s!\n' % (b3.name, b4.name))
print('b1 = %d\ng = %d\n' % (b1, b2))
print('%s -> %s ~ %d' % (b4.name, b3.name, b4.public_key))
b3.establish_shared_secret(b4.public_key)
print('%s -> %s ~ %d\n' % (b3.name, b4.name, b3.public_key))
b4.establish_shared_secret(b3.public_key)
print('Shared secret established!\n')
b5 = 'the weathers nice today'
print('%s -> %s ~ %d' % (b4.name, b3.name, b4.aes_ecb_encrypt(b5)))
b6 = 'it is indeed'
print('%s -> %s ~ %d\n' % (b3.name, b4.name, b3.aes_ecb_encrypt(b6)))
print('Secure communication ended.')