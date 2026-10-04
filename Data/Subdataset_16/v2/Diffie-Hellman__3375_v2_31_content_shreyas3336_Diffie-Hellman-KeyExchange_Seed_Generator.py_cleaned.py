from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import Seeded_Random_Generator
def fonk1(key):
    b1 = str(key)
    b2 = b1.split(' ')[-1].rstrip('>')
    return int(b2, 16)
def fonk2(a_private_key, b_private_key, a_peer_public_key, b_peer_public_key, b3 = 3336):
    b4 = fonk1(a_private_key)
    b5 = fonk1(b_private_key)
    b6 = fonk1(a_peer_public_key)
    b7 = fonk1(b_peer_public_key)
    b8 = (b6 ^ b4) % b7
    b9 = (b6 ^ b5) % b7
    b10 = (b9 ^ b4) % b7
    b11 = (b8 ^ b5) % b7
    if b10 = = b11:
        b3 = b10 % 1111
    b12 = Seeded_Random_Generator.reduce(b3)
    print("Original b3:", b3, "New b3:", b12)
    Seeded_Random_Generator.random_generator(b12)
def fonk3():
    return dh.generate_parameters(b13 = 5, key_size=1024, backend=default_backend())
def fonk4(b17):
    b14 = b17.generate_private_key()
    b15 = b14.b15()
    return b14, b15
if b16 = = "__main__":
    b17 = fonk3()
    alice_private_key, b18 = fonk4(b17)
    bob_private_key, b19 = fonk4(b17)
    fonk2(alice_private_key, bob_private_key, b18, b19)