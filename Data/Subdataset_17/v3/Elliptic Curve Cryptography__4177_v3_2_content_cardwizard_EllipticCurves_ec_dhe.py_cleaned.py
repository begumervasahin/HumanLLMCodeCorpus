from ecc import EllipticCurve, Point
from typing import Tuple
def generate_public_key(p: int, a: int, b: int, G: Tuple[int, int], private_key: int) -> Point:
    elliptic_curve = EllipticCurve(a, b, p)
    generator_point = Point(elliptic_curve, G[0], G[1], "Generator")
    public_key = generator_point * private_key
    return public_key
def main():
    alice_private_key = 4
    bob_private_key = 7
    p = 37
    a = 7
    b = 3
    G = (2, 5)
    ecc = EllipticCurve(a, b, p)
    generator_point = Point(ecc, G[0], G[1], "Generator")
    alice_public_key = generate_public_key(p, a, b, G, alice_private_key)
    alice_public_key.name = "Alice Public Key"
    bob_public_key = generate_public_key(p, a, b, G, bob_private_key)
    bob_public_key.name = "Bob Public Key"
    shared_secret_from_bob = alice_public_key * bob_private_key
    shared_secret_from_alice = bob_public_key * alice_private_key
    assert shared_secret_from_alice == shared_secret_from_bob
    shared_secret_from_alice.name = "Shared Secret"
    ecc.plot_points([generator_point, alice_public_key, bob_public_key, shared_secret_from_alice])
if __name__ == '__main__':
    main()