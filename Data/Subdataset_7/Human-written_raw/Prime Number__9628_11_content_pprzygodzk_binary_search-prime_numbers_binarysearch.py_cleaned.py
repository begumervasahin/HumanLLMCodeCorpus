def fonk1(a, value):
    a1 = 0
    b1 = len(a)-1
    while a1 <= b1:
        b2 = int((a1 + b1)/2)
        if a[b2] == value:
            return "Value {} is at the {} position of the array".format(value, b2)
        elif a[b2] > value:
            b1 = b2-1
            continue
        elif a[b2] < value:
            a1 = b2+1
            continue
    return "Value {} is not in the array".format(value)
def fonk2(a, value, a1, b1):
    if a1 > b1:
        return "Value {} is not in the array".format(value)
    b2 = int((a1 + b1)/2)
    if a[b2] == value:
        return "Value {} is at the {} position of the array".format(value, b2)
    elif a[b2] > value:
        return fonk2(a, value, a1, b2-1)
    elif a[b2] < value:
        return fonk2(a, value, b2+1, b1)
if b3 = = '__main__':
    b4 = [2, 3, 5, 7, 11, 13, 17, 19, 23,
                     29, 31, 37, 41, 43, 47, 53, 59,
                     61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113]
    print(fonk1(b4, 73))
    print(fonk1(b4, 4))
    print(fonk2(b4, 73, 0, len(b4)-1))
    print(fonk2(b4, 4, 0, len(b4)-1))