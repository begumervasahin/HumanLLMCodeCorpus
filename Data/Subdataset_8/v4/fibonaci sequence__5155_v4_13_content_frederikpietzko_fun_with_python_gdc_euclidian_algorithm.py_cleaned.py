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
if __name__ == "__main__":
    while True:
        alg = input("Classic (c) or modern Euclid (e) algorithm?")
        while True:
            n = input("Enter 'exit' to choose another algorithm. Otherwise, enter a number: ")
            if n.isnumeric():
                a = int(n)
                b = int(input("Enter the second number: "))
                gcd = classic_euclid_recursive(a, b) if alg == "c" else modern_euclid_recursive(a, b)
                print(gcd)
            else:
                break