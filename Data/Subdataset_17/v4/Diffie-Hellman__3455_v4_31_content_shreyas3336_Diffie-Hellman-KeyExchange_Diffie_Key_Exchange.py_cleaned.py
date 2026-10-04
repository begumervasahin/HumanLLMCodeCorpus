from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import Seed_Generator
def generate_access_key():
    parameters = dh.generate_parameters(generator=5, key_size=1024, backend=default_backend())
    alice_private_key = parameters.generate_private_key()
    alice_public_key = alice_private_key.public_key()
    bob_private_key = parameters.generate_private_key()
    bob_public_key = bob_private_key.public_key()
    alice_shared_key = alice_private_key.exchange(bob_public_key)
    bob_shared_key = bob_private_key.exchange(alice_public_key)
    if alice_shared_key == bob_shared_key:
        Seed_Generator.generate_seed(
            alice_private_key, bob_private_key,
            alice_public_key, bob_public_key
        )
        return alice_shared_key
    else:
        return False
shared_key = generate_access_key()
if shared_key:
    print("Access key generated successfully.")
else:
    print("Failed to generate access key.")