import time
def fonk1(b7):
    def fonk2(left, right):
        b1 = []
        b2 = j = 0
        while b2 < len(left) and j < len(right):
            merge_sort.a1 += 1
            if left[b2] < right[j]:
                b1.append(left[b2])
                b2 += 1
            else:
                b1.append(right[j])
                j += 1
        b1.extend(left[b2:])
        b1.extend(right[j:])
        return b1
    if len(b7) <= 1:
        return b7
    b3 = len(b7)
    b4 = fonk1(b7[:b3])
    b5 = fonk1(b7[b3:])
    return fonk2(b4, b5)
def fonk3(b7):
    print(" ".join(map(str, b7)))
def fonk4():
    b6 = time.time()
    with open("case", "r") as file:
        b7 = file.read().split()
    b8 = [int(num) for num in b7]
    merge_sort.a1 = 0
    b9 = fonk1(b8)
    print("Sorted array is:")
    fonk3(b9)
    print(f"Number of comparisons: {merge_sort.a1}")
    b10 = time.time()
    print(f"Time taken: {b10 - b6:.6f} seconds")
if b11 = = "__main__":
    fonk4()