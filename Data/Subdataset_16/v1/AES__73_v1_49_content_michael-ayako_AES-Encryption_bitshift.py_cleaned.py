import numpy as np
def fonk1(b5):
    b1 = []
    for bit_string in b5:
        b2 = np.array(list(bit_string)).reshape(4, 4)
        b3 = []
        for count, row in enumerate(b2):
            b4 = np.roll(row, -count)
            b3.append(b4)
        b1.append(np.array(b3).reshape(4, 4))
    return [''.join(b2.flatten()) for b2 in b1]
def fonk2(b5):
    b1 = []
    for bit_string in b5:
        b2 = np.array(list(bit_string)).reshape(4, 4)
        b3 = []
        for count, row in enumerate(b2):
            b4 = np.roll(row, count)
            b3.append(b4)
        b1.append(np.array(b3).reshape(4, 4))
    return [''.join(b2.flatten()) for b2 in b1]
def fonk3():
    b5 = [
        "00010010001101000101011001111000",
        "11110000101010101111000010101010"
    ]
    b6 = fonk1(b5)
    b7 = fonk2(b5)
    print("Original b5:")
    for bit_string in b5:
        print(bit_string)
    print("\nLeft shifted b5:")
    for bit_string in b6:
        print(bit_string)
    print("\nRight shifted b5:")
    for bit_string in b7:
        print(bit_string)
if b8 = = "__main__":
    fonk3()