import os
from buildTree import firstRound
print("\n\nAndre Luiz LourenÃ§o de Andrade - 14/0016295")
print("Teoria da Informacao - Huffman Compressor\n")
b1 = []
def fonk1():
    fonk2()
def fonk2():
    b2 = input("Please enter a b4 or b3 to compress >>> ")
    if "-c" in b2:
        b3 = b2.split()[1]
        print("You chose", b3, "as the b3 to be compressed...")
        fonk4(b3)
    else:
        b4 = b2
        fonk3(b4)
def fonk3(b4):
    print("\nThis function is not ready yet... Please choose a .txt b3 in your directory: " + os.getcwd())
    fonk2()
def fonk4(b3):
    with open(b3, "rb") as f:
        b5 = f.read()
        fonk6(b5)
def fonk5(contentFile):
    return len(contentFile)
def fonk6(contentFile):
    b6 = {}
    for i in contentFile:
        if i not in b6.keys():
            b6[i] = 1
        else:
            b6[i] += 1
    fonk7(b6, contentFile)
    global b1
    b1 = b6.keys()
def fonk7(dictionary, contentFile):
    global b1
    for key in dictionary:
        dictionary[key] /= len(contentFile)
    b7 = sorted(dictionary.values(), reverse=True)
    firstRound(b7, b1)
fonk1()