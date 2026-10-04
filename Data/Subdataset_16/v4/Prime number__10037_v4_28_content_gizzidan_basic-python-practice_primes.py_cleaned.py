def fonk1(b5):
    lower_bound, b1 = sorted(b5)
    b2 = []
    for x in range(lower_bound + 1, b1):
        if x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)):
            b2.append(x)
    if not b2:
        return "No Primes"
    for i in range(0, len(b2), 3):
        b2[i] = str(b2[i]) + ":"
    for i in range(1, len(b2), 3):
        b2[i] = str(b2[i]) + "!"
    for i in range(2, len(b2), 3):
        b2[i] = str(b2[i]) + ","
    return "".join(b2)
def fonk2():
    try:
        b3 = int(input("Enter first number: "))
        b4 = int(input("Enter second number: "))
        b5 = [b3, b4]
        b6 = fonk1(b5)
        print(b6)
    except ValueError:
        print("Please enter valid integers.")
if b7 = = "__main__":
    fonk2()