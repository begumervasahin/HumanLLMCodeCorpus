from ecc import EllipticCurve, Point
def generate_keys(prime_field_size: int, coefficient_a: int, coefficient_b: int, generator_point: tuple, private_key: int) -> Point:
    elliptic_curve = EllipticCurve(coefficient_a, coefficient_b, prime_field_size)
    generator = Point(elliptic_curve, generator_point[0], generator_point[1], "Generator")
    generated_point = generator * private_key
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
    alice_public_key = generate_keys(prime_field_size, coefficient_a, coefficient_b, generator_point, alice_private_key)
    alice_public_key.name = "Alice Public Key"
    bob_public_key = generate_keys(prime_field_size, coefficient_a, coefficient_b, generator_point, bob_private_key)
    bob_public_key.name = "Bob Public Key"
    shared_secret_bob = alice_public_key * bob_private_key
    shared_secret_alice = bob_public_key * alice_private_key
    assert shared_secret_alice == shared_secret_bob
    shared_secret_alice.name = "Shared Secret"
    ecc.plot_points([Generator, alice_public_key, bob_public_key, shared_secret_alice])