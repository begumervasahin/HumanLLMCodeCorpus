def main():
    min_limit = max_limit = step = fizzes = buzzes = fizzbuzzes = normal = 0
    while True:
        try:
            min_limit, max_limit = map(int, input("Enter the start and stop values separated by a space: ").split())
            break
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
    if min_limit > max_limit:
        step = -1
    for i in range(min_limit, max_limit + step, step):
        if i % 3 == 0 and i % 5 != 0 and i != 0:
            print("fizz", end=" ")
            fizzes += 1
        elif i % 5 == 0 and i % 3 != 0 and i != 0:
            print("buzz", end=" ")
            buzzes += 1
        elif i % 3 == 0 and i % 5 == 0 and i != 0:
            print("fizzbuzz", end=" ")
            fizzbuzzes += 1
        else:
            print(i, end=" ")
            normal += 1
    print("\nFizzes in range:", fizzes)
    print("Buzzes in range:", buzzes)
    print("Fizzbuzzes in range:", fizzbuzzes)
    print("Normal numbers in range:", normal)
if __name__ == "__main__":
    main()