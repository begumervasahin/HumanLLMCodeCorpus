from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import Seed_Generator
def generate_diffie_hellman_parameters():
    return dh.generate_parameters(generator=5, key_size=1024, backend=default_backend())
def generate_private_and_public_keys(parameters):
    alice_private_key = parameters.generate_private_key()
    bob_private_key = parameters.generate_private_key()
    return (
        alice_private_key,
        alice_private_key.public_key(),
        bob_private_key,
        bob_private_key.public_key()
    )
def exchange_keys_and_compute_shared_key(alice_private_key, alice_public_key, bob_private_key, bob_public_key):
    alice_shared_key = alice_private_key.exchange(bob_public_key)
    bob_shared_key = bob_private_key.exchange(alice_public_key)
    return alice_shared_key if alice_shared_key == bob_shared_key else False
def generate_access_key():
    parameters = generate_diffie_hellman_parameters()
    alice_private_key, alice_public_key, bob_private_key, bob_public_key = generate_private_and_public_keys(parameters)
    shared_key = exchange_keys_and_compute_shared_key(
        alice_private_key, alice_public_key, bob_private_key, bob_public_key
    )
    if shared_key:
        Seed_Generator.generate_seed(
            alice_private_key, bob_private_key,
            alice_public_key, bob_public_key
        )
        return shared_key
    return False
if __name__ == "__main__":
    shared_key = generate_access_key()
    if shared_key:
        print("Access key generated successfully.")
    else:
        print("Failed to generate access key.")