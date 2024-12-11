from myFunctions import *
a1 = 10000
a2 = 0
a3 = 0
a4 = 1000
b1 = get_three_random_numbers()
for x in range(a1):
    b2 = random_case_algorithm(b1)
    a2 += b2
    a3 = b2 if b2 > a3 else a3
    a4 = b2 if b2 < a4 else a4
print(f"Number of Tries: {a1}\n"
      f"Highest number of guess in a try: {a3}\n"
      f"Lowest tries: {a4}\n"
      f"Number of Correct tries: {a1}\n"
      f"Average number of tries: {a2}/{a1}: {a2/a1} ")