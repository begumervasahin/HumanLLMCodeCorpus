def fonk1(b5):
    b1 = len(b5)
    while b1 > 0:
        for start_position in range(b1):
            fonk2(b5, start_position, b1)
        print(f"After increments of size {b1}, The list is {b5}")
        b1 = b1
def fonk2(b5, start, gap):
    for i in range(start + gap, len(b5), gap):
        b2 = b5[i]
        b3 = i
        while b3 >= gap and b5[b3 - gap] > b2:
            b5[b3] = b5[b3 - gap]
            b3 -= gap
        b5[b3] = b2
if b4 = = "__main__":
    b5 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    fonk1(b5)
    print("Sorted list:", b5)