from myFunctions import *
iterations = 10000
attempts = 0
highest_attempt = 0
lowest_attempt = 1000
options = all_1000_options()
for x in range(iterations):
    three_random_numbers = get_three_random_numbers()
    iteration = worst_case_algorithm(options, three_random_numbers)
    attempts += iteration
    highest_attempt = max(iteration, highest_attempt)
    lowest_attempt = min(iteration, lowest_attempt)
print(f"Number of Tries: {iterations}\n"
      f"Highest number of guesses in a try: {highest_attempt}\n"
      f"Lowest number of guesses: {lowest_attempt}\n"
      f"Number of Correct tries: {iterations}\n"
      f"Average number of guesses: {attempts}/{iterations}: {attempts/iterations} ")