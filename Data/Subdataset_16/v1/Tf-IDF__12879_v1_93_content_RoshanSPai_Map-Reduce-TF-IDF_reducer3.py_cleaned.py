from operator import itemgetter
import sys
def fonk1(b18):
    b1 = None
    a1 = 0
    b2 = {}
    b3 = []
    for b4 in b18:
        b4 = b4.strip()
        b3.append(b4)
        var2, b5 = b4.split(',')
        var3, b6 = var2.split('=')
        b6 = b6.strip()
        b7 = b5.split("&")
        b8 = b7[3].strip()
        try:
            b8 = int(b8)
        except ValueError:
            continue
        if b1 = = b6:
            a1 += b8
        else:
            if b1:
                b2[b1] = a1
            a1 = b8
            b1 = b6
    if b1 = = b6:
        b2[b1] = a1
    return b2, b3
def fonk2(b2, b3):
    b9 = []
    for b4 in b3:
        b4 = b4.strip()
        var2, b5 = b4.split(',')
        var3, b6 = var2.split('=')
        b6 = b6.strip()
        b7, b10 = b5.split("=")
        b11 = b10.split("&")
        b12 = b11[0]
        b13 = b11[1]
        b14 = b11[2]
        b15 = str(b2[b6])
        b16 = f"key={b6}&{b12}, b11={b13}&{b14}&{b15}"
        b9.append(b16)
    return b9
if b17 = = "__main__":
    b18 = [
        "b19 = value1, value2&value3&value4&5",
        "b20 = value2, value5&value6&value7&10",
        "b19 = value1, value2&value3&value4&15"
    ]
    b2, b3 = fonk1(b18)
    b9 = fonk2(b2, b3)
    for b4 in b9:
        print(b4)