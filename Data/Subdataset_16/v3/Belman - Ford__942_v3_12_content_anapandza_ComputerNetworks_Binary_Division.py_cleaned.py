def fonk1(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))
def fonk2(dividend, divisor):
    b1 = len(divisor)
    b2 = dividend[:b1]
    while b1 < len(dividend):
        if b2[0] == '1':
            b2 = fonk1(divisor, b2) + dividend[b1]
        else:
            b2 = fonk1('0' * b1, b2) + dividend[b1]
        b1 += 1
    if b2[0] == '1':
        b2 = fonk1(divisor, b2)
    else:
        b2 = fonk1('0' * b1, b2)
    return b2
def fonk3():
    b3 = "1001110"
    b4 = "1011"
    b5 = fonk2(b3, b4)
    print("Data:", b3)
    print("Key:", b4)
    print("Remainder:", b5)
if b6 = = "__main__":
    fonk3()