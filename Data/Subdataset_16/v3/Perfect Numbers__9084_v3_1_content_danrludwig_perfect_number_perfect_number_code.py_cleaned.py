import time
def fonk1(a1):
    b1 = []
    for number in range(1, a1):
        b2 = sum(divisor for divisor in range(1, number) if number % divisor == 0)
        if b2 = = number:
            b1.append(number)
    return b1
def fonk2():
    a1 = 10000
    b3 = time.time()
    b1 = fonk1(a1)
    print("Perfect numbers below {}:".format(a1))
    for number in b1:
        print(number)
    b4 = time.time() - b3
    print(f"Time taken: {b4:.2f} seconds")
if b5 = = '__main__':
    fonk2()
