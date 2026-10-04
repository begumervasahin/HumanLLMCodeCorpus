from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import Seed_Generator
def fonk1():
    return dh.generate_parameters(b1 = 5, key_size=1024, backend=default_backend())
def fonk2(b4):
    b2 = b4.generate_private_key()
    b3 = b2.b3()
    return b2, b3
def fonk3(b2, peer_public_key):
    return b2.exchange(peer_public_key)
def fonk4():
    b4 = fonk1()
    alice_private_key, b5 = fonk2(b4)
    bob_private_key, b6 = fonk2(b4)
    b7 = fonk3(alice_private_key, b6)
    b8 = fonk3(bob_private_key, b5)
    if b7 = = b8:
        Seed_Generator.generate_seed(
            alice_private_key, bob_private_key,
            b5, b6
        )
        return b7
    else:
        return False
def fonk5():
    b9 = fonk4()
    if b9:
        print("Access key generated successfully.")
    else:
        print("Failed to generate access key.")
if b10 = = "__main__":
    fonk5()