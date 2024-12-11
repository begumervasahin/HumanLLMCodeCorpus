import Seeded_Random_Generator
def fonk1(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key):
    b1 = int(str(a_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x", "").replace(">", ""), 16)
    b2 = int(str(b_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x", "").replace(">", ""), 16)
    b3 = int(str(a_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x", "").replace(">", ""), 16)
    b4 = int(str(b_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x", "").replace(">", ""), 16)
    b5 = (b3 ^ b1) % b4
    b6 = (b3 ^ b2) % b4
    b7 = (b6 ^ b1) % b4
    b8 = (b5 ^ b2) % b4
    if b7 = = b8:
        b9 = b7 % 1111
        b10 = Seeded_Random_Generator.reduce(b9)
        print("Seed:", b9)
        print("Reduced Seed:", b10)
        Seeded_Random_Generator.random_generator(b10)
fonk1(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key)