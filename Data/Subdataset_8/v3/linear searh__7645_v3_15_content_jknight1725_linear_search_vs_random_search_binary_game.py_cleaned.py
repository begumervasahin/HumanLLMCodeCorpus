def calculate_midpoint(lower_bound, upper_bound):
    return (lower_bound + upper_bound)
def display_computer_guess(guess):
    print(f"The computer's guess is: {guess}")
def get_user_feedback():
    return input("Is the guess too high (h), too low (l), or correct (c)? ")
def adjust_guess_range(feedback, current_guess, lower_bound, upper_bound):
    if feedback == 'h':
        return lower_bound, current_guess - 1
    elif feedback == 'l':
        return current_guess + 1, upper_bound
    else:
        return current_guess, current_guess
def congratulate_on_success(final_guess, total_attempts):
    print(f"\nCongratulations! The computer guessed {final_guess} in {total_attempts} attempts.")
from myFunctions import *
attempts = 1
lower_bound = 0
upper_bound = 1000
current_guess = calculate_midpoint(lower_bound, upper_bound)
display_computer_guess(current_guess)
feedback = get_user_feedback()
while feedback != 'c':
    lower_bound, upper_bound = adjust_guess_range(feedback, current_guess, lower_bound, upper_bound)
    current_guess = calculate_midpoint(lower_bound, upper_bound)
    attempts += 1
    display_computer_guess(current_guess)
    feedback = get_user_feedback()
congratulate_on_success(current_guess, attempts)