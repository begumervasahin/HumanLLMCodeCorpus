from myFunctions import *
import random
iterations = 10000
attempts = 0
highest_attempt = 0
lowest_attempt = 1000
three_random_numbers = get_three_random_numbers()
for x in range(iterations):
    iteration = random_case_algorithm(three_random_numbers)
    attempts += iteration
    highest_attempt = max(iteration, highest_attempt)
    lowest_attempt = min(iteration, lowest_attempt)
print(f"Number of Tries: {iterations}\n"
      f"Highest number of guesses in a try: {highest_attempt}\n"
      f"Lowest tries: {lowest_attempt}\n"
      f"Number of Correct tries: {iterations}\n"
      f"Average number of tries: {attempts}/{iterations}: {attempts/iterations} ")