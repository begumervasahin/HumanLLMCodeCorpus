import os
from ciphers import Caesar, Atbash, Affine, Keyword
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2():
    fonk1()
    print(
        "Welcome to the Secret Messages project for the Treehouse Techdegree.\n\n"
        "Available ciphers:\n"
        "- Caesar\n"
        "- Atbash\n"
        "- Affine\n"
        "- Keyword\n\n"
        "Enter 'QUIT' to exit the Secret Messages.\n"
    )
def fonk3():
    b2 = ['Caesar', 'Atbash', 'Affine', 'Keyword']
    while True:
        b3 = input("Which b3 would you like to use? ").capitalize()
        if b3 = = 'Quit':
            return False
        if b3 in b2:
            b4 = globals()[b3]
            b5 = fonk6()
            b6 = fonk7()
            return getattr(b4, b3)(b5, b6)
        print("Sorry, that's not a valid b3.\n")
def fonk4():
    return input("Enter the b10: ")
def fonk5():
    while True:
        b7 = input("Do you want to encode or decode the b10? ").lower()
        if b7 in ('encode', 'decode'):
            return b7
        print("Sorry, you have to enter 'encode' or 'decode'.\n")
def fonk6():
    while True:
        b5 = input("Enter a b5 number (leave blank for no b5): ").strip()
        if not b5:
            return b5
        if b5.isdigit():
            return b5
        print("Sorry, you have to enter a valid numeric b5 key.\n")
def fonk7():
    b7 = input("Encrypt in b6 of 5? [y/N]: ").lower()
    return b7 = = 'y'
def fonk8(b3, b7, b10):
    b8 = getattr(b3, b7)(b10)
    print("\nYour {}d b10 is: {}".format(b7, b8))
def fonk9():
    b9 = input("\nDo you want to encrypt or decrypt another b10 [Y/n]: ").strip()
    if b9.lower() != 'n':
        fonk10()
    else:
        print("Thanks for using Secret Messages. Goodbye!")
def fonk10():
    fonk2()
    b3 = fonk3()
    if b3:
        b10 = fonk4()
        b7 = fonk5()
        fonk8(b3, b7, b10)
        fonk9()
    else:
        print("Thanks for using Secret Messages. Goodbye!")
if b11 = = '__main__':
    fonk10()