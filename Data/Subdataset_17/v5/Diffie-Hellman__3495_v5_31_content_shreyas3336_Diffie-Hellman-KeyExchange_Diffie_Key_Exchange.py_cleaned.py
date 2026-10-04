from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import Seed_Generator
def generate_diffie_hellman_parameters():
    return dh.generate_parameters(generator=5, key_size=1024, backend=default_backend())
def generate_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key
def compute_shared_key(private_key, peer_public_key):
    return private_key.exchange(peer_public_key)
def generate_access_key():
    parameters = generate_diffie_hellman_parameters()
    alice_private_key, alice_public_key = generate_key_pair(parameters)
    bob_private_key, bob_public_key = generate_key_pair(parameters)
    alice_shared_key = compute_shared_key(alice_private_key, bob_public_key)
    bob_shared_key = compute_shared_key(bob_private_key, alice_public_key)
    if alice_shared_key == bob_shared_key:
        Seed_Generator.generate_seed(
            alice_private_key, bob_private_key,
            alice_public_key, bob_public_key
        )
        return alice_shared_key
    else:
        return False
def main():
    shared_key = generate_access_key()
    if shared_key:
        print("Access key generated successfully.")
    else:
        print("Failed to generate access key.")
if __name__ == "__main__":
    main()