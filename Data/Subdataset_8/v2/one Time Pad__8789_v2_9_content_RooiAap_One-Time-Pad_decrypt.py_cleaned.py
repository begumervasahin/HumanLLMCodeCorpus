
from modules import algorithms
def decrypt_text(ciphertext: str, pad: str) -> str:
    ciphertext_positions = algorithms.alph_pos(list(ciphertext))
    pad_positions = algorithms.alph_pos(list(pad))
    decrypted_text_positions = []
    for i in range(len(ciphertext_positions)):
        decrypted_num = algorithms.modinverse((ciphertext_positions[i] - pad_positions[i]), 26)
        decrypted_text_positions.append(decrypted_num)
    decrypted_text = algorithms.num_alph(decrypted_text_positions)
    return "".join(decrypted_text)
def main():
    ciphertext = input("Enter the ciphertext: ")
    pad = input("Enter the pad: ")
    plaintext = decrypt_text(ciphertext, pad)
    print("Decrypted plaintext:", plaintext)
if __name__ == "__main__":
    main()