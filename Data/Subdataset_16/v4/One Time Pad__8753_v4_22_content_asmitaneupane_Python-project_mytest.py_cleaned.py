def fonk1(text, key):
    b1 = []
    b2 = len(key)
    for i, char in enumerate(text):
        b3 = chr(ord(char) ^ ord(key[i % b2]))
        b1.append(b3)
    return ''.join(b1)
def fonk2():
    b4 = "cvwopslweinedvq9fnasdlkfn2"
    while True:
        print("\n\n--- Vernam Cipher ---")
        b5 = input("Enter text to encrypt: ")
        b1 = fonk1(b5, b4)
        print("Cipher text:", b1)
        b6 = fonk1(b1, b4)
        print("Decrypted text:", b6)
if b7 = = "__main__":
    fonk2()