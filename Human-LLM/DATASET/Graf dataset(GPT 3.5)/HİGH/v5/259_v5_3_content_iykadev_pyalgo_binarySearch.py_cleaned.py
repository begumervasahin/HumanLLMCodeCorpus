def fonk1(sorted_list, target):
    a1 = 0
    b1 = len(sorted_list) - 1
    while a1 <= b1:
        b2 = (a1 + b1)
        if sorted_list[b2] == target:
            return True
        elif target < sorted_list[b2]:
            b1 = b2 - 1
        else:
            a1 = b2 + 1
    return False
b3 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(fonk1(b3, 3))
print(fonk1(b3, 13))
