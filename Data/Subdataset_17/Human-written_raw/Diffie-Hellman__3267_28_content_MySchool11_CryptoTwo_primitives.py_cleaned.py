__author__ = "Mr Bancroft"
from random import sample
def calculate_prime_primitives(prime):
    number_to_check = 0
    print("Working out public key and public shared base...")
    primitive_roots = []
    for each in range(1, prime):
        number_to_check += 1
        candidate_prime_roots = []
        for i in range(1, prime):
            modulus = (number_to_check ** i) % prime
            candidate_prime_roots.append(modulus)
            cleaned_up_candidate_prime_roots = set(candidate_prime_roots)
            if len(cleaned_up_candidate_prime_roots) == len(range(1, prime)):
                primitive_roots.append(number_to_check)
    return sample(primitive_roots, 1)[0]