
from myFunctions import get_three_random_numbers, random_case_algorithm
a1 = 10000
a2 = 0
a3 = 0
b1 = float('inf')
b2 = get_three_random_numbers()
for _ in range(a1):
    b3 = random_case_algorithm(b2)
    a2 += b3
    a3 = max(a3, b3)
    b1 = min(b1, b3)
b4 = a2 / a1
print(f"Number of Tries: {a1}\n"
      f"Highest number of guesses in a try: {a3}\n"
      f"Lowest number of guesses: {b1}\n"
      f"Number of Correct tries: {a1}\n"
      f"Average number of guesses: {a2}/{a1}: {b4} ")