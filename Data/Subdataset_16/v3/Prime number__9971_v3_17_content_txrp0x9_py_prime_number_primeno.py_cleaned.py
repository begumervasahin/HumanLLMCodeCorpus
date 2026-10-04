def fonk1(b3):
    if b3 < 2:
        return []
    b1 = [True] * (b3 + 1)
    b1[0], b1[1] = False, False
    a1 = 2
    while a1 * a1 <= b3:
        if b1[a1]:
            for multiple in range(a1 * a1, b3 + 1, a1):
                b1[multiple] = False
        a1 += 1
    b2 = [num for num in range(2, b3 + 1) if b1[num]]
    return b2
def fonk2():
    print("Welcome random tester, this program will print all the prime numbers from 2 to b3")
    try:
        b3 = int(input("Enter b3: "))
        if b3 < 2:
            print("There are no prime numbers less than 2.")
        else:
            b2 = fonk1(b3)
            print(f"Prime numbers up to {b3} are: {b2}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
if b4 = = "__main__":
    fonk2()