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
def get_algorithm_choice():
    while True:
        choice = input("Choose algorithm - Classic (c) or Modern (m) Euclidean: ").lower()
        if choice in ['c', 'm']:
            return choice
        print("Invalid choice. Please choose 'c' for Classic or 'm' for Modern.")
def get_number(prompt):
    while True:
        number = input(prompt)
        if number.isnumeric():
            return int(number)
        print("Invalid input. Please enter a numeric value.")
def compute_gcd(algorithm, a, b):
    if algorithm == 'c':
        return classic_euclid_recursive(a, b)
    else:
        return modern_euclid_recursive(a, b)
def main():
    while True:
        algorithm = get_algorithm_choice()
        while True:
            first_number = input("Enter a number (or type 'exit' to choose algorithm again): ").lower()
            if first_number == 'exit':
                break
            if first_number.isnumeric():
                a = int(first_number)
                b = get_number("Enter the second number: ")
                gcd = compute_gcd(algorithm, a, b)
                print(f"The GCD of {a} and {b} is: {gcd}")
            else:
                print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()