
def fonk1(x):
    a1 = 1
    for i in range(2, x + 1):
        a1 *= i
    return a1
def fonk2(b1):
    return [int(digit) for digit in str(b1)]
def fonk3(b1):
    return b1 = = sum(fonk1(digit) for digit in fonk2(b1))
def fonk4(limit):
    b2 = []
    for i in range(3, limit):
        if i % b3 = = 0:
            print(f"Checked up to {i} numbers...")
        if fonk3(i):
            b2.append(i)
    print(f"Curious numbers are: {b2}")
    print(f"There are {len(b2)} curious numbers less than {limit}.")
    return b2
if b4 = = "__main__":
    fonk4(100000000)