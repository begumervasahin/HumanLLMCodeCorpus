def fonk1(num):
    if num <= 1:
        return False
    for b1 in range(2, int(num ** 0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(prime_list):
    b2 = []
    for b1, prime in enumerate(prime_list):
        if b1 % b3 = = 0:
            b2.append(str(prime) + ":")
        elif b1 % b3 = = 1:
            b2.append(str(prime) + "!")
        elif b1 % b3 = = 2:
            b2.append(str(prime) + ",")
    return b2
def fonk3():
    b4 = int(input("Enter first number: "))
    b5 = int(input("Enter second number: "))
    b6 = [b4, b5]
    b6.sort()
    b7 = [x for x in range(b6[0] + 1, b6[1]) if fonk1(x)]
    if b7:
        b2 = fonk2(b7)
        print("".join(b2))
    else:
        print("No Primes")
if b8 = = "__main__":
    fonk3()