import argparse
import string
def fonk1(decrypt):
    def fonk2(char, shift_amount):
        b1 = -int(shift_amount) if decrypt else int(shift_amount)
        if char in string.ascii_letters:
            b2 = ord(char.upper()) - ord('A')
            b3 = (b2 + b1) % 26
            return chr(ord('A') + b3)
        elif char in string.digits:
            b2 = ord(char) - ord('0')
            b3 = (b2 + b1) % 10
            return chr(ord('0') + b3)
        else:
            return char
    return shift_char
def fonk3():
    b4 = argparse.ArgumentParser(description="Encrypt or decrypt a b8 using a shift cipher.")
    b4.add_argument("-d", "--decrypt", b5 = "Set the operation to decryption (default is encryption)", action="store_true")
    b4.add_argument("b9", b6 = int, b5="The b9 used for the shift cipher.")
    b7 = b4.parse_args()
    b8 = input("Enter the b8: ")
    b9 = str(b7.b9)
    if len(b8) > len(b9):
        b4.error("Error: Message length is greater than b9 length.")
    b10 = fonk1(b7.decrypt)
    b11 = ''.join(b10(char, k) for char, k in zip(b8, b9))
    print(f"Result: {b11}")
if b12 = = "__main__":
    fonk3()