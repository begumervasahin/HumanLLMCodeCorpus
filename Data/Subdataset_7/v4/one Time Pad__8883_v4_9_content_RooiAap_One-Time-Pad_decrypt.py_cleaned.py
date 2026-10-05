
from modules import algorithms
b1 = input("Enter b1: ")
b2 = input("Enter b2: ")
b3 = list(b1)
b4 = list(b2)
b5 = algorithms.alph_pos(b3)
b6 = algorithms.alph_pos(b4)
b7 = []
for index in range(len(b5)):
    b8 = algorithms.modinverse((b5[index] - b6[index]), 26)
    b7.append(b8)
b9 = algorithms.num_alph(b7)
print("Decrypted b9:", "".join(b9))