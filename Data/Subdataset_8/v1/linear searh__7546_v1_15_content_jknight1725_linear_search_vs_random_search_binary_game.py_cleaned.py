
def mid(lower, upper):
    return (lower + upper)
def computer_says(guess):
    print(f"The computer guesses: {guess}")
def get_adjustment():
    return input("Is the guess too high (h), too low (l), or correct (c)? ")
def make_adjustment(adjustment, guess, lower, upper):
    if adjustment == 'h':
        return lower, guess - 1
    elif adjustment == 'l':
        return guess + 1, upper
    else:
        return guess, guess
def found(guess, total_guesses):
    print(f"\nCongratulations! The computer guessed {guess} in {total_guesses} guesses.")
from myFunctions import *
guesses = 1
lower_bound = 0
upper_bound = 1000
cpu_guess = mid(lower_bound, upper_bound)
computer_says(cpu_guess)
adjustment = get_adjustment()
while adjustment != 'c':
    lower_bound, upper_bound = make_adjustment(adjustment, cpu_guess, lower_bound, upper_bound)
    cpu_guess = mid(lower_bound, upper_bound)
    guesses += 1
    computer_says(cpu_guess)
    adjustment = get_adjustment()
found(cpu_guess, guesses)