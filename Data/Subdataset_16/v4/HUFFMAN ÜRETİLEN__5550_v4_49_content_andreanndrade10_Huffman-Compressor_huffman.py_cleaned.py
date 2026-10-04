import os
from buildTree import firstRound
def fonk1():
    fonk2()
    b1 = fonk3()
    if b1.endswith(".txt"):
        b2 = fonk5(b1)
        b3 = fonk6(b2)
        b4 = fonk7(b3, b2)
        firstRound(b4, list(b3.keys()))
    else:
        fonk4()
def fonk2():
    print("\n\nAndre Luiz Lourenço de Andrade - 14/0016295")
    print("Teoria da Informação - Huffman Compressor\n")
def fonk3():
    return input("Please enter a string or a file path (e.g., '-c filename.txt') >>> ").strip()
def fonk4():
    print("\nThis function is not ready yet... Please choose a .txt file from your directory: " + os.getcwd())
    fonk1()
def fonk5(file_path):
    try:
        with open(file_path, "rb") as file:
            b5 = file.read()
        print(f"You chose {file_path} as the file to be compressed...")
        return b5
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        fonk1()
def fonk6(b5):
    b3 = {}
    for byte in b5:
        b3[byte] = b3.get(byte, 0) + 1
    return b3
def fonk7(b3, b5):
    b6 = len(b5)
    for key in b3:
        b3[key] /= b6
    b7 = sorted(b3.values(), reverse=True)
    return b7
if b8 = = "__main__":
    fonk1()