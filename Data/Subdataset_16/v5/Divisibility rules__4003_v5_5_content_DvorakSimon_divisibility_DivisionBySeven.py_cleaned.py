def fonk1(number):
    b1 = number
    while len(str(b1)) > 2 and b1 > 0:
        print(b1)
        b2 = str(b1)[:-1]
        b3 = int(str(b1)[-1])
        b1 = int(b2) - (2 * b3)
    if b1 % b4 = = 0:
        return f"Number {b1} is divisible by b4!"
    else:
        return f"Number {b1} is not divisible by b4."
if b5 = = "__main__":
    a1 = 1946
    b6 = fonk1(a1)
    print(b6)