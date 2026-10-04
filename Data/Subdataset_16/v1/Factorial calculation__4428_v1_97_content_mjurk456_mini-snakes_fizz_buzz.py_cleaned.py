def fonk1():
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    while True:
        try:
            min_limit, b1 = [int(a) for a in input("Input start and stop values for counting (separated by space): ").split()]
            break
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
    b2 = 1 if min_limit <= b1 else -1
    for i in range(min_limit, b1 + b2, b2):
        if i % b3 = = 0 and i % b5 != 0:
            print("fizz", b4 = " ")
            a1 += 1
        elif i % b5 = = 0 and i % b3 != 0:
            print("buzz", b4 = " ")
            a2 += 1
        elif i % b3 = = 0 and i % b5 == 0:
            print("fizzbuzz", b4 = " ")
            a3 += 1
        else:
            print(i, b4 = " ")
            a4 += 1
    print("\nFizzes in range:", a1)
    print("Buzzes in range:", a2)
    print("Fizzbuzzes in range:", a3)
    print("Normal numbers in range:", a4)
if b6 = = "__main__":
    fonk1()