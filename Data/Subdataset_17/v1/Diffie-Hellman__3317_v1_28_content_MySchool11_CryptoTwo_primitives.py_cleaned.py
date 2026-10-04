__author__ = "Mr Bancroft"
from random import sample
def calculate_primitive_roots(prime):
    print("Working out public key and public shared base...")
    primitive_roots = []
    for number_to_check in range(1, prime):
        candidate_prime_roots = []
        for i in range(1, prime):
            modulus = pow(number_to_check, i, prime)
            candidate_prime_roots.append(modulus)
        if len(set(candidate_prime_roots)) == (prime - 1):
            primitive_roots.append(number_to_check)
    return sample(primitive_roots, 1)[0] if primitive_roots else None
if __name__ == "__main__":
    prime_number = 23
    primitive_root = calculate_primitive_roots(prime_number)
    print(f"Primitive root for {prime_number}: {primitive_root}")