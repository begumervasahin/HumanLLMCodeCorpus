import numpy as np
def fonk1(b4):
    b1 = []
    for bit_string in b4:
        b2 = np.array(list(bit_string)).reshape(4, 4)
        b3 = [np.roll(row, -count) for count, row in enumerate(b2)]
        b1.append(np.array(b3).reshape(4, 4))
    return [''.join(b2.flatten()) for b2 in b1]
def fonk2(b4):
    b1 = []
    for bit_string in b4:
        b2 = np.array(list(bit_string)).reshape(4, 4)
        b3 = [np.roll(row, count) for count, row in enumerate(b2)]
        b1.append(np.array(b3).reshape(4, 4))
    return [''.join(b2.flatten()) for b2 in b1]
def fonk3():
    b4 = [
        "00010010001101000101011001111000",
        "11110000101010101111000010101010"
    ]
    b5 = fonk1(b4)
    b6 = fonk2(b4)
    print("Original b4:")
    for bit_string in b4:
        print(bit_string)
    print("\nLeft shifted b4:")
    for bit_string in b5:
        print(bit_string)
    print("\nRight shifted b4:")
    for bit_string in b6:
        print(bit_string)
if b7 = = "__main__":
    fonk3()