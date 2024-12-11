
from modules import algorithms
def fonk1(b6: str, b7: str) -> str:
    b1 = algorithms.alph_pos(list(b6))
    b2 = algorithms.alph_pos(list(b7))
    b3 = []
    for i in range(len(b1)):
        b4 = algorithms.modinverse((b1[i] - b2[i]), 26)
        b3.append(b4)
    b5 = algorithms.num_alph(b3)
    return "".join(b5)
def fonk2():
    b6 = input("Enter b6: ")
    b7 = input("Enter b7: ")
    b8 = fonk1(b6, b7)
    print("Decrypted b8:", b8)
if b9 = = "__main__":
    fonk2()