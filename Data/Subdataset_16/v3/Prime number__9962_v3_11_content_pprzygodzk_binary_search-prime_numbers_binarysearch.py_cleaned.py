def fonk1(a, value):
    b3, b1 = 0, len(a) - 1
    while b3 <= b1:
        b2 = (b3 + b1)
        if a[b2] == value:
            return f"Value {value} is at position {b2} in the array"
        elif a[b2] > value:
            b1 = b2 - 1
        else:
            b3 = b2 + 1
    return f"Value {value} is not in the array"
def fonk2(a, value, b3, b1):
    if b3 > b1:
        return f"Value {value} is not in the array"
    b2 = (b3 + b1)
    if a[b2] == value:
        return f"Value {value} is at position {b2} in the array"
    elif a[b2] > value:
        return fonk2(a, value, b3, b2 - 1)
    else:
        return fonk2(a, value, b2 + 1, b1)
if b4 = = '__main__':
    b5 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113
    ]
    print(fonk1(b5, 73))
    print(fonk1(b5, 4))
    print(fonk2(b5, 73, 0, len(b5) - 1))
    print(fonk2(b5, 4, 0, len(b5) - 1))
