from ecc import EllipticCurve, Point
def generate_keys(p: int, a: int, b: int, G: tuple, n: int) -> Point:
    elliptic_curve = EllipticCurve(a, b, p)
    generator = Point(elliptic_curve, G[0], G[1], "Generator")
    generated_point = generator * n
    return generated_point
if __name__ == '__main__':
    prime_field_size = 37
    coefficient_a = 7
    coefficient_b = 3
    generator_point = (2, 5)
    alice_private_key = 4
    bob_private_key = 7
    ecc = EllipticCurve(coefficient_a, coefficient_b, prime_field_size)
    Generator = Point(ecc, generator_point[0], generator_point[1], "Generator")
    alice_pub = alice_private_key * Generator
    alice_pub.name = "Alice Public Key"
    bob_pub = bob_private_key * Generator
    bob_pub.name = "Bob Public Key"
    shared_secret_bob = alice_pub * bob_private_key
    shared_secret_alice = bob_pub * alice_private_key
    assert shared_secret_alice == shared_secret_bob
    shared_secret_alice.name = "Shared Secret"
    ecc.plot_points([Generator, alice_pub, bob_pub, shared_secret_alice])