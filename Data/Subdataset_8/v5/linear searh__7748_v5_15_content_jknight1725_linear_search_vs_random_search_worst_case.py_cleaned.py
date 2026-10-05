
from myFunctions import get_three_random_numbers, worst_case_algorithm, all_1000_options
iterations = 10000
total_attempts = 0
highest_attempt = 0
lowest_attempt = float('inf')
options = all_1000_options()
for iteration in range(iterations):
    three_random_numbers = get_three_random_numbers()
    attempts = worst_case_algorithm(options, three_random_numbers)
    total_attempts += attempts
    highest_attempt = max(highest_attempt, attempts)
    lowest_attempt = min(lowest_attempt, attempts)
print(f"Number of Tries: {iterations}")
print(f"Highest number of guesses in a try: {highest_attempt}")
print(f"Lowest number of guesses: {lowest_attempt}")
print(f"Number of Correct tries: {iterations}")
print(f"Average number of tries: {total_attempts}/{iterations}: {total_attempts / iterations}")