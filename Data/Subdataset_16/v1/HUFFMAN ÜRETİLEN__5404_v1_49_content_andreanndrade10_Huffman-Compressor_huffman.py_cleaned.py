import os
from buildTree import firstRound
def fonk1():
    print("\n\nAndre Luiz Lourenço de Andrade - 14/0016295")
    print("Teoria da Informação - Huffman Compressor\n")
    b1 = fonk2()
    if fonk3(b1):
        b2 = fonk4(b1)
        print(f"You chose {b2} as the file to be compressed...")
        b3 = fonk5(b2)
    else:
        b3 = fonk6()
    if b3:
        b4 = fonk7(b3)
        fonk8(b4, b3)
def fonk2():
    return input("Please enter a string or file to compress >>> ")
def fonk3(b1):
    return "-c" in b1
def fonk4(b1):
    return b1.split()[1]
def fonk5(b2):
    try:
        with open(b2, "rb") as file:
            b3 = file.read()
            return b3
    except FileNotFoundError:
        print(f"Error: File '{b2}' not found.")
        return None
def fonk6():
    print("\nThis function is not ready yet... Please choose a .txt file in your directory: " + os.getcwd())
    return fonk2()
def fonk7(b3):
    b5 = {}
    for byte in b3:
        b5[byte] = b5.get(byte, 0) + 1
    return b5
def fonk8(b5, b3):
    b6 = len(b3)
    for key in b5:
        b5[key] /= b6
    b7 = sorted(b5.values(), reverse=True)
    b8 = list(b5.keys())
    firstRound(b7, b8)
if b9 = = "__main__":
    fonk1()