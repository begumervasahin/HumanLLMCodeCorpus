from random import choice
def is_primitive_root(candidate, prime):
    residues = set()
    for exponent in range(1, prime):
        residue = pow(candidate, exponent, prime)
        residues.add(residue)
    return len(residues) == prime - 1
def find_random_primitive_root(prime):
    print("Calculating public key and base...")
    primitive_roots = [
        candidate
        for candidate in range(1, prime)
        if is_primitive_root(candidate, prime)
    ]
    return choice(primitive_roots) if primitive_roots else None
if __name__ == "__main__":
    prime_number = 23
    primitive_root = find_random_primitive_root(prime_number)
    print(f"A primitive root of {prime_number} is: {primitive_root}")