def fonk1(b3):
    b1 = [True] * (b3 + 1)
    a1 = 2
    while a1 * a1 <= b3:
        if b1[a1]:
            for i in range(a1 * 2, b3 + 1, a1):
                b1[i] = False
        a1 += 1
    return b1
def fonk2(b3, b1):
    print(f"Prime numbers from 2 to {b3}:")
    for x in range(2, b3):
        if b1[x]:
            print(x)
if b2 = = "__main__":
    print("Welcome to the prime number generator!")
    print("This program will print all prime numbers from 2 to b3.")
    b3 = int(input("Enter the value of b3: "))
    b1 = fonk1(b3)
    fonk2(b3, b1)