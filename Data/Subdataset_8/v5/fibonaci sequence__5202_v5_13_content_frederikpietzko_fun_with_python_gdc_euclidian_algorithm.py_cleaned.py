def classic_euclid_recursive(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    if a > b:
        return classic_euclid_recursive(a - b, b)
    else:
        return classic_euclid_recursive(a, b - a)
def modern_euclid_recursive(a, b):
    if b == 0:
        return a
    return modern_euclid_recursive(b, a % b)
if __name__ == "__main__":
    while True:
        algorithm_choice = input("Choose Classic (c) or Modern (e) Euclid algorithm: ")
        while True:
            number_input = input("Enter 'exit' to choose another algorithm. Otherwise, enter a number: ")
            if number_input.isnumeric():
                a = int(number_input)
                b = int(input("Enter the second number: "))
                if algorithm_choice.lower() == "c":
                    gcd = classic_euclid_recursive(a, b)
                else:
                    gcd = modern_euclid_recursive(a, b)
                print(f"The GCD of {a} and {b} is: {gcd}")
            else:
                break