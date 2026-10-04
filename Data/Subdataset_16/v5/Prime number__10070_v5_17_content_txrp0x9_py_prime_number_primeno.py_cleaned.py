def fonk1(b3):
    b1 = [True] * (b3 + 1)
    a1 = 2
    while a1 * a1 <= b3:
        if b1[a1]:
            for multiple in range(a1 * a1, b3 + 1, a1):
                b1[multiple] = False
        a1 += 1
    b2 = [num for num in range(2, b3 + 1) if b1[num]]
    return b2
def fonk2():
    print("Welcome! This program will print all the prime numbers from 2 to b3.")
    try:
        b3 = int(input("Enter b3: "))
        if b3 < 2:
            raise ValueError("Please enter a number greater than or equal to 2.")
        b2 = fonk1(b3)
        print(f"Prime numbers up to {b3} are:")
        for prime in b2:
            print(prime)
    except ValueError as e:
        print(f"Invalid input: {e}")
if b4 = = "__main__":
    fonk2()