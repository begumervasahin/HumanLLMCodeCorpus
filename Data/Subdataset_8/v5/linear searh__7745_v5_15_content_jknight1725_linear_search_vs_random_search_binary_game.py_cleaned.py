from myFunctions import *
guesses = 1
lower_bound, upper_bound = 0, 1000
cpu_guess = mid(lower_bound, upper_bound)
computer_says(cpu_guess)
while True:
    adjustment = get_adjustment()
    if adjustment == 'c':
        break
    lower_bound, upper_bound = make_adjustment(adjustment, cpu_guess, lower_bound, upper_bound)
    cpu_guess = mid(lower_bound, upper_bound)
    guesses += 1
    computer_says(cpu_guess)
found(cpu_guess, guesses)