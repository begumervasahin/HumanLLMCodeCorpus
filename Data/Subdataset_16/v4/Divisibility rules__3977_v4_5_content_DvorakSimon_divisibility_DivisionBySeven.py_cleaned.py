def fonk1(number):
    b1 = number
    b2 = str(b1)
    while len(b2) > 2 and b1 > 0:
        print(b2)
        b3 = b2[:-1]
        b4 = int(b2[-1])
        b5 = int(b3) - (2 * b4)
        b2 = str(b5)
        b1 = b5
    if b1 % b6 = = 0:
        return f"Number {b2} is divisible by b6!"
    else:
        return f"Number {b2} is not divisible by b6."
if b7 = = "__main__":
    a1 = 1946
    b8 = fonk1(a1)
    print(b8)