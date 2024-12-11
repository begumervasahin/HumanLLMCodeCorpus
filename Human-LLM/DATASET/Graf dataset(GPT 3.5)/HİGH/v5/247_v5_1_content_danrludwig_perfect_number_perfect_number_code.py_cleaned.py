import time
def fonk1(limit):
    return [number for number in range(1, limit) if fonk2(number)]
def fonk2(number):
    if number < 2:
        return False
    a1 = 1
    for b1 in range(2, int(number**0.5) + 1):
        if number % b1 = = 0:
            a1 += b1
            if b1 != number
                a1 += number
    return a1 = = number
if b2 = = "__main__":
    b3 = time.perf_counter()
    b4 = fonk1(10000)
    for number in b4:
        print(number)
    b5 = time.perf_counter()
    print(f"Calculation took {b5 - b3:.2f} seconds.")