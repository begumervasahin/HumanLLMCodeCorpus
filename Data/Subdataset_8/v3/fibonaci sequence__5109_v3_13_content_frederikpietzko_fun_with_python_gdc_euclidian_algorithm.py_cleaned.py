def classic_euclid_recursive(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return classic_euclid_recursive(a - min(a, b), b - min(a, b))
def modern_euclid_recursive(a, b):
    if b == 0:
        return a
    return modern_euclid_recursive(b, a % b)
if __name__ == "__main__":
    while True:
        alg = input("Classic (c) or modern Euclid (e) algorithm? ")
        if alg.lower() not in ['c', 'e']:
            print("Invalid input. Please choose 'c' or 'e'.")
            continue
        while True:
            n = input("Enter 'exit' to choose another algorithm. Otherwise, enter a number: ")
            if n.lower() == 'exit':
                break
            elif n.isnumeric():
                a = int(n)
                b = int(input("Enter the second number: "))
                gcd = classic_euclid_recursive(a, b) if alg == "c" else modern_euclid_recursive(a, b)
                print(f"GCD of {a} and {b} is: {gcd}")
            else:
                print("Invalid input. Please enter a number or 'exit'.")