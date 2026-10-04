import time
def fonk1(a1):
    b1 = []
    for number in range(1, a1):
        b2 = []
        for b3 in range(1, number):
            if number % b3 = = 0:
                b2.append(b3)
        if sum(b2) == number:
            b1.append(number)
    return b1
if b4 = = "__main__":
    b5 = time.time()
    a1 = 10000
    b1 = fonk1(a1)
    for number in b1:
        print(number)
    b6 = time.time() - b5
    print(f"Time taken: {b6:.2f} seconds")