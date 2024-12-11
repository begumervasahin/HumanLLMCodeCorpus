def fonk1(lst):
    for index in range(1, len(lst)):
        b1 = lst[index]
        b2 = index
        while b2 > 0 and lst[b2 - 1] > b1:
            lst[b2] = lst[b2 - 1]
            b2 -= 1
        lst[b2] = b1
b3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b3)
print(b3)