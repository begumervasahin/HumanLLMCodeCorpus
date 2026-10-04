def fonk1(a, b):
    b1 = []
    for i in range(1, len(b)):
        b1.append('0' if a[i] == b[i] else '1')
    return ''.join(b1)
def fonk2(dividend, divisor):
    b2 = len(divisor)
    b3 = dividend[0:b2]
    while b2 < len(dividend):
        if b3[0] == '1':
            b3 = fonk1(divisor, b3) + dividend[b2]
        else:
            b3 = fonk1('0' * b2, b3) + dividend[b2]
        b2 += 1
    if b3[0] == '1':
        b3 = fonk1(divisor, b3)
    else:
        b3 = fonk1('0' * b2, b3)
    return b3
def fonk3():
    b4 = "1001110"
    b5 = "1011"
    b6 = fonk2(b4, b5)
    print("Data: ", b4)
    print("Key: ", b5)
    print("Remainder: ", b6)
if b7 = = "__main__":
    fonk3()