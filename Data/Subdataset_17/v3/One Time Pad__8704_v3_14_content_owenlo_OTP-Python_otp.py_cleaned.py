import random
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def main():
    vector = "Once more into the fray."
    otp, encrypted_message = encrypt(vector)
    decrypted_message = decrypt(otp, encrypted_message)
    print(f"Test Vector: {vector}")
    print(f"One-Time Pad (OTP): {otp}")
    print(f"Encrypted: {encrypted_message}")
    print(f"Decrypted: {decrypted_message}")
def generate_otp():
    return "".join(random.sample(CHARSET, len(CHARSET)))
def encrypt(plaintext):
    otp = generate_otp()
    encrypted_message = "".join(
        otp[CHARSET.index(c)] if c in CHARSET else c for c in plaintext.upper()
    )
    return otp, encrypted_message
def decrypt(otp, encrypted_message):
    decrypted_message = "".join(
        CHARSET[otp.index(c)] if c in otp else c for c in encrypted_message.upper()
    )
    return decrypted_message
if __name__ == "__main__":
    main()