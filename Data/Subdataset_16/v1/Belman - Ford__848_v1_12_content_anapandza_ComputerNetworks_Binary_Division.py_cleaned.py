def fonk1(a, b):
    b1 = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            b1.append('0')
        else:
            b1.append('1')
    return ''.join(b1)
def fonk2(dividend, divisor):
    b2 = len(divisor)
    b3 = dividend[0:b2]
    while b2 < len(dividend):
        if b3[0] == '1':
            b3 = fonk1(divisor, b3) + dividend[b2]
        else:
            b3 = fonk1('0'*b2, b3) + dividend[b2]
        b2 += 1
    if b3[0] == '1':
        b3 = fonk1(divisor, b3)
    else:
        b3 = fonk1('0'*b2, b3)
    b4 = b3
    return b4
def fonk3():
    b5 = "1001110"
    b6 = "1011"
    b7 = fonk2(b5, b6)
    print("Data: ", b5)
    print("Key: ", b6)
    print("Remainder: ", b7)
if b8 = = "__main__":
    fonk3()