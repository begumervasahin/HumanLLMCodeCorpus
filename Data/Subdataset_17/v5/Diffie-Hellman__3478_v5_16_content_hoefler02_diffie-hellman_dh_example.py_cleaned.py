from Crypto.Util.number import getStrongPrime
from random import randint
from dh_client import DH_Client
def generate_parameters(prime_bits=512):
    prime = getStrongPrime(prime_bits)
    base = randint(2, prime - 2)
    return prime, base
def initialize_clients(prime, base):
    alice = DH_Client('Alice', base, prime)
    bob = DH_Client('Bob', base, prime)
    return alice, bob
def display_parameters(alice, bob, prime, base):
    print(f'Secure communication established between {alice.name} and {bob.name}!\n')
    print(f'Prime (p) = {prime}\nBase (g) = {base}\n')
    print(f'{bob.name} -> {alice.name} ~ Public Key: {bob.public_key}')
    print(f'{alice.name} -> {bob.name} ~ Public Key: {alice.public_key}\n')
def establish_shared_secrets(alice, bob):
    alice.establish_shared_secret(bob.public_key)
    bob.establish_shared_secret(alice.public_key)
    if alice.shared_secret == bob.shared_secret:
        print('Shared secret established!\n')
    else:
        print('Error: Shared secrets do not match.\n')
def exchange_messages(alice, bob):
    message_from_bob = 'The weather is nice today'
    encrypted_message_from_bob = bob.aes_ecb_encrypt(message_from_bob)
    print(f'{bob.name} -> {alice.name} ~ Encrypted Message: {encrypted_message_from_bob}')
    message_from_alice = 'It is indeed'
    encrypted_message_from_alice = alice.aes_ecb_encrypt(message_from_alice)
    print(f'{alice.name} -> {bob.name} ~ Encrypted Message: {encrypted_message_from_alice}\n')
def main():
    prime, base = generate_parameters()
    alice, bob = initialize_clients(prime, base)
    display_parameters(alice, bob, prime, base)
    establish_shared_secrets(alice, bob)
    exchange_messages(alice, bob)
    print('Secure communication ended.')
if __name__ == "__main__":
    main()