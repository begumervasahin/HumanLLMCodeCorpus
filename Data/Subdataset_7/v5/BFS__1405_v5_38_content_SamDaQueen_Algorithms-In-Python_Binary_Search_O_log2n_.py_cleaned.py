
def fonk1(input_array, value):
    a1 = 0
    b1 = len(input_array) - 1
    while a1 <= b1:
        b2 = (a1 + b1)
        if input_array[b2] == value:
            return b2
        elif input_array[b2] < value:
            a1 = b2 + 1
        else:
            b1 = b2 - 1
    return -1
b3 = [1, 3, 9, 11, 15, 19, 29]
a2 = 25
a3 = 15
print(fonk1(b3, a2))
print(fonk1(b3, a3))
