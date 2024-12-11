
from myFunctions import get_three_random_numbers, random_case_algorithm
import random
a1 = 10000
a2 = 0
a3 = 0
a4 = 1000
b1 = get_three_random_numbers()
for x in range(a1):
    b2 = random_case_algorithm(b1)
    a2 += b2
    if b2 > a3:
        a3 = b2
    if b2 < a4:
        a4 = b2
print("Number of Tries:", a1)
print("Highest number of guesses in a try:", a3)
print("Lowest tries:", a4)
print("Number of Correct tries:", a1)
print("Average number of tries:", f"{a2}/{a1}: {a2/a1}")