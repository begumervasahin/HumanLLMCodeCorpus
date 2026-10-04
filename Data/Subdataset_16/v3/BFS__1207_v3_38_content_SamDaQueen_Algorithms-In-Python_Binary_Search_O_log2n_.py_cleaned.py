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
def fonk2():
    b3 = [1, 3, 9, 11, 15, 19, 29]
    b4 = [
        (25, "Index of {0} in the list: {1}"),
        (15, "Index of {0} in the list: {1}")
    ]
    for value, message in b4:
        b5 = fonk1(b3, value)
        print(message.format(value, b5))
if b6 = = "__main__":
    fonk2()