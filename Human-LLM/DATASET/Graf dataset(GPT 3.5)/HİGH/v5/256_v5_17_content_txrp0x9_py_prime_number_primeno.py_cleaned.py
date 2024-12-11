def fonk1():
    print("Welcome to the prime number generator.")
    print("This program will print all prime numbers from 2 to b1.")
    b1 = int(input("Enter the value of b1: "))
    b2 = [True for _ in range(b1 + 1)]
    a1 = 2
    while a1 * a1 <= b1:
        if b2[a1]:
            for multiple in range(a1 * 2, b1 + 1, a1):
                b2[multiple] = False
        a1 += 1
    b3 = [x for x in range(2, b1) if b2[x]]
    return b3
b3 = fonk1()
print("Prime numbers from 2 to", b1, "are:")
for prime_number in b3:
    print(prime_number)