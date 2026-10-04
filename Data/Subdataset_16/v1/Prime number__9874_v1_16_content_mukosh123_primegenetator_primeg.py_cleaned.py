def fonk1(num):
    if type(num) != int:
        return 'wrong arg'
    if num < 0 or type(num) != int:
        return 'wrong arg'
    b1 = []
    for i in range(1, num + 1):
        b2 = True
        a1 = 2
        while a1 < i:
            if i % a1 = = 0:
                b2 = False
                break
            a1 += 1
        if b2:
            b1.append(i)
    return b1
if b3 = = "__main__":
    a2 = 10
    b4 = fonk1(a2)
    print("Prime numbers up to {}: {}".format(a2, b4))