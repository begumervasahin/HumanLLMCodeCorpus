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
    else:
        return modern_euclid_recursive(b, a % b)
def get_algorithm_choice():
    while True:
        alg = input("Choose algorithm - Classic (c) or Modern (m) Euclidean: ").lower()
        if alg in ['c', 'm']:
            return alg
        print("Invalid choice. Please choose 'c' for Classic or 'm' for Modern.")
def get_number(prompt):
    while True:
        num = input(prompt)
        if num.isnumeric():
            return int(num)
        print("Invalid input. Please enter a numeric value.")
def main():
    while True:
        alg = get_algorithm_choice()
        while True:
            n = input("Enter a number (or type 'exit' to choose algorithm again): ").lower()
            if n == 'exit':
                break
            if n.isnumeric():
                a = int(n)
                b = get_number("Enter the second number: ")
                if alg == 'c':
                    gcd = classic_euclid_recursive(a, b)
                else:
                    gcd = modern_euclid_recursive(a, b)
                print(f"The GCD of {a} and {b} is: {gcd}")
            else:
                print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()