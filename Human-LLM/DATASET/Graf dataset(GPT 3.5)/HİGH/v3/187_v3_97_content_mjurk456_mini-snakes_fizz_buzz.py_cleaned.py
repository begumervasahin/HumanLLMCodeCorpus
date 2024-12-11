def fonk1():
    while True:
        try:
            min_limit, b1 = map(int, input("Enter the start and stop values separated by a space: ").split())
            return min_limit, b1
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
def fonk2(min_limit, b1):
    b2 = buzzes = fizzbuzzes = b7 = 0
    b3 = 1 if min_limit <= b1 else -1
    for i in range(min_limit, b1 + b3, b3):
        if i % b4 = = 0 and i % b6 != 0 and i != 0:
            print("fizz", b5 = " ")
            b2 += 1
        elif i % b6 = = 0 and i % b4 != 0 and i != 0:
            print("buzz", b5 = " ")
            buzzes += 1
        elif i % b4 = = 0 and i % b6 == 0 and i != 0:
            print("fizzbuzz", b5 = " ")
            fizzbuzzes += 1
        else:
            print(i, b5 = " ")
            b7 += 1
    return b2, buzzes, fizzbuzzes, b7
def fonk3(b2, buzzes, fizzbuzzes, b7):
    print("\nNumber of b2 in the range:", b2)
    print("Number of buzzes in the range:", buzzes)
    print("Number of fizzbuzzes in the range:", fizzbuzzes)
    print("Number of b7 numbers in the range:", b7)
def fonk4():
    min_limit, b1 = fonk1()
    b2, buzzes, fizzbuzzes, b7 = fonk2(min_limit, b1)
    fonk3(b2, buzzes, fizzbuzzes, b7)
if b8 = = "__main__":
    fonk4()