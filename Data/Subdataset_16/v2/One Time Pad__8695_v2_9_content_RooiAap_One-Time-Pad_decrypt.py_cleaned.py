from modules import algorithms
def fonk1(ciphertext: str, b6: str) -> str:
    b1 = algorithms.alph_pos(list(ciphertext))
    b2 = algorithms.alph_pos(list(b6))
    b3 = [
        algorithms.modinverse((b1[i] - b2[i]), 26)
        for i in range(len(b1))
    ]
    b4 = algorithms.num_alph(b3)
    return "".join(b4)
def fonk2():
    b5 = input("Enter ciphertext: ")
    b6 = input("Enter b6: ")
    if len(b5) != len(b6):
        print("Error: The length of the ciphertext and the b6 must be the same.")
    else:
        b7 = fonk1(b5, b6)
        print("Decrypted text:", b7)
if b8 = = "__main__":
    fonk2()