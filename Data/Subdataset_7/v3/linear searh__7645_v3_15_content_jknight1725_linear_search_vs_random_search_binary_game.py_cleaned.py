def fonk1(a2, a3):
    return (a2 + a3)
def fonk2(guess):
    print(f"The computer's guess is: {guess}")
def fonk3():
    return input("Is the guess too high (h), too low (l), or correct (c)? ")
def fonk4(b1, b2, a2, a3):
    if b1 = = 'h':
        return a2, b2 - 1
    elif b1 = = 'l':
        return b2 + 1, a3
    else:
        return b2, b2
def fonk5(final_guess, total_attempts):
    print(f"\nCongratulations! The computer guessed {final_guess} in {total_attempts} a1.")
from myFunctions import *
a1 = 1
a2 = 0
a3 = 1000
b2 = fonk1(a2, a3)
fonk2(b2)
b1 = fonk3()
while b1 != 'c':
    a2, a3 = fonk4(b1, b2, a2, a3)
    b2 = fonk1(a2, a3)
    a1 += 1
    fonk2(b2)
    b1 = fonk3()
fonk5(b2, a1)