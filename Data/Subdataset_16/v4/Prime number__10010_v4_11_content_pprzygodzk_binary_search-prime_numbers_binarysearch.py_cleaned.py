def fonk1(array, value):
    a1 = 0
    b1 = len(array) - 1
    while a1 <= b1:
        b2 = (a1 + b1)
        if array[b2] == value:
            return f"Value {value} is at the {b2} position of the array"
        elif array[b2] > value:
            b1 = b2 - 1
        else:
            a1 = b2 + 1
    return f"Value {value} is not in the array"
def fonk2(array, value, a1, b1):
    if a1 > b1:
        return f"Value {value} is not in the array"
    b2 = (a1 + b1)
    if array[b2] == value:
        return f"Value {value} is at the {b2} position of the array"
    elif array[b2] > value:
        return fonk2(array, value, a1, b2 - 1)
    else:
        return fonk2(array, value, b2 + 1, b1)
if b3 = = '__main__':
    b4 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
        59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113
    ]
    print(fonk1(b4, 73))
    print(fonk1(b4, 4))
    print(fonk2(b4, 73, 0, len(b4) - 1))
    print(fonk2(b4, 4, 0, len(b4) - 1))