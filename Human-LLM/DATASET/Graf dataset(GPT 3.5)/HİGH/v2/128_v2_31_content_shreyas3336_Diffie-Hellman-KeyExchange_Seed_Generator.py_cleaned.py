import Seeded_Random_Generator
def fonk1(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key):
    b1 = str(a_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x", "").replace(">", "")
    b2 = str(b_private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x", "").replace(">", "")
    b3 = str(a_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x", "").replace(">", "")
    b4 = str(b_peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x", "").replace(">", "")
    b5 = int(b1, 16)
    b6 = int(b2, 16)
    b7 = int(b3, 16)
    b8 = int(b4, 16)
    b9 = (b7 ^ b5) % b8
    b10 = (b7 ^ b6) % b8
    b11 = (b10 ^ b5) % b8
    b12 = (b9 ^ b6) % b8
    if b11 = = b12:
        b13 = b11 % 1111
        b14 = Seeded_Random_Generator.reduce(b13)
        print("Seed:", b13)
        print("Reduced Seed:", b14)
        Seeded_Random_Generator.random_generator(b14)
fonk1(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key)