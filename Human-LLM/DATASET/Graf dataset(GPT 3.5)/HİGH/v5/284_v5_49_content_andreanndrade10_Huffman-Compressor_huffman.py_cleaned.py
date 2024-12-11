import os
from buildTree import firstRound
def fonk1():
    fonk2()
    fonk3()
def fonk2():
    print("\n\nAndre Luiz LourenÃ§o de Andrade - 14/0016295")
    print("Teoria da Informacao - Huffman Compressor\n")
def fonk3():
    b1 = input("Please enter a string or file to compress >>> ")
    if "-c" in b1:
        b2 = b1.split()[1]
        print(f"You chose {b2} as the file to be compressed...")
        fonk4(b2)
    else:
        print("\nThis function is not ready yet... Please choose a .txt file in your directory: " + os.getcwd())
        fonk3()
def fonk4(b2):
    with open(b2, "rb") as file:
        b3 = file.read()
        fonk5(b3)
def fonk5(b3):
    b4 = {}
    for char in b3:
        b4[char] = b4.get(char, 0) + 1
    fonk6(b4, b3)
def fonk6(b4, b3):
    b5 = b4.keys()
    b6 = len(b3)
    for key in b4:
        b4[key] /= b6
    b7 = sorted(b4.values(), reverse=True)
    firstRound(b7, b5)
if b8 = = "__main__":
    fonk1()