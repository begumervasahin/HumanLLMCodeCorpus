
from myFunctions import get_three_random_numbers, worst_case_algorithm, all_1000_options
a1 = 10000
a2 = 0
a3 = 0
b1 = float('inf')
b2 = all_1000_options()
for iteration in range(a1):
    b3 = get_three_random_numbers()
    b4 = worst_case_algorithm(b2, b3)
    a2 += b4
    a3 = max(a3, b4)
    b1 = min(b1, b4)
print(f"Number of Tries: {a1}")
print(f"Highest number of guesses in a try: {a3}")
print(f"Lowest number of guesses: {b1}")
print(f"Number of Correct tries: {a1}")
print(f"Average number of tries: {a2}/{a1}: {a2 / a1}")