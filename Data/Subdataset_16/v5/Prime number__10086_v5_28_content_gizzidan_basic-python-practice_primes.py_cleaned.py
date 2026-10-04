def fonk1(b7):
    lower_bound, b1 = sorted(b7)
    b2 = []
    for num in range(lower_bound + 1, b1):
        if num > 1 and all(num % divisor != 0 for divisor in range(2, int(num ** 0.5) + 1)):
            b2.append(num)
    if not b2:
        return "No Primes"
    b3 = []
    for i, prime in enumerate(b2):
        if i % b4 = = 0:
            b3.append(f"{prime}:")
        elif i % b4 = = 1:
            b3.append(f"{prime}!")
        else:
            b3.append(f"{prime},")
    return "".join(b3)
def fonk2():
    try:
        b5 = int(input("Enter first number: "))
        b6 = int(input("Enter second number: "))
        b7 = [b5, b6]
        b8 = fonk1(b7)
        print(b8)
    except ValueError:
        print("Please enter valid integers.")
if b9 = = "__main__":
    fonk2()