
from modules import algorithms
ciphertext = input("Enter ciphertext: ")
pad = input("Enter pad: ")
ciphertext_list = list(ciphertext)
pad_list = list(pad)
ciphertext_num = algorithms.alph_pos(ciphertext_list)
pad_num = algorithms.alph_pos(pad_list)
plaintext_num = []
for index in range(len(ciphertext_num)):
    inverse_mod = algorithms.modinverse((ciphertext_num[index] - pad_num[index]), 26)
    plaintext_num.append(inverse_mod)
plaintext = algorithms.num_alph(plaintext_num)
print("Decrypted plaintext:", "".join(plaintext))