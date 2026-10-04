def fonk1(x):
    if x < 2:
        return False
    for b1 in range(2, int(x ** 0.5) + 1):
        if x % b1 = = 0:
            return False
    return True
def fonk2(b5):
    for b1 in range(0, len(b5), 3):
        b5[b1] = f"{b5[b1]}:"
    for b1 in range(1, len(b5), 3):
        b5[b1] = f"{b5[b1]}!"
    for b1 in range(2, len(b5), 3):
        b5[b1] = f"{b5[b1]},"
    return b5
def fonk3():
    try:
        b2 = int(input("Enter first number: "))
        b3 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    lower_bound, b4 = sorted([b2, b3])
    b5 = [x for x in range(lower_bound + 1, b4) if fonk1(x)]
    if b5:
        b6 = fonk2(b5)
        print("".join(b6))
    else:
        print("No Primes")
if b7 = = "__main__":
    fonk3()