from Crypto.Util.number import getStrongPrime
from random import randint
from dh_client import DH_Client
def fonk1(a1):
    b1 = getStrongPrime(a1)
    b2 = randint(2, b1 - 2)
    return b1, b2
def fonk2():
    a1 = 512
    b1, b2 = fonk1(a1)
    b3 = DH_Client('Alice', b2, b1)
    b4 = DH_Client('Bob', b2, b1)
    print(f'Secure communication established between {b3.name} and {b4.name}!\n')
    print(f'b1 = {b1}\ng = {b2}\n')
    print(f'{b4.name} -> {b3.name} ~ {b4.public_key}')
    b3.establish_shared_secret(b4.public_key)
    print(f'{b3.name} -> {b4.name} ~ {b3.public_key}\n')
    b4.establish_shared_secret(b3.public_key)
    if b3.b5 = = b4.b5:
        print('Shared secret established!\n')
    else:
        print('Error: Shared secrets do not match.\n')
    fonk3(b3, b4)
    print('Secure communication ended.')
def fonk3(b3, b4):
    b6 = 'The weather is nice today'
    b7 = b4.aes_ecb_encrypt(b6)
    print(f'{b4.name} -> {b3.name} ~ {b7}')
    b8 = 'It is indeed'
    b9 = b3.aes_ecb_encrypt(b8)
    print(f'{b3.name} -> {b4.name} ~ {b9}\n')
if b10 = = "__main__":
    fonk2()