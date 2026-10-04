import timeit
import random
def fonk1(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]
def fonk2(array):
    if len(array) <= 1:
        return array
    b1 = len(array)
    b2 = fonk2(array[:b1])
    b3 = fonk2(array[b1:])
    return fonk3(b2, b3)
def fonk3(left, right):
    b4 = []
    l_index, b5 = 0, 0
    while l_index < len(left) and b5 < len(right):
        if left[l_index] <= right[b5]:
            b4.append(left[l_index])
            l_index += 1
        else:
            b4.append(right[b5])
            b5 += 1
    b4.extend(left[l_index:])
    b4.extend(right[b5:])
    return b4
def fonk4(size, b6 = 1, upper_bound=99999):
    return [random.randint(b6, upper_bound) for _ in range(size)]
b7 = [7, 4, 3, 8, 1, 12, 9, 14] + fonk4(5000)
b8 = timeit.default_timer()
b9 = fonk2(b7)
b10 = timeit.default_timer() - b8
print(f"Merge Sort: {b10:.6f} seconds")
print(b9)