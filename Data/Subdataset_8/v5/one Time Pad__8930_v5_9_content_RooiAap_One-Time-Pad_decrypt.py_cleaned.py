
from modules import algorithms
def decrypt_ciphertext(ciphertext, pad):
    ciphertext_list = list(ciphertext)
    pad_list = list(pad)
    ciphertext_num = algorithms.alph_pos(ciphertext_list)
    pad_num = algorithms.alph_pos(pad_list)
    plaintext_num = []
    for ct_num, pad_num in zip(ciphertext_num, pad_num):
        inverse_mod = algorithms.modinverse((ct_num - pad_num), 26)
        plaintext_num.append(inverse_mod)
    plaintext = algorithms.num_alph(plaintext_num)
    return "".join(plaintext)
def main():
    ciphertext = input("Enter ciphertext: ")
    pad = input("Enter pad: ")
    decrypted_text = decrypt_ciphertext(ciphertext, pad)
    print("Decrypted plaintext:", decrypted_text)
if __name__ == "__main__":
    main()