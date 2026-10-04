
import random
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def main():
    vector = "Once more into the fray."
    otp, encrypted_message = encrypt(vector)
    decrypted_message = decrypt(otp, encrypted_message)
    print(f"Test Vector: {vector}")
    print(f"OTP: {otp}")
    print(f"Encrypted: {encrypted_message}")
    print(f"Decrypted: {decrypted_message}")
def encrypt(plaintext):
    otp = "".join(random.sample(CHARSET, len(CHARSET)))
    result = "".join(otp[CHARSET.find(c)] for c in plaintext.upper() if c in CHARSET)
    return otp, result
def decrypt(otp, secret):
    result = "".join(CHARSET[otp.find(c)] for c in secret.upper() if c in otp)
    return result
if __name__ == "__main__":
    main()