import os
from buildTree import firstRound
print("\n\nAndre Luiz Lourenço de Andrade - 14/0016295")
print("Teoria da Informacao - Huffman Compressor\n")
def fonk1():
    fonk2()
def fonk2():
    b1 = input("Please enter a string or file to compress >>> ")
    if "-c" in b1:
        b2 = b1.split()[1]
        print("You chose", b2, "as the file to be compressed...")
        fonk3(b2)
    else:
        print("\nThis function is not ready yet... Please choose a .txt file in your directory: " + os.getcwd())
        fonk2()
def fonk3(b2):
    try:
        with open(b2, "rb") as file:
            b3 = file.read()
            fonk4(b3)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        fonk2()
def fonk4(b3):
    b4 = fonk5(b3)
    b5 = list(b4.keys())
    b6 = fonk6(b4, b3)
    firstRound(b6, b5)
def fonk5(b3):
    b4 = {}
    for symbol in b3:
        if symbol not in b4:
            b4[symbol] = 1
        else:
            b4[symbol] += 1
    return b4
def fonk6(b4, b3):
    b7 = len(b3)
    b6 = [b4[symbol] / b7 for symbol in b4]
    b6.sort(b8 = True)
    return b6
if b9 = = "__main__":
    fonk1()