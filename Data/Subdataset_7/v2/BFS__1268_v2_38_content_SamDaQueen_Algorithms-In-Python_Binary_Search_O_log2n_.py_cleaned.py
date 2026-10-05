def fonk1(input_array, value):
    b1 = len(input_array)
    a1 = 0
    b2 = b1
    b3 = b1
    while (value != input_array[b2]) and (b3 >= 0):
        if value < input_array[b2]:
            b1 = b2
            b2 = b2 - (b1 - a1)
        else:
            a1 = b2
            b2 = b2 + (b1 - a1)
        b3 = b3 - 1
    if b3 < 0:
        return -1
    else:
        return b2
b4 = [1, 3, 9, 11, 15, 19, 29]
a2 = 25
a3 = 15
print(fonk1(b4, a2))
print(fonk1(b4, a3))
