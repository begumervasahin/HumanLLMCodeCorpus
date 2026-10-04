import timeit
import random
def fonk1(src, src_start, dest, dest_start, length):
    for b4 in range(length):
        dest[dest_start + b4] = src[src_start + b4]
def fonk2(array):
    if len(array) <= 1:
        return array
    b1 = len(array)
    b2 = array[:b1]
    b3 = array[b1:]
    fonk2(b2)
    fonk2(b3)
    fonk3(b2, b3, array)
    return array
def fonk3(left, right, merged):
    b4 = j = k = 0
    while b4 < len(left) and j < len(right):
        if left[b4] <= right[j]:
            merged[k] = left[b4]
            b4 += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1
    fonk1(left, b4, merged, k, len(left) - b4)
    fonk1(right, j, merged, k, len(right) - j)
def fonk4(b5 = 5000, upper_limit=99999):
    b6 = [7, 4, 3, 8, 1, 12, 9, 14]
    b7 = [random.randint(1, upper_limit) for _ in range(b5)]
    return b6 + b7
def fonk5():
    b8 = fonk4()
    b9 = timeit.default_timer()
    b10 = fonk2(b8)
    b11 = timeit.default_timer() - b9
    print(f"Merge Sort Time: {b11:.6f} seconds")
    print(b10)
if b12 = = "__main__":
    fonk5()