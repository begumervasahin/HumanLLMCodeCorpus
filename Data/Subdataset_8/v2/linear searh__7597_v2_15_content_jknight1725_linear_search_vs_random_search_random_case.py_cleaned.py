
from myFunctions import get_three_random_numbers, random_case_algorithm
import random
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
print("Number of Tries:", iterations)
print("Highest number of guesses in a try:", highest_attempt)
print("Lowest tries:", lowest_attempt)
print("Number of Correct tries:", iterations)
print("Average number of tries:", f"{attempts}/{iterations}: {attempts/iterations}")