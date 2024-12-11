import os
from buildTree import firstRound
print("\n\nAndre Luiz Lourenço de Andrade - 14/0016295")
print("Teoria da Informacao - Huffman Compressor\n")
b1 = []
def fonk1():
    fonk2()
def fonk2():
    b2 = input("Please enter a b4 or b3 to compress >>> ")
    if b2.find("-c") != -1:
        b3 = b2.split()[1]
        print("You chose", b3, "as the b3 to be compressed...")
        fonk4(b3)
        return b3
    else:
        b4 = b2
        fonk3(b4)
        return b4
def fonk3(b4):
    print("\nThis function is not ready yet... Please choose a .txt b3 in your directory: " + os.getcwd())
    fonk2()
def fonk4(b3):
    try:
        with open(b3, "rb") as f:
            b5 = f.read()
            fonk6(b5)
            return b5
    except FileNotFoundError:
        print("File not found. Please make sure the b3 exists.")
        fonk2()
def fonk5(contentFile):
    b6 = len(contentFile)
    return b6
def fonk6(contentFile):
    b7 = {}
    for i in contentFile:
        if i not in b7.keys():
            b7[i] = 1
        else:
            b7[i] += 1
    fonk7(b7, contentFile)
    global b1
    b1 = b7.keys()
    return b7
def fonk7(dictionary, contentFile):
    for key in dictionary:
        dictionary[key] /= len(contentFile)
    b8 = sorted(dictionary.values(), reverse=True)
    firstRound(b8, b1)
    return b8
if b9 = = "__main__":
    fonk1()