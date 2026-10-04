from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import Seed_Generator
def fonk1():
    b1 = dh.generate_parameters(generator=5, key_size=1024, backend=default_backend())
    b2 = b1.generate_private_key()
    b3 = b2.public_key()
    b4 = b1.generate_private_key()
    b5 = b4.public_key()
    b6 = b2.exchange(b5)
    b7 = b4.exchange(b3)
    if b6 = = b7:
        Seed_Generator.generate_seed(
            b2, b4,
            b3, b5
        )
        return b6
    else:
        return False
b8 = fonk1()
if b8:
    print("Access key generated successfully.")
else:
    print("Failed to generate access key.")