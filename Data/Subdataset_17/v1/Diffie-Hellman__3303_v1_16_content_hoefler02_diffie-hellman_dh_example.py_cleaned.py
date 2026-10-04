from Crypto.Util.number import getStrongPrime
from random import randint
from faker import Faker
from dh_client import DH_Client
p = getStrongPrime(512)
g = randint(2, p - 2)
a = DH_Client('Alice', g, p)
b = DH_Client('Bob', g, p)
print(f'Secure communication established between {a.name} and {b.name}!\n')
print(f'p = {p}\ng = {g}\n')
print(f'{b.name} -> {a.name} ~ {b.public_key}')
a.establish_shared_secret(b.public_key)
print(f'{a.name} -> {b.name} ~ {a.public_key}\n')
b.establish_shared_secret(a.public_key)
print('Shared secret established!\n')
msg_two = 'the weather is nice today'
encrypted_msg_two = b.aes_ecb_encrypt(msg_two)
print(f'{b.name} -> {a.name} ~ {encrypted_msg_two}')
msg_one = 'it is indeed'
encrypted_msg_one = a.aes_ecb_encrypt(msg_one)
print(f'{a.name} -> {b.name} ~ {encrypted_msg_one}\n')
print('Secure communication ended.')