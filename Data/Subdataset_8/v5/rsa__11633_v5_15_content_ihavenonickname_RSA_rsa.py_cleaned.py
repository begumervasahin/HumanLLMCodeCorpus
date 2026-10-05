class RSAKey:
    def __init__(self, exponent, modulus):
        self.exponent = exponent
        self.modulus = modulus
    def encrypt(self, plaintext):
        return pow(plaintext, self.exponent, self.modulus)
def calculate_modular_inverse(u, v):
    a, b = u, v
    x, y = 0, 1
    while a != 0:
        quotient = b
        a, b = b - quotient * a, a
        x, y = y - quotient * x, x
    return y % v
def generate_rsa_keys(prime_p, prime_q):
    phi = (prime_p - 1) * (prime_q - 1)
    modulus = prime_p * prime_q
    public_exponent = 65537
    private_exponent = calculate_modular_inverse(public_exponent, phi)
    public_key = RSAKey(exponent=public_exponent, modulus=modulus)
    private_key = RSAKey(exponent=private_exponent, modulus=modulus)
    return public_key, private_key
def main():
    public_key, private_key = generate_rsa_keys(23, 29)
    original_value = 42
    encrypted_value = public_key.encrypt(original_value)
    decrypted_value = private_key.encrypt(encrypted_value)
    print("Original:", original_value)
    print("Encrypted:", encrypted_value)
    print("Decrypted:", decrypted_value)
if __name__ == '__main__':
    main()