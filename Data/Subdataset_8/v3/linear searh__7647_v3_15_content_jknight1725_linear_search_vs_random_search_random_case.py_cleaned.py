
from myFunctions import get_three_random_numbers, random_case_algorithm
import random
NUM_ITERATIONS = 10000
INITIAL_LOWEST_ATTEMPT = float('inf')
INITIAL_HIGHEST_ATTEMPT = 0
total_attempts = 0
highest_attempt = INITIAL_HIGHEST_ATTEMPT
lowest_attempt = INITIAL_LOWEST_ATTEMPT
three_random_numbers = get_three_random_numbers()
for _ in range(NUM_ITERATIONS):
    iteration = random_case_algorithm(three_random_numbers)
    total_attempts += iteration
    highest_attempt = max(iteration, highest_attempt)
    lowest_attempt = min(iteration, lowest_attempt)
print("Number of Tries:", NUM_ITERATIONS)
print("Highest number of guesses in a try:", highest_attempt)
print("Lowest tries:", lowest_attempt)
print("Number of Correct tries:", NUM_ITERATIONS)
print("Average number of tries:", f"{total_attempts}/{NUM_ITERATIONS}: {total_attempts/NUM_ITERATIONS}")