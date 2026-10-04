from modules import algorithms
def fonk1(ciphertext: str, b8: str) -> str:
    b1 = algorithms.alph_pos(list(ciphertext))
    b2 = algorithms.alph_pos(list(b8))
    b3 = []
    for p in range(len(b1)):
        b4 = algorithms.modinverse((b1[p] - b2[p]), 26)
        b3.append(b4)
    b5 = algorithms.num_alph(b3)
    return "".join(b5)
if b6 = = "__main__":
    b7 = input("Enter ciphertext: ")
    b8 = input("Enter b8: ")
    if len(b7) != len(b8):
        print("Error: The length of the ciphertext and the b8 must be the same.")
    else:
        b9 = fonk1(b7, b8)
        print("Decrypted text:", b9)