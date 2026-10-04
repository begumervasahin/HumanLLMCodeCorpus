import os
from buildTree import firstRound
def fonk1():
    fonk2()
    b1 = fonk3()
    if fonk4(b1):
        b2 = fonk5(b1)
        b3 = fonk6(b2)
    else:
        b3 = fonk7()
    if b3:
        b4 = fonk8(b3)
        fonk9(b4, len(b3))
def fonk2():
    print("\n\nAndre Luiz Lourenço de Andrade - 14/0016295")
    print("Teoria da Informação - Huffman Compressor\n")
def fonk3():
    return input("Please enter a string or the file path to compress (e.g., '-c <b2>') >>> ")
def fonk4(b1):
    return b1.startswith("-c")
def fonk5(b1):
    b5 = b1.split(maxsplit=1)
    return b5[1] if len(b5) > 1 else ""
def fonk6(b2):
    if not b2:
        print("Error: No file path provided.")
        return None
    try:
        with open(b2, "rb") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{b2}' not found.")
        return None
def fonk7():
    print(f"\nThis feature is not yet implemented. Please select a .txt file from your directory: {os.getcwd()}")
    return None
def fonk8(b3):
    b4 = {}
    for byte in b3:
        b4[byte] = b4.get(byte, 0) + 1
    return b4
def fonk9(b4, total_size):
    b6 = {byte: count / total_size for byte, count in b4.items()}
    b7 = sorted(b6.values(), reverse=True)
    b8 = list(b6.keys())
    firstRound(b7, b8)
if b9 = = "__main__":
    fonk1()