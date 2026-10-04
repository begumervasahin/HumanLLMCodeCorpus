from modules import algorithms
def decrypt(ciphertext: str, pad: str) -> str:
    c_text_num = algorithms.alph_pos(list(ciphertext))
    pad_num = algorithms.alph_pos(list(pad))
    p_text_num = []
    for p in range(len(c_text_num)):
        y = algorithms.modinverse((c_text_num[p] - pad_num[p]), 26)
        p_text_num.append(y)
    plaintext = algorithms.num_alph(p_text_num)
    return "".join(plaintext)
if __name__ == "__main__":
    c_text = input("Enter ciphertext: ")
    pad = input("Enter pad: ")
    if len(c_text) != len(pad):
        print("Error: The length of the ciphertext and the pad must be the same.")
    else:
        decrypted_text = decrypt(c_text, pad)
        print("Decrypted text:", decrypted_text)