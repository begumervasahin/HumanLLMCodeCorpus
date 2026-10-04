import time
def fonk1(number):
    return [b1 for b1 in range(1, number) if number % b1 = = 0]
def fonk2(a1):
    b2 = []
    for number in range(1, a1):
        if sum(fonk1(number)) == number:
            b2.append(number)
    return b2
def fonk3():
    a1 = 10000
    b3 = time.time()
    b2 = fonk2(a1)
    for number in b2:
        print(number)
    b4 = time.time() - b3
    print(f"Time taken: {b4:.2f} seconds")
if b5 = = "__main__":
    fonk3()