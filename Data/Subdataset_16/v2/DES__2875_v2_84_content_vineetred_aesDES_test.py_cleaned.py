from collections import deque
def fonk1(input_str):
    b1 = []
    a1 = 0
    for _ in range(b5):
        b2 = []
        for i in range(b5):
            b3 = input_str[(8 * i) + a1 : (8 * i) + 2 + a1]
            b2.append(b3)
        a1 += 2
        b1.append(b2)
    return b1
def fonk2(byte_data):
    b4 = []
    for i, byte in enumerate(byte_data):
        if i % b5 = = 0:
            b4.append([byte])
        else:
            b4[i
    return b4
def fonk3(b10):
    b6 = fonk2(bytes.fromhex(b10))
    for j in range(b5, 44):
        x0, x1, x2, b7 = b6[j - b5]
        b8 = [b7, x0, x1, x2]
        b6.append(b8)
    return b6
if b9 = = "__main__":
    b10 = "7750f228896eb4561b9cd67497aad0b1"
    b11 = fonk3(b10)
    print(f"Key Schedule Length: {len(b11)}")
    b12 = "example string for b2 break"
    b1 = fonk1(b12)
    print("Columns:")
    for col in b1:
        print(col)