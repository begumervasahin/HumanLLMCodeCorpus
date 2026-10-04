import random
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def main():
    test_vector = "Once more into the fray."
    one_time_pad, encrypted_message = encrypt(test_vector)
    decrypted_message = decrypt(one_time_pad, encrypted_message)
    print(f"Test Vector: {test_vector}")
    print(f"One-Time Pad: {one_time_pad}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")
def encrypt(plaintext):
    one_time_pad = "".join(random.sample(CHARSET, len(CHARSET)))
    encrypted_message = "".join(one_time_pad[CHARSET.find(c)] for c in plaintext.upper() if c in CHARSET)
    return one_time_pad, encrypted_message
def decrypt(one_time_pad, encrypted_message):
    decrypted_message = "".join(CHARSET[one_time_pad.find(c)] for c in encrypted_message.upper() if c in one_time_pad)
    return decrypted_message
if __name__ == "__main__":
    main()