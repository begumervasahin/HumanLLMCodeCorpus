import Seeded_Random_Generator
def generate_seed(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key):
    a_private_key_hex = str(a_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x", "").replace(">", "")
    b_private_key_hex = str(b_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x", "").replace(">", "")
    a_peer_public_key_hex = str(a_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x", "").replace(">", "")
    b_peer_public_key_hex = str(b_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x", "").replace(">", "")
    a_pkey = int(a_private_key_hex, 16)
    b_pkey = int(b_private_key_hex, 16)
    a_public_key = int(a_peer_public_key_hex, 16)
    b_public_key = int(b_peer_public_key_hex, 16)
    x1 = (a_public_key ^ a_pkey) % b_public_key
    x2 = (a_public_key ^ b_pkey) % b_public_key
    k1 = (x2 ^ a_pkey) % b_public_key
    k2 = (x1 ^ b_pkey) % b_public_key
    if k1 == k2:
        seed = k1 % 1111
        new_seed = Seeded_Random_Generator.reduce(seed)
        print("Seed:", seed)
        print("Reduced Seed:", new_seed)
        Seeded_Random_Generator.random_generator(new_seed)
generate_seed(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key)