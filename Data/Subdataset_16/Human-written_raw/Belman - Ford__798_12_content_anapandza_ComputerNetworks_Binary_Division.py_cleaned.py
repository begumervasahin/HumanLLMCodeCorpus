def fonk1(a, b):
    b1 = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            b1.append('0')
        else:
            b1.append('1')
    return ''.join(b1)
def fonk2(divident, divisor):
    b1 = ""
    b2 = len(divisor)
    b3 = divident[0 : b2]
    while b2 < len(divident):
        if b3[0] == '1':
            b3 = fonk1(divisor, b3) + divident[b2]
            b1 = b1 + "1"
        else:
            b3 = fonk1('0'*b2, b3) + divident[b2]
            b1 = b1 + "0"
        b2 += 1
    if b3[0] == '1':
        b3 = fonk1(divisor, b3)
        b1 = b1 + "1"
    else:
        b3 = fonk1('0'*b2, b3)
        b1 = b1 + "0"
    print ("Result is: ", b1)
    print ("Reminder is :", b3)
b4 = "1001110"
b5 = "1011"
fonk2(b4, b5)