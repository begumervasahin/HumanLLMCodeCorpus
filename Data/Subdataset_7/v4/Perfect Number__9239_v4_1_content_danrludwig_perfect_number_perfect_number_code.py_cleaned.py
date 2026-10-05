import time
def fonk1(limit):
    b1 = []
    for number in range(1, limit):
        if fonk2(number):
            b1.append(number)
    return b1
def fonk2(number):
    a1 = 0
    for b2 in range(1, number):
        if number % b2 = = 0:
            a1 += b2
    return a1 = = number
if b3 = = "__main__":
    b4 = time.perf_counter()
    b5 = fonk1(10000)
    b6 = time.perf_counter()
    for number in b5:
        print(number)
    print(f"Calculation took {b6 - b4:.2f} seconds.")