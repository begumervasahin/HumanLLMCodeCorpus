import time
def fonk1(limit):
    b1 = []
    for number in range(1, limit):
        a1 = 0
        for b2 in range(1, number
            if number % b2 = = 0:
                a1 += b2
        if a1 = = number:
            b1.append(number)
    return b1
a2 = 10000
b3 = time.perf_counter()
b4 = fonk1(a2)
b5 = time.perf_counter()
print(f"Perfect numbers below {a2}:")
for perfect_number in b4:
    print(perfect_number)
print(f"Calculation took {b5 - b3:.6f} seconds.")