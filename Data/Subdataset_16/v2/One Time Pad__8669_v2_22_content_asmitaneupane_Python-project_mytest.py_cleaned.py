def fonk1(text, key):
    b1 = ""
    a1 = 0
    for char in text:
        b1 += chr(ord(char) ^ ord(key[a1]))
        a1 += 1
        if a1 = = len(key):
            a1 = 0
    return b1
b2 = "cvwopslweinedvq9fnasdlkfn2"
def fonk2():
    while True:
        print("\n\n--- Vernam Cipher ---")
        b3 = input("Enter text to encrypt: ")
        b4 = fonk1(b3, b2)
        print("Cipher text:", b4)
        b5 = fonk1(b4, b2)
        print("Decrypted text:", b5)
if b6 = = "__main__":
    fonk2()