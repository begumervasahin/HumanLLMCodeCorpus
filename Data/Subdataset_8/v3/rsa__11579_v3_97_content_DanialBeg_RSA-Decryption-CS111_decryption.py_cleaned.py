import string
def main():
    exponent, modulus = get_public_key()
    print("Exponent:", exponent)
    print("Modulus:", modulus)
    p, q = calculate_factors(modulus)
    phi_n = calculate_phi_n(p, q)
    decrypt_exponent = calculate_decrypt_exponent(exponent, phi_n)
    encrypted_message = [51, 12, 51, 39, 31, 21, 14, 10, 20, 17, 7, 25, 14, 26, 33, 52, 15, 7,
                   27, 51, 7, 49, 8, 15, 51, 7, 8, 25, 7, 25, 10, 49, 18, 52, 51, 7, 8,
                   25, 7, 18, 26, 25, 25, 10, 27, 52, 51, 7, 27, 33, 21, 7, 20, 26, 21,
                   7, 25, 10, 49, 18, 52, 51, 39]
    alphabet = list(string.ascii_lowercase)
    alphabet.append(' ')
    decrypted_message = decrypt_message(encrypted_message, decrypt_exponent, modulus, alphabet)
    print("Decrypted Message:", decrypted_message)
def get_public_key():
    exponent = int(input("Please enter the exponent value in the public key: "))
    modulus = int(input("Please enter the modulus value in the public key: "))
    return exponent, modulus
def calculate_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors[1], factors[2]
def calculate_phi_n(p, q):
    return (p + 1) * (q + 1)
def calculate_decrypt_exponent(exponent, phi_n):
    return modular_inverse(exponent, phi_n)
def modular_inverse(a, b):
    for num in range(1, b):
        if (a * num) % b == 1:
            return num
    return 1
def decrypt_message(encrypted_message, decrypt_exponent, modulus, alphabet):
    decrypted_message = ""
    for encrypted_char in encrypted_message:
        decrypted_char_index = pow(encrypted_char, decrypt_exponent, modulus) - 2
        decrypted_char = alphabet[decrypted_char_index]
        decrypted_message += decrypted_char
    return decrypted_message
if __name__ == "__main__":
    main()