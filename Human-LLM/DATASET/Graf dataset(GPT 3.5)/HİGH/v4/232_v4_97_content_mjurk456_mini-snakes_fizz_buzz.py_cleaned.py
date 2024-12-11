def fonk1():
    b1 = b2 = a1 = fizzes = buzzes = fizzbuzzes = normal = 0
    while True:
        try:
            b1, b2 = map(int, input("Enter the start and stop values separated by a space: ").split())
            break
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
    if b1 > b2:
        a1 = -1
    for i in range(b1, b2 + a1, a1):
        if i % b3 = = 0 and i % b5 != 0 and i != 0:
            print("fizz", b4 = " ")
            fizzes += 1
        elif i % b5 = = 0 and i % b3 != 0 and i != 0:
            print("buzz", b4 = " ")
            buzzes += 1
        elif i % b3 = = 0 and i % b5 == 0 and i != 0:
            print("fizzbuzz", b4 = " ")
            fizzbuzzes += 1
        else:
            print(i, b4 = " ")
            normal += 1
    print("\nFizzes in range:", fizzes)
    print("Buzzes in range:", buzzes)
    print("Fizzbuzzes in range:", fizzbuzzes)
    print("Normal numbers in range:", normal)
if b6 = = "__main__":
    fonk1()