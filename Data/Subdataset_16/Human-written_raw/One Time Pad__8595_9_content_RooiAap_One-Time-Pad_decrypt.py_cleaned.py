from modules import algorithms
b1 = input("Enter ciphertext: ")
b2 = input("Enter b2: ")
b3 = algorithms.alph_pos(list(b1))
b4 = algorithms.alph_pos(list(b2))
b5 = []
for p in range(len(b3)):
    b6 = algorithms.modinverse((b3[p] - b4[p]), 26)
    b5.append(b6)
b7 = algorithms.num_alph(b5)
print("".join(b7))