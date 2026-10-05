from ecdsa.numbertheory import inverse_mod as modinv
import sys
def main():
    e = 65537
    try:
        p = int(input("Enter a prime number: "))
        q = int(input("Enter another prime number (ensure their sum is at least 26 for alphabet encoding): "))
        if p + q < 26:
            raise ValueError("The sum of the input values should be at least 26.")
    except ValueError as ve:
        print("Error:", ve)
        sys.exit(1)
    n = p * q
    d = modinv(e, ((p-1)*(q-1)))
    plaintext = input("Enter the text you want to encrypt: ").lower()
    print("Your plaintext is:", plaintext)
    print("p:", p)
    print("q:", q)
    plain_list_num = [ord(char) - 96 for char in plaintext if char.isalpha()]
    print("Your plaintext list is:", plain_list_num)
    enc_list_num = [(i**e) % n for i in plain_list_num]
    print("Your encrypted values are:", enc_list_num)
    end_list_num = [(i**d) % n for i in enc_list_num]
    print("Your decrypted values are:", end_list_num)
    ending = ''.join([chr(num + 96) for num in end_list_num])
    print("Plaintext (Decrypted) is:", ending)
if __name__ == "__main__":
    main()