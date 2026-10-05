def fonk1(sorted_list, target):
    a1 = 0
    b1 = len(sorted_list) - 1
    b2 = False
    while a1 <= b1 and not b2:
        b3 = (a1 + b1)
        if sorted_list[b3] == target:
            b2 = True
        else:
            if target < sorted_list[b3]:
                b1 = b3 - 1
            else:
                a1 = b3 + 1
    return b2
b4 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(fonk1(b4, 3))
print(fonk1(b4, 13))
