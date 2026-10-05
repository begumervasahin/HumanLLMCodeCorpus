
from myFunctions import *
ITERATIONS = 10000
total_attempts = 0
max_attempts = 0
min_attempts = float('inf')
options = all_1000_options()
for _ in range(ITERATIONS):
    random_numbers = get_three_random_numbers()
    attempts_needed = worst_case_algorithm(options, random_numbers)
    total_attempts += attempts_needed
    max_attempts = max(max_attempts, attempts_needed)
    min_attempts = min(min_attempts, attempts_needed)
average_attempts = total_attempts / ITERATIONS
print(f"Number of Tries: {ITERATIONS}\n"
      f"Highest number of guesses in a try: {max_attempts}\n"
      f"Lowest number of guesses: {min_attempts}\n"
      f"Number of Correct tries: {ITERATIONS}\n"
      f"Average number of guesses: {total_attempts}/{ITERATIONS}: {average_attempts}")