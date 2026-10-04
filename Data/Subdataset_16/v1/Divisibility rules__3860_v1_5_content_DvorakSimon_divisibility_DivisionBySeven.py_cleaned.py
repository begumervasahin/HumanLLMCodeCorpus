def fonk1(b4):
    b1 = str(b4)
    while len(b1) > 2 and b4 > 0:
        print(b1)
        b2 = b1[:-1]
        b3 = int(b1[-1])
        b1 = str(int(b2) - (2 * b3))
        b4 = int(b1)
    if b4 % b5 = = 0:
        return f"Number {b1} is divisible by b5!"
    else:
        return f"Number {b1} is not divisible by b5."
a1 = 1946
b6 = fonk1(a1)
print(b6)