import random
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def main():
    vector = "Once more into the fray."
    encrypted_otp, encrypted_message = encrypt(vector)
    decrypted_message = decrypt(encrypted_otp, encrypted_message)
    print("Test Vector: " + vector)
    print("OTP: " + encrypted_otp)
    print("Encrypted: " + encrypted_message)
    print("Decrypted: " + decrypted_message)
def encrypt(plaintext):
    otp = "".join(random.sample(CHARSET, len(CHARSET)))
    result = ""
    for c in plaintext.upper():
        if c in CHARSET:
            result += otp[CHARSET.index(c)]
        else:
            result += c
    return otp, result
def decrypt(otp, secret):
    result = ""
    for c in secret.upper():
        if c in otp:
            result += CHARSET[otp.index(c)]
        else:
            result += c
    return result
if __name__ == "__main__":
    main()