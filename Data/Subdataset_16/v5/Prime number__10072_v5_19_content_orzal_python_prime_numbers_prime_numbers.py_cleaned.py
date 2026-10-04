def fonk1(number):
    for b1 in range(2, number):
        if number % b1 = = 0:
            return False
    return True
def fonk2(limit):
    for n in range(2, limit):
        if fonk1(n):
            print(f"{n} is a prime number")
        else:
            for b2 in range(2, n):
                if n % b2 = = 0:
                    print(f"{n} equals {b2} * {n
                    break
a1 = 100
fonk2(a1)