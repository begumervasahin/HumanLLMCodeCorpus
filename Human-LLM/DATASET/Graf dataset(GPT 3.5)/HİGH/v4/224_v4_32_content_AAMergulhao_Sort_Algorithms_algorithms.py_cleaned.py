def fonk1(lst):
    if len(lst) <= 1:
        return lst
    b1 = lst[0]
    b2 = [x for x in lst if x == b1]
    b3 = [x for x in lst if x < b1]
    b4 = [x for x in lst if x > b1]
    return fonk1(b3) + b2 + fonk1(b4)
def fonk2(lst):
    b5 = []
    b6 = lst[:]
    while b6:
        b7 = min(b6)
        b5.append(b7)
        b6.remove(b7)
    return b5
def fonk3(b11, b12):
    b8 = []
    i, b9 = 0, 0
    while i < len(b11) and b9 < len(b12):
        if b11[i] <= b12[b9]:
            b8.append(b11[i])
            i += 1
        else:
            b8.append(b12[b9])
            b9 += 1
    b8 += b11[i:]
    b8 += b12[b9:]
    return b8
def fonk4(lst):
    if len(lst) <= 1:
        return lst
    else:
        b10 = len(lst)
        b11 = fonk4(lst[:b10])
        b12 = fonk4(lst[b10:])
        return fonk3(b11, b12)