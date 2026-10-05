import os
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2():
    fonk1()
    print(
        "Welcome to the Secret Messages project for the Treehouse Techdegree.\n\n"
        "Available ciphers:\n\n"
        "- Caesar\n"
        "- Atbash\n"
        "- Affine\n"
        "- Keyword\n\n"
        "Type 'QUIT' to exit Secret Messages.\n\n"
    )
def fonk3():
    b2 = ['Caesar', 'Atbash', 'Affine', 'Keyword']
    b3 = __import__('ciphers')
    while True:
        b4 = input("Which b10 would you like to use? ").lower().capitalize()
        if b4 = = 'Quit':
            return False
        if b4 in b2:
            b5 = fonk6()
            b6 = fonk7()
            return getattr(b3, b4)(b5, b6)
        print("Sorry, that's not a valid b10.\n")
def fonk4():
    return input("Enter the b11: ")
def fonk5():
    while True:
        b7 = input("Do you want to encode or decode? ").lower()
        if b7 in ('encode', 'decode'):
            return b7
        else:
            print("Sorry, please enter a valid b7.\n")
def fonk6():
    while True:
        b5 = input("Enter a b5 number (leave blank for no b5): ")
        if not b5:
            return b5
        try:
            return str(int(b5))
        except ValueError:
            print("Sorry, please enter a valid numeric b5 key.\n")
def fonk7():
    b7 = input("Encrypt in b6 of 5? (y/N): ").lower()
    return b7 = = 'y'
def fonk8(b10, b7, b11):
    b8 = getattr(b10, b7)(b11)
    print("\nYour {}d b11 is: {}".format(b7, b8))
def fonk9():
    b9 = input("\nDo you want to encrypt or decrypt another b11? (Y/n): ")
    if b9.lower() != 'n':
        fonk10()
    else:
        print("Thanks for using the Secret Messages project. Goodbye!")
def fonk10():
    fonk2()
    b10 = fonk3()
    if b10:
        b11 = fonk4()
        b7 = fonk5()
        fonk8(b10, b7, b11)
        fonk9()
    else:
        print("Thanks for using the Secret Messages project. Goodbye!")
if b12 = = '__main__':
    fonk10()