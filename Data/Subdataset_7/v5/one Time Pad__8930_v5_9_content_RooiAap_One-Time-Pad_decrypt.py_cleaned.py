
from modules import algorithms
def fonk1(b8, b9):
    b1 = list(b8)
    b2 = list(b9)
    b3 = algorithms.alph_pos(b1)
    b4 = algorithms.alph_pos(b2)
    b5 = []
    for ct_num, b4 in zip(b3, b4):
        b6 = algorithms.modinverse((ct_num - b4), 26)
        b5.append(b6)
    b7 = algorithms.num_alph(b5)
    return "".join(b7)
def fonk2():
    b8 = input("Enter b8: ")
    b9 = input("Enter b9: ")
    b10 = fonk1(b8, b9)
    print("Decrypted b7:", b10)
if b11 = = "__main__":
    fonk2()