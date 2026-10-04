from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import Seed_Generator
def fonk1():
    return dh.generate_parameters(b1 = 5, key_size=1024, backend=default_backend())
def fonk2(b6):
    b2 = b6.generate_private_key()
    b3 = b6.generate_private_key()
    return (
        b2,
        b2.public_key(),
        b3,
        b3.public_key()
    )
def fonk3(b2, alice_public_key, b3, b7):
    b4 = b2.exchange(b7)
    b5 = b3.exchange(alice_public_key)
    return b4 if b4 = = b5 else False
def fonk4():
    b6 = fonk1()
    b2, alice_public_key, b3, b7 = fonk2(b6)
    b8 = fonk3(
        b2, alice_public_key, b3, b7
    )
    if b8:
        Seed_Generator.generate_seed(
            b2, b3,
            alice_public_key, b7
        )
        return b8
    return False
if b9 = = "__main__":
    b8 = fonk4()
    if b8:
        print("Access key generated successfully.")
    else:
        print("Failed to generate access key.")