from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import Seeded_Random_Generator
def extract_key_value(key):
    key_str = str(key)
    key_hex = key_str.split(' ')[-1].rstrip('>')
    return int(key_hex, 16)
def generate_seed(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key, initial_seed=3336):
    a_pkey = extract_key_value(a_private_key)
    b_pkey = extract_key_value(b_private_key)
    a_public_key = extract_key_value(a_peer_public_key)
    b_public_key = extract_key_value(b_peer_public_key)
    x1 = (a_public_key ^ a_pkey) % b_public_key
    x2 = (a_public_key ^ b_pkey) % b_public_key
    k1 = (x2 ^ a_pkey) % b_public_key
    k2 = (x1 ^ b_pkey) % b_public_key
    if k1 == k2:
        seed = k1 % 1111
    else:
        seed = initial_seed
    new_seed = Seeded_Random_Generator.reduce(seed)
    print("Original seed:", seed, "New seed:", new_seed)
    Seeded_Random_Generator.random_generator(new_seed)
def generate_diffie_hellman_parameters():
    return dh.generate_parameters(generator=5, key_size=1024, backend=default_backend())
def generate_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key
def main():
    parameters = generate_diffie_hellman_parameters()
    alice_private_key, alice_public_key = generate_key_pair(parameters)
    bob_private_key, bob_public_key = generate_key_pair(parameters)
    generate_seed(alice_private_key, bob_private_key, alice_public_key, bob_public_key)
if __name__ == "__main__":
    main()