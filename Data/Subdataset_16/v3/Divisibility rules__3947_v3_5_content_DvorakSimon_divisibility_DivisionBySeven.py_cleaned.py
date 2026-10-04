def fonk1(b5):
    b1 = str(b5)
    while len(b1) > 2 and b5 > 0:
        print(b1)
        b2 = b1[:-1]
        b3 = int(b1[-1])
        b4 = int(b2) - (2 * b3)
        b1 = str(b4)
        b5 = b4
    if b5 % b6 = = 0:
        return f"Number {b1} is divisible by b6!"
    else:
        return f"Number {b1} is not divisible by b6."
if b7 = = "__main__":
    a1 = 1946
    b8 = fonk1(a1)
    print(b8)