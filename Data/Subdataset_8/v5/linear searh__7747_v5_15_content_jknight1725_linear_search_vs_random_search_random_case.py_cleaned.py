
from myFunctions import get_three_random_numbers, random_case_algorithm
ITERATIONS = 10000
total_attempts = 0
highest_attempt = 0
lowest_attempt = float('inf')
three_random_numbers = get_three_random_numbers()
for _ in range(ITERATIONS):
    attempts_this_iteration = random_case_algorithm(three_random_numbers)
    total_attempts += attempts_this_iteration
    highest_attempt = max(highest_attempt, attempts_this_iteration)
    lowest_attempt = min(lowest_attempt, attempts_this_iteration)
average_attempts = total_attempts / ITERATIONS
print(f"Number of Tries: {ITERATIONS}\n"
      f"Highest number of guesses in a try: {highest_attempt}\n"
      f"Lowest number of guesses: {lowest_attempt}\n"
      f"Number of Correct tries: {ITERATIONS}\n"
      f"Average number of guesses: {total_attempts}/{ITERATIONS}: {average_attempts} ")