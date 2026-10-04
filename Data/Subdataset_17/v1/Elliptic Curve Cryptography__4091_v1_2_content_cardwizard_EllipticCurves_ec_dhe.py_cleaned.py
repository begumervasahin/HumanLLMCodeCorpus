from ecc import EllipticCurve, Point
from typing import Tuple
def generate_keys(p: int, a: int, b: int, G: Tuple[int, int], n: int) -> Point:
    elliptic_curve = EllipticCurve(a, b, p)
    generator = Point(elliptic_curve, G[0], G[1], "Generator")
    generated_point = generator * n
    return generated_point
if __name__ == '__main__':
    alice_private_key = 4
    bob_private_key = 7
    p = 37
    a = 7
    b = 3
    G = (2, 5)
    ecc = EllipticCurve(a, b, p)
    Generator = Point(ecc, G[0], G[1], "Generator")
    alice_pub = generate_keys(p, a, b, G, alice_private_key)
    alice_pub.name = "Alice Public Key"
    bob_pub = generate_keys(p, a, b, G, bob_private_key)
    bob_pub.name = "Bob Public Key"
    shared_secret_bob = alice_pub * bob_private_key
    shared_secret_alice = bob_pub * alice_private_key
    assert shared_secret_alice == shared_secret_bob
    shared_secret_alice.name = "Shared Secret"
    ecc.plot_points([Generator, alice_pub, bob_pub, shared_secret_alice])