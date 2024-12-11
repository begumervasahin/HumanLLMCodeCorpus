
from myFunctions import get_three_random_numbers, random_case_algorithm
import random
a1 = 10000
b1 = float('inf')
a2 = 0
a3 = 0
b2 = a2
b3 = b1
b4 = get_three_random_numbers()
for _ in range(a1):
    b5 = random_case_algorithm(b4)
    a3 += b5
    b2 = max(b5, b2)
    b3 = min(b5, b3)
print("Number of Tries:", a1)
print("Highest number of guesses in a try:", b2)
print("Lowest tries:", b3)
print("Number of Correct tries:", a1)
print("Average number of tries:", f"{a3}/{a1}: {a3/a1}")