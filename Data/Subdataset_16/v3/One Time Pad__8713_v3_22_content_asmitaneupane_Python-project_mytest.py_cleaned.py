def fonk1(text, key):
    b1 = []
    a1 = 0
    for char in text:
        b2 = chr(ord(char) ^ ord(key[a1]))
        b1.append(b2)
        a1 = (a1 + 1) % len(key)
    return ''.join(b1)
b3 = "cvwopslweinedvq9fnasdlkfn2"
def fonk2():
    while True:
        print("\n\n--- Vernam Cipher ---")
        b4 = input("Enter text to encrypt: ")
        b5 = fonk1(b4, b3)
        print("Cipher text:", b5)
        b6 = fonk1(b5, b3)
        print("Decrypted text:", b6)
if b7 = = "__main__":
    fonk2()