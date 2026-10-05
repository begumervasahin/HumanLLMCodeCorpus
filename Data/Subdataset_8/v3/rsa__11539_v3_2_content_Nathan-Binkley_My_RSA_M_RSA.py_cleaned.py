from ecdsa.numbertheory import inverse_mod as modinv
import sys
def main():
    public_exponent = 65537
    try:
        p = int(input("Enter a prime number: "))
        q = int(input("Enter another prime number (ensure their sum is at least 26 for alphabet encoding): "))
        if p + q < 26:
            raise ValueError("The sum of the input values should be at least 26.")
    except ValueError as ve:
        print("Error:", ve)
        sys.exit(1)
    modulus = p * q
    private_exponent = modinv(public_exponent, ((p-1)*(q-1)))
    plaintext = input("Enter the text you want to encrypt: ").lower()
    print("Your plaintext is:", plaintext)
    print("p:", p)
    print("q:", q)
    plain_num_list = [ord(char) - 96 for char in plaintext if char.isalpha()]
    print("Your plaintext list is:", plain_num_list)
    encrypted_num_list = [(num**public_exponent) % modulus for num in plain_num_list]
    print("Your encrypted values are:", encrypted_num_list)
    decrypted_num_list = [(num**private_exponent) % modulus for num in encrypted_num_list]
    print("Your decrypted values are:", decrypted_num_list)
    decrypted_text = ''.join([chr(num + 96) for num in decrypted_num_list])
    print("Plaintext (Decrypted) is:", decrypted_text)
if __name__ == "__main__":
    main()