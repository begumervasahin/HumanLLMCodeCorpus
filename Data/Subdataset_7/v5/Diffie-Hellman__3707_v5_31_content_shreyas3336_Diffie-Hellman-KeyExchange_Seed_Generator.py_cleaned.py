import Seeded_Random_Generator
def fonk1(private_key):
    return int(str(private_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x", "").replace(">", ""), 16)
def fonk2(peer_public_key):
    return int(str(peer_public_key).replace("<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x", "").replace(">", ""), 16)
def fonk3(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key):
    b1 = fonk1(a_private_key)
    b2 = fonk1(b_private_key)
    b3 = fonk2(a_peer_public_key)
    b4 = fonk2(b_peer_public_key)
    b5 = (b3 ^ b1) % b4
    b6 = (b3 ^ b2) % b4
    b7 = (b6 ^ b1) % b4
    b8 = (b5 ^ b2) % b4
    return b7, b8
def fonk4(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key):
    b7, b8 = fonk3(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key)
    if b7 = = b8:
        b9 = b7 % 1111
        b10 = Seeded_Random_Generator.reduce(b9)
        print("Seed:", b9)
        print("Reduced Seed:", b10)
        Seeded_Random_Generator.random_generator(b10)
fonk4(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key)