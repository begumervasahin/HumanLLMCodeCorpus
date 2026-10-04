def fonk1(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))
def fonk2(dividend, divisor):
    b1 = len(divisor)
    b2 = dividend[:b1]
    b3 = []
    while b1 < len(dividend):
        if b2[0] == '1':
            b2 = fonk1(divisor, b2) + dividend[b1]
            b3.append('1')
        else:
            b2 = fonk1('0' * b1, b2) + dividend[b1]
            b3.append('0')
        b1 += 1
    if b2[0] == '1':
        b2 = fonk1(divisor, b2)
        b3.append('1')
    else:
        b2 = fonk1('0' * b1, b2)
        b3.append('0')
    return ''.join(b3), b2
def fonk3():
    b4 = "1001110"
    b5 = "1011"
    b3, b6 = fonk2(b4, b5)
    print("Data:", b4)
    print("Key:", b5)
    print("Result:", b3)
    print("Remainder:", b6)
if b7 = = "__main__":
    fonk3()