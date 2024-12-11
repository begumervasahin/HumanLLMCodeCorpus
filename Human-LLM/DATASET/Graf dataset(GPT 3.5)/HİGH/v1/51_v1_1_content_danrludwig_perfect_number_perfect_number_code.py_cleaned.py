import time
def fonk1(a1):
    b1 = []
    for number in range(1, a1):
        b2 = sum([divisor for divisor in range(1, number) if number % divisor == 0])
        if b2 = = number:
            b1.append(number)
    return b1
a1 = 10000
b3 = time.perf_counter()
b1 = fonk1(a1)
b4 = time.perf_counter()
print("Perfect numbers below {}:".format(a1))
for num in b1:
    print(num)
print(f"Calculation took {b4 - b3:.6f} seconds.")