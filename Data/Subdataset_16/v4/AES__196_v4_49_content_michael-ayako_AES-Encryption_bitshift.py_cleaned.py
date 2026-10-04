import numpy as np
def fonk1(b4):
    b1 = []
    for bit_string in b4:
        b2 = np.array(list(bit_string)).reshape(4, 4)
        b3 = [np.roll(row, -count) for count, row in enumerate(b2)]
        b1.append(''.join(np.array(b3).flatten()))
    return b1
def fonk2(b4):
    b1 = []
    for bit_string in b4:
        b2 = np.array(list(bit_string)).reshape(4, 4)
        b3 = [np.roll(row, count) for count, row in enumerate(b2)]
        b1.append(''.join(np.array(b3).flatten()))
    return b1
def fonk3(title, b4):
    print(f"\n{title}:")
    for bit_string in b4:
        print(bit_string)
def fonk4():
    b4 = [
        "00010010001101000101011001111000",
        "11110000101010101111000010101010"
    ]
    b5 = fonk1(b4)
    b6 = fonk2(b4)
    fonk3("Original b4", b4)
    fonk3("Left shifted b4", b5)
    fonk3("Right shifted b4", b6)
if b7 = = "__main__":
    fonk4()