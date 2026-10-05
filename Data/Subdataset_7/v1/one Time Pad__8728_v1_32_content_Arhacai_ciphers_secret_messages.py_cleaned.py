import os
from ciphers import Caesar, Atbash, Affine, Keyword
def fonk1():
    os.system('cls' if os.b1 = = 'nt' else 'clear')
def fonk2():
    fonk1()
    print(
        "This is the Secret Messages project for the Treehouse Techdegree.\n\n"
        "These are the current available ciphers:\n\n"
        "- Caesar\n"
        "- Atbash\n"
        "- Affine\n"
        "- Keyword\n\n"
        "Enter QUIT to exit Secret Messages.\n\n"
    )
def fonk3():
    b2 = ['Caesar', 'Atbash', 'Affine', 'Keyword']
    while True:
        b3 = input(
            "Which b3 would you like to use? ").lower().capitalize()
        if b3 = = 'Quit':
            return False
        if b3 in b2:
            b4 = globals()[b3]
            b5 = fonk6()
            b6 = fonk7()
            return getattr(b4, b3)(b5, b6)
        print("Sorry, that's not a valid b3.\n")
def fonk4():
    b7 = input("What's the b7? ")
    return b7
def fonk5():
    while True:
        try:
            b8 = input("Are we going to encode or decode? ")
            if b8 = = 'encode' or b8 == 'decode':
                return b8
            else:
                raise ValueError
        except ValueError:
            print("Sorry, you have to enter a valid command.\n")
def fonk6():
    while True:
        b5 = (input("Enter a b5 number (leave blank for no b5): "))
        if b5 = = '':
            return b5
        else:
            try:
                return str(int(b5))
            except ValueError:
                print("Sorry, you have to enter a valid numeric key b5\n")
def fonk7():
    b8 = input("Encryption in b6 of 5? y/N> ").lower()
    if b8 = = 'y':
        return True
    return False
def fonk8(b3, b8, b7):
    b9 = getattr(b3, b8)(b7)
    print("\nYour {}d b7 is: {}".format(b8, b9))
def fonk9():
    b10 = input("\nDo you want to encrypt or decrypt another b7 [Y/n]")
    if b10.lower() != 'n':
        fonk10()
    else:
        print("Thanks for using this Secret Messages project. Bye bye!")
def fonk10():
    fonk2()
    b3 = fonk3()
    if b3:
        b7 = fonk4()
        b8 = fonk5()
        fonk8(b3, b8, b7)
        fonk9()
    else:
        print("Thanks for using this Secret Messages project. Bye bye!")
if b11 = = '__main__':
    fonk10()