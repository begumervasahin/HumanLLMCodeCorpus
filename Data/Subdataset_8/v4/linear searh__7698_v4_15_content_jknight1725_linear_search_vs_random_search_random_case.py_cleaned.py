
from myFunctions import get_three_random_numbers, random_case_algorithm
iterations = 10000
attempts = 0
highest_attempt = 0
lowest_attempt = 1000
three_random_numbers = get_three_random_numbers()
for x in range(iterations):
    iteration = random_case_algorithm(three_random_numbers)
    attempts += iteration
    if iteration > highest_attempt:
        highest_attempt = iteration
    if iteration < lowest_attempt:
        lowest_attempt = iteration
print(f"Number of Tries: {iterations}\n"
      f"Highest number of guesses in a try: {highest_attempt}\n"
      f"Lowest number of guesses: {lowest_attempt}\n"
      f"Number of Correct tries: {iterations}\n"
      f"Average number of guesses: {attempts}/{iterations}: {attempts/iterations} ")