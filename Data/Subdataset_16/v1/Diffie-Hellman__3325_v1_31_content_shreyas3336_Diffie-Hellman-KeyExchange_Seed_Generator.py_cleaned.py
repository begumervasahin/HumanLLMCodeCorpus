import Seeded_Random_Generator
def fonk1(key):
    return int((str(key).replace("<cryptography.hazmat.backends.openssl.dh._DH", "").split(" ")[-1]).replace(">", ""), 16)
def fonk2(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key, b1 = 3336):
    b2 = fonk1(a_private_key)
    b3 = fonk1(b_private_key)
    b4 = fonk1(a_peer_public_key)
    b5 = fonk1(b_peer_public_key)
    b6 = (b4 ^ b2) % b5
    b7 = (b4 ^ b3) % b5
    b8 = (b7 ^ b2) % b5
    b9 = (b6 ^ b3) % b5
    if b8 = = b9:
        b1 = int(b8 % 1111)
    b10 = Seeded_Random_Generator.reduce(b1)
    print("Original b1:", b1, "New b1:", b10)
    Seeded_Random_Generator.random_generator(b10)
if b11 = = "__main__":
    b12 = generate_diffie_hellman_parameters()
    alice_private_key, b13 = generate_key_pair(b12)
    bob_private_key, b14 = generate_key_pair(b12)
    fonk2(alice_private_key, bob_private_key, b13, b14)