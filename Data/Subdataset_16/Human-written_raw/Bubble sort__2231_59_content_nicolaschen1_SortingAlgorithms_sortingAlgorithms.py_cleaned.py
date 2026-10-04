b1 = [6, 3, 2, 89, 10, 2.3, 5, 80.2]
def fonk1(list):
    for i in range(1, len(list)):
        b2 = list[i]
        b3 = i
        while b3 > 0 and list[b3-1] > b2:
            list[b3] = list[b3 - 1]
            b3 = b3-1
        list[b3] = b2
    return list
def fonk2(list):
    b4 = True
    a1 = 0
    while b4 = = True:
        b4 = False
        a1 = a1 + 1
        for b2 in range(0, len(list) - a1):
            if list[b2] > list[b2 + 1]:
                b4 = True
                list[b2], list[b2 + 1] = list[b2 + 1], list[b2]
    return list
def fonk3(list):
    b4, b6, b2 = True, 1, 0
    b8, b5 = 0, len(list) - 2
    while b4 = = True:
        b4 = False
        while (b2 < b5 and b6 = = 1) or \
        (b2 > b8 and b6 = = -1) :
            if list[b2] > list[b2 + 1]:
                b4 = True
                list[b2], list[b2 + 1] = \
                    list[b2 + 1], list[b2]
            b2 = b2 + b6
        if b6 = =1:
            b7 = b5 - 1
        else:
            b8 = b8 + 1
        b6 = -b6
    return list
def fonk4(list):
    b11, b10, b9 = 1,2,len(list)
    while b11 < b9:
        if list[b11-1] <= list[b11]:
            b11, b10 = b10, b10+1
        else:
            list[b11 - 1], list[b11] = list[b11], list[b11 - 1]
            b11 -= 1
            if b11 = = 0:
                b11, b10 = b10, b10+1
    return list
def fonk5(b15, b16):
    b12 = []
    left_index, b13 = 0, 0
    while left_index < len(b15) and b13 < len(b16):
        if b15[left_index] <= b16[b13]:
            b12.append(b15[left_index])
            left_index += 1
        else:
            b12.append(b16[b13])
            b13 += 1
    if b15:
        b12.extend(b15[left_index:])
    if b16:
        b12.extend(b16[b13:])
    return b12
def fonk6(x):
    if len(x) <= 1:
        return x
    b14 = len(x)
    b15 = x[:b14]
    b16 = x[b14:]
    b15 = fonk6(b15)
    b16 = fonk6(b16)
    return list(fonk5(b15, b16))
def fonk7(list):
    b17 = len(list)
    for b2 in range(0,b17):
        b18 = b2
        for b3 in range(b2+1,b17) :
            if list[b3] < list[b18] :
                b18 = b3
        if b18 is not b2 :
            b19 = list[b2]
            list[b2] = list[b18]
            list[b18] = b19
    return list
print(fonk1(b1))
print(fonk2(b1))
print(fonk3(b1))
print(fonk4(b1))
print(fonk6(b1))
print(fonk7(b1))