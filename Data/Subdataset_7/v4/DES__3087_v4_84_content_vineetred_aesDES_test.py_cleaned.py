from collections import deque
def fonk1(test):
    b1 = []
    b2 = []
    a1 = 0
    for j in range(b4):
        for i in range(b4):
            b2.append(test[(8 * i) + a1:(8 * i) + 2 + a1])
        a1 += 2
        b1.append(b2)
        b2 = []
    return b1
def fonk2(bytes_string):
    b3 = []
    for i, byte in enumerate(bytes_string):
        if i % b4 = = 0:
            b3.append([byte])
        else:
            b3[i
    return b3
def fonk3(key):
    b5 = []
    b6 = fonk2(bytes.fromhex(key))
    for j in range(b4, 44):
        b7 = b6[j - b4][0]
        b8 = b6[j - b4][1]
        b9 = b6[j - b4][2]
        b10 = b6[j - b4][3]
        b11 = [b10, b7, b8, b9]
        b6.append(b11)
    return b6
b12 = "7750f228896eb4561b9cd67497aad0b1"
b13 = fonk3(b12)
print("Length of b13 key schedule:", len(b13))