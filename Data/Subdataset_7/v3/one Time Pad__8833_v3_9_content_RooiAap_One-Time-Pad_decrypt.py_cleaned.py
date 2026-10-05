from modules import algorithms
def fonk1(b6: str, b7: str) -> str:
    b1 = algorithms.alph_pos(list(b6))
    b2 = algorithms.alph_pos(list(b7))
    b3 = []
    for cipher_pos, pad_pos in zip(b1, b2):
        b4 = algorithms.modinverse((cipher_pos - pad_pos), 26)
        b3.append(b4)
    b5 = algorithms.num_alph(b3)
    return "".join(b5)
def fonk2():
    b6 = input("Enter the b6: ")
    b7 = input("Enter the b7: ")
    b8 = fonk1(b6, b7)
    print("Decrypted b8:", b8)
if b9 = = "__main__":
    fonk2()