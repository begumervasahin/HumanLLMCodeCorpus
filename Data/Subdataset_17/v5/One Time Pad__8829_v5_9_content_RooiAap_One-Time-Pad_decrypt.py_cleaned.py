from modules import algorithms
def decrypt_ciphertext(ciphertext, pad):
    ciphertext_positions = algorithms.alph_pos(list(ciphertext))
    pad_positions = algorithms.alph_pos(list(pad))
    plaintext_positions = [
        algorithms.modinverse((ciphertext_positions[i] - pad_positions[i]), 26)
        for i in range(len(ciphertext_positions))
    ]
    plaintext = algorithms.num_alph(plaintext_positions)
    return "".join(plaintext)
def main():
    ciphertext = input("Enter ciphertext: ")
    pad = input("Enter pad: ")
    decrypted_text = decrypt_ciphertext(ciphertext, pad)
    print("Decrypted text:", decrypted_text)
if __name__ == "__main__":
    main()