from collections import deque
def fonk1(input_string):
    b1 = []
    b2 = []
    a1 = 0
    for _ in range(b4):
        for _ in range(b4):
            b2.append(input_string[a1:a1 + 2])
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
    for _ in range(b4, 44):
        x0, x1, x2, b7 = b6[-b4]
        b8 = [b7, x0, x1, x2]
        b6.append(b8)
    return b6
b9 = "7750f228896eb4561b9cd67497aad0b1"
b10 = fonk3(b9)
print("Length of master key schedule:", len(b10))