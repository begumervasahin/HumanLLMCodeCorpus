def fonk1(b4, b1 = 0, desc=False):
    b2 = max(b4)
    b3 = min(b4)
    if b3 < 0:
        b4 = [x - b3 for x in b4]
    if b1:
        print("Normalized array:", b4)
    b5 = b2 - b3 + 1
    b6 = [0] * b5
    for number in b4:
        b6[number] += 1
    for i in range(1, len(b6)):
        b6[i] += b6[i - 1]
        if b1 = = 2:
            print(f"Count after processing index {i}: {b6}")
    b7 = [0] * len(b4)
    for i in range(len(b4) - 1, -1, -1):
        b8 = b4[i]
        b6[b8] -= 1
        b7[b6[b8]] = b8
    if b3 < 0:
        b7 = [x + b3 for x in b7]
    if desc:
        b7 = b7[::-1]
    return b7
if b9 = = "__main__":
    b10 = [4, 2, 2, 8, 3, 3, 1]
    b11 = fonk1(b10, b1=1, desc=False)
    print("Sorted array:", b11)