from Crypto.Util.number import getStrongPrime
from random import randint
from faker import Faker
from dh_client import DH_Client
b1 = getStrongPrime(512)
b2 = randint(2, b1 - 2)
b3 = DH_Client('Alice', b2, b1)
b4 = DH_Client('Bob', b2, b1)
print(f'Secure communication established between {b3.name} and {b4.name}!\n')
print(f'b1 = {b1}\ng = {b2}\n')
print(f'{b4.name} -> {b3.name} ~ {b4.public_key}')
b3.establish_shared_secret(b4.public_key)
print(f'{b3.name} -> {b4.name} ~ {b3.public_key}\n')
b4.establish_shared_secret(b3.public_key)
print('Shared secret established!\n')
b5 = 'the weather is nice today'
b6 = b4.aes_ecb_encrypt(b5)
print(f'{b4.name} -> {b3.name} ~ {b6}')
b7 = 'it is indeed'
b8 = b3.aes_ecb_encrypt(b7)
print(f'{b3.name} -> {b4.name} ~ {b8}\n')
print('Secure communication ended.')