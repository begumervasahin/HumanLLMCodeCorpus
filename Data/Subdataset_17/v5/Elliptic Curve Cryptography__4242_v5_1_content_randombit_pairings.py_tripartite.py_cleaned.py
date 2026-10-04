import random
import bn256
def generate_private_key():
    return random.randrange(2, bn256.order)
def generate_public_keys(private_key):
    public_key_g1 = bn256.g1_scalar_base_mult(private_key)
    public_key_g2 = bn256.g2_scalar_base_mult(private_key)
    return public_key_g1, public_key_g2
def generate_shared_key(public_key_g2, public_key_g1, private_key):
    pairing_result = bn256.optimal_ate(public_key_g2, public_key_g1)
    return bn256.gt_scalar_mult(pairing_result, private_key)
def hash_key(shared_key):
    return bn256.gt_hash(shared_key)
def main():
    a_private_key = generate_private_key()
    b_private_key = generate_private_key()
    c_private_key = generate_private_key()
    a_public_key_g1, a_public_key_g2 = generate_public_keys(a_private_key)
    b_public_key_g1, b_public_key_g2 = generate_public_keys(b_private_key)
    c_public_key_g1, c_public_key_g2 = generate_public_keys(c_private_key)
    a_shared_key = generate_shared_key(b_public_key_g2, c_public_key_g1, a_private_key)
    b_shared_key = generate_shared_key(c_public_key_g2, a_public_key_g1, b_private_key)
    c_shared_key = generate_shared_key(a_public_key_g2, b_public_key_g1, c_private_key)
    a_hashed_key = hash_key(a_shared_key)
    b_hashed_key = hash_key(b_shared_key)
    c_hashed_key = hash_key(c_shared_key)
    print(f"Hashed Key for a: {a_hashed_key}")
    print(f"Hashed Key for b: {b_hashed_key}")
    print(f"Hashed Key for c: {c_hashed_key}")
if __name__ == "__main__":
    main()