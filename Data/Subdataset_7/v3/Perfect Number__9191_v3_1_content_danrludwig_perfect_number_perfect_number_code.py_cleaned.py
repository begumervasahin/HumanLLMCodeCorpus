import time
def fonk1(number):
    return sum([divisor for divisor in range(1, number
def fonk2(limit):
    b1 = []
    for number in range(1, limit):
        if fonk1(number) == number:
            b1.append(number)
    return b1
a1 = 10000
b2 = time.perf_counter()
b3 = fonk2(a1)
b4 = time.perf_counter()
print(f"Perfect numbers below {a1}:")
for perfect_number in b3:
    print(perfect_number)
print(f"Calculation took {b4 - b2:.6f} seconds.")