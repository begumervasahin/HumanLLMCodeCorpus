import random
import bn256
def generate_random_scalar():
    return random.randrange(2, bn256.order)
def generate_random_points():
    a_k = generate_random_scalar()
    b_k = generate_random_scalar()
    c_k = generate_random_scalar()
    a_g1 = bn256.g1_scalar_base_mult(a_k)
    b_g1 = bn256.g1_scalar_base_mult(b_k)
    c_g1 = bn256.g1_scalar_base_mult(c_k)
    a_g2 = bn256.g2_scalar_base_mult(a_k)
    b_g2 = bn256.g2_scalar_base_mult(b_k)
    c_g2 = bn256.g2_scalar_base_mult(c_k)
    return ((a_g1, b_g1, c_g1), (a_g2, b_g2, c_g2))
def calculate_keys(points, scalars):
    a_g1, b_g1, c_g1 = points[0]
    a_g2, b_g2, c_g2 = points[1]
    a_k, b_k, c_k = scalars
    a_key = bn256.gt_scalar_mult(bn256.optimal_ate(b_g2, c_g1), a_k)
    b_key = bn256.gt_scalar_mult(bn256.optimal_ate(c_g2, a_g1), b_k)
    c_key = bn256.gt_scalar_mult(bn256.optimal_ate(a_g2, b_g1), c_k)
    return (a_key, b_key, c_key)
def print_keys(keys):
    a_key, b_key, c_key = keys
    print("Hash of a_key:", bn256.gt_hash(a_key))
    print("Hash of b_key:", bn256.gt_hash(b_key))
    print("Hash of c_key:", bn256.gt_hash(c_key))
points = generate_random_points()
keys = calculate_keys(points, (a_k, b_k, c_k))
print_keys(keys)