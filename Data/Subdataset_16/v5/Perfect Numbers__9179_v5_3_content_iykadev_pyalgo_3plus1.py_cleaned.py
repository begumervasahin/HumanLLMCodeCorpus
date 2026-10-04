def fonk1(b2):
    b1 = []
    while b2 > 1:
        b1.append(b2)
        if b2 % 2:
            b2 = 3 * b2 + 1
        else:
            b2 = b2
    b1.append(1)
    return b1
def fonk2(start_value):
    b1 = fonk1(start_value)
    for value in b1:
        print(value)
if b3 = = "__main__":
    fonk2(15000)