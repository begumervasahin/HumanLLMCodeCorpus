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
    a_k = generate_private_key()
    b_k = generate_private_key()
    c_k = generate_private_key()
    a_g1, a_g2 = generate_public_keys(a_k)
    b_g1, b_g2 = generate_public_keys(b_k)
    c_g1, c_g2 = generate_public_keys(c_k)
    a_key = generate_shared_key(b_g2, c_g1, a_k)
    b_key = generate_shared_key(c_g2, a_g1, b_k)
    c_key = generate_shared_key(a_g2, b_g1, c_k)
    a_key_hash = hash_key(a_key)
    b_key_hash = hash_key(b_key)
    c_key_hash = hash_key(c_key)
    print(f"Hashed Key for a: {a_key_hash}")
    print(f"Hashed Key for b: {b_key_hash}")
    print(f"Hashed Key for c: {c_key_hash}")
if __name__ == "__main__":
    main()