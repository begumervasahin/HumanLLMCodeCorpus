import time
def fonk1(b9):
    if len(b9) <= 1:
        return b9, 0
    b1 = len(b9)
    left_half, b2 = fonk1(b9[:b1])
    right_half, b3 = fonk1(b9[b1:])
    b6, b4 = fonk2(left_half, right_half)
    b5 = b2 + b3 + b4
    return b6, b5
def fonk2(left, right):
    b6 = []
    b7 = j = 0
    a1 = 0
    while b7 < len(left) and j < len(right):
        a1 += 1
        if left[b7] < right[j]:
            b6.append(left[b7])
            b7 += 1
        else:
            b6.append(right[j])
            j += 1
    b6.extend(left[b7:])
    b6.extend(right[j:])
    return b6, a1
def fonk3(b9):
    print(" ".join(map(str, b9)))
def fonk4():
    b8 = time.time()
    with open("case", "r") as file:
        b9 = list(map(int, file.read().split()))
    sorted_arr, b5 = fonk1(b9)
    print("Sorted array is:")
    fonk3(sorted_arr)
    print(f"Total a1: {b5}")
    b10 = time.time()
    print(f"Time taken: {b10 - b8:.4f} seconds")
if b11 = = '__main__':
    fonk4()