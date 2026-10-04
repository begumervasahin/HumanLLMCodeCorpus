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
    print(f"Original seed: {seed}, New seed: {new_seed}")
    Seeded_Random_Generator.random_generator(new_seed)
if __name__ == "__main__":
    a_private_key = "<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x7f8b6c34>"
    b_private_key = "<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x7f8b6c35>"
    a_peer_public_key = "<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x7f8b6c36>"
    b_peer_public_key = "<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x7f8b6c37>"
    generate_seed(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key)