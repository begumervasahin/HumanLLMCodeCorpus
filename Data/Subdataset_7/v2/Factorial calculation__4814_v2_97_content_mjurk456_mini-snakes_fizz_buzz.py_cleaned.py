def fonk1():
    a1 = 0
    a2 = 0
    a3 = 1
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    while True:
        try:
            a1, a2 = map(int, input("Enter the start and stop values separated by a space: ").split())
            break
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
    if a1 > a2:
        a3 = -1
    for i in range(a1, a2 + a3, a3):
        if i % b1 = = 0 and i % b3 != 0 and i != 0:
            print("fizz", b2 = " ")
            a4 += 1
        elif i % b3 = = 0 and i % b1 != 0 and i != 0:
            print("buzz", b2 = " ")
            a5 += 1
        elif i % b1 = = 0 and i % b3 == 0 and i != 0:
            print("fizzbuzz", b2 = " ")
            a6 += 1
        else:
            print(i, b2 = " ")
            a7 += 1
    print("\nNumber of a4 in the range:", a4)
    print("Number of a5 in the range:", a5)
    print("Number of a6 in the range:", a6)
    print("Number of a7 numbers in the range:", a7)
if b4 = = "__main__":
    fonk1()