def fonk1(b3):
    b1 = [True for _ in range(b3 + 1)]
    a1 = 2
    while a1 * a1 <= b3:
        if b1[a1]:
            for i in range(a1 * a1, b3 + 1, a1):
                b1[i] = False
        a1 += 1
    b2 = [a1 for a1 in range(2, b3 + 1) if b1[a1]]
    return b2
def fonk2():
    print("Welcome random tester, this program will print all the prime numbers from 2 to b3")
    b3 = int(input("Enter b3: "))
    b2 = fonk1(b3)
    print("Prime numbers up to", b3, "are:")
    for prime in b2:
        print(prime)
if b4 = = "__main__":
    fonk2()