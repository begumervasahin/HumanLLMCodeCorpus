from Crypto.Util.number import getStrongPrime
from dh_client import DH_Client
from random import randint
def initialize_communication(prime_bits=512):
    p = getStrongPrime(prime_bits)
    g = randint(2, p - 2)
    alice = DH_Client('Alice', g, p)
    bob = DH_Client('Bob', g, p)
    return alice, bob, p, g
def display_initial_parameters(alice, bob, p, g):
    print(f'Secure communication established between {alice.name} and {bob.name}!\n')
    print(f'p = {p}\ng = {g}\n')
    print(f'{bob.name} -> {alice.name} ~ {bob.public_key}')
    print(f'{alice.name} -> {bob.name} ~ {alice.public_key}\n')
def exchange_shared_secrets(alice, bob):
    alice.establish_shared_secret(bob.public_key)
    bob.establish_shared_secret(alice.public_key)
    if alice.shared_secret == bob.shared_secret:
        print('Shared secret established!\n')
    else:
        print('Error: Shared secrets do not match.\n')
def exchange_encrypted_messages(alice, bob):
    message_from_bob = 'The weather is nice today'
    encrypted_message_from_bob = bob.aes_ecb_encrypt(message_from_bob)
    print(f'{bob.name} -> {alice.name} ~ {encrypted_message_from_bob}')
    message_from_alice = 'It is indeed'
    encrypted_message_from_alice = alice.aes_ecb_encrypt(message_from_alice)
    print(f'{alice.name} -> {bob.name} ~ {encrypted_message_from_alice}\n')
def main():
    alice, bob, p, g = initialize_communication()
    display_initial_parameters(alice, bob, p, g)
    exchange_shared_secrets(alice, bob)
    exchange_encrypted_messages(alice, bob)
    print('Secure communication ended.')
if __name__ == "__main__":
    main()