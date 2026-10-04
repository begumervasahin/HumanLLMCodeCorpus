def fonk1():
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    while True:
        try:
            b1 = input("Enter start and stop values (separated by a space): ").split()
            min_limit, b2 = int(b1[0]), int(b1[1])
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter two integers separated by a space.")
    b3 = 1 if min_limit <= b2 else -1
    for number in range(min_limit, b2 + b3, b3):
        if number % b4 = = 0 and number % b6 != 0:
            print("fizz", b5 = " ")
            a1 += 1
        elif number % b6 = = 0 and number % b4 != 0:
            print("buzz", b5 = " ")
            a2 += 1
        elif number % b4 = = 0 and number % b6 == 0:
            print("fizzbuzz", b5 = " ")
            a3 += 1
        else:
            print(number, b5 = " ")
            a4 += 1
    print("\nFizzes in range:", a1)
    print("Buzzes in range:", a2)
    print("Fizzbuzzes in range:", a3)
    print("Normal numbers in range:", a4)
if b7 = = "__main__":
    fonk1()