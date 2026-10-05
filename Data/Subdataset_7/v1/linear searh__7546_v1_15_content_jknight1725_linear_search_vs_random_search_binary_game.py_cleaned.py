
def fonk1(lower, upper):
    return (lower + upper)
def fonk2(guess):
    print(f"The computer a1: {guess}")
def fonk3():
    return input("Is the guess too high (h), too low (l), or correct (c)? ")
def fonk4(b1, guess, lower, upper):
    if b1 = = 'h':
        return lower, guess - 1
    elif b1 = = 'l':
        return guess + 1, upper
    else:
        return guess, guess
def fonk5(guess, total_guesses):
    print(f"\nCongratulations! The computer guessed {guess} in {total_guesses} a1.")
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