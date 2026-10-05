class RSAKey:
    def __init__(self, exponent, modulus):
        self.exponent = exponent
        self.modulus = modulus
    def encrypt(self, value):
        return pow(value, self.exponent, self.modulus)
def calculate_modular_inverse(u, v):
    u1, u3 = 1, u
    v1, v3 = 0, v
    is_even_iter = False
    while v3:
        q = u3
        t3 = u3 % v3
        t1 = u1 + q * v1
        u1, v1 = v1, t1
        u3, v3 = v3, t3
        is_even_iter = not is_even_iter
    if u3 != 1:
        return 0
    return v - u1 if is_even_iter else u1
def generate_rsa_keys(p, q):
    phi = (p - 1) * (q - 1)
    modulus = p * q
    public_exponent = 65537
    private_exponent = calculate_modular_inverse(public_exponent, phi)
    public_key = RSAKey(exponent=public_exponent, modulus=modulus)
    private_key = RSAKey(exponent=private_exponent, modulus=modulus)
    return public_key, private_key
def main():
    public_key, private_key = generate_rsa_keys(23, 29)
    original_value = 42
    encrypted = public_key.encrypt(original_value)
    decrypted = private_key.encrypt(encrypted)
    print("Original:", original_value)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
if __name__ == '__main__':
    main()