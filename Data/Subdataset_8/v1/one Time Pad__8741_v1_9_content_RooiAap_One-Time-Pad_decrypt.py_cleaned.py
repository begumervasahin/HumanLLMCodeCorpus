
from modules import algorithms
def decrypt_text(ciphertext: str, pad: str) -> str:
    c_text_num = algorithms.alph_pos(list(ciphertext))
    pad_num = algorithms.alph_pos(list(pad))
    p_text_num = []
    for i in range(len(c_text_num)):
        decrypted_num = algorithms.modinverse((c_text_num[i] - pad_num[i]), 26)
        p_text_num.append(decrypted_num)
    decrypted_text = algorithms.num_alph(p_text_num)
    return "".join(decrypted_text)
def main():
    ciphertext = input("Enter ciphertext: ")
    pad = input("Enter pad: ")
    plaintext = decrypt_text(ciphertext, pad)
    print("Decrypted plaintext:", plaintext)
if __name__ == "__main__":
    main()