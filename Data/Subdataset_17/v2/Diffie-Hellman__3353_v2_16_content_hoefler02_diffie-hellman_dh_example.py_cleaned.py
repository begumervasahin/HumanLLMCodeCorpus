from Crypto.Util.number import getStrongPrime
from random import randint
from dh_client import DH_Client
prime_bits = 512
p = getStrongPrime(prime_bits)
g = randint(2, p - 2)
alice = DH_Client('Alice', g, p)
bob = DH_Client('Bob', g, p)
print(f'Secure communication established between {alice.name} and {bob.name}!\n')
print(f'p = {p}\ng = {g}\n')
print(f'{bob.name} -> {alice.name} ~ {bob.public_key}')
alice.establish_shared_secret(bob.public_key)
print(f'{alice.name} -> {bob.name} ~ {alice.public_key}\n')
bob.establish_shared_secret(alice.public_key)
if alice.shared_secret == bob.shared_secret:
    print('Shared secret established!\n')
else:
    print('Error: Shared secrets do not match.\n')
message_from_bob = 'The weather is nice today'
encrypted_message_from_bob = bob.aes_ecb_encrypt(message_from_bob)
print(f'{bob.name} -> {alice.name} ~ {encrypted_message_from_bob}')
message_from_alice = 'It is indeed'
encrypted_message_from_alice = alice.aes_ecb_encrypt(message_from_alice)
print(f'{alice.name} -> {bob.name} ~ {encrypted_message_from_alice}\n')
print('Secure communication ended.')