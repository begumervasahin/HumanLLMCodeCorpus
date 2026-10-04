from Crypto.Util.number import getStrongPrime
from random import randint
from dh_client import DH_Client
def fonk1(b1 = 512):
    b2 = getStrongPrime(b1)
    b3 = randint(2, b2 - 2)
    return b2, b3
def fonk2(b2, b3):
    b4 = DH_Client('Alice', b3, b2)
    b5 = DH_Client('Bob', b3, b2)
    return b4, b5
def fonk3(b4, b5, b2, b3):
    print(f'Secure communication established between {b4.name} and {b5.name}!\n')
    print(f'Prime (p) = {b2}\nBase (g) = {b3}\n')
    print(f'{b5.name} -> {b4.name} ~ Public Key: {b5.public_key}')
    print(f'{b4.name} -> {b5.name} ~ Public Key: {b4.public_key}\n')
def fonk4(b4, b5):
    b4.establish_shared_secret(b5.public_key)
    b5.establish_shared_secret(b4.public_key)
    if b4.b6 = = b5.b6:
        print('Shared secret established!\n')
    else:
        print('Error: Shared secrets do not match.\n')
def fonk5(b4, b5):
    b7 = 'The weather is nice today'
    b8 = b5.aes_ecb_encrypt(b7)
    print(f'{b5.name} -> {b4.name} ~ Encrypted Message: {b8}')
    b9 = 'It is indeed'
    b10 = b4.aes_ecb_encrypt(b9)
    print(f'{b4.name} -> {b5.name} ~ Encrypted Message: {b10}\n')
def fonk6():
    b2, b3 = fonk1()
    b4, b5 = fonk2(b2, b3)
    fonk3(b4, b5, b2, b3)
    fonk4(b4, b5)
    fonk5(b4, b5)
    print('Secure communication ended.')
if b11 = = "__main__":
    fonk6()