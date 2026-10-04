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
if b3 = = "__main__":
    while True:
        print("\n\n--- Vernam Cipher ---")
        b4 = input("Enter text to encrypt: ")
        b5 = fonk1(b4, b2)
        print("Cipher text: " + b5)
        b6 = fonk1(b5, b2)
        print("Decrypted text: " + b6)