def fonk1(x):
    if x < 2:
        return False
    for b1 in range(2, int(x ** 0.5) + 1):
        if x % b1 = = 0:
            return False
    return True
def fonk2():
    b2 = int(input("Enter first number: "))
    b3 = int(input("Enter second number: "))
    b4 = [b2, b3]
    b4.sort()
    b5 = [x for x in range(b4[0] + 1, b4[1]) if fonk1(x)]
    if len(b5) > 1:
        for b1 in range(0, len(b5) - 1, 3):
            b5[b1] = str(b5[b1]) + ":"
        for b1 in range(1, len(b5) - 1, 3):
            b5[b1] = str(b5[b1]) + "!"
        for b1 in range(2, len(b5) - 1, 3):
            b5[b1] = str(b5[b1]) + ","
        print("".join(map(str, b5)))
    elif len(b5) == 1:
        print("".join(map(str, b5)))
    else:
        print("No Primes")
if b6 = = "__main__":
    fonk2()