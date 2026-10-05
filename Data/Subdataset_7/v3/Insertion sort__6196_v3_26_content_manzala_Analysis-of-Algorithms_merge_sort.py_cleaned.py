import timeit
import random
def fonk1(src, src_pos, dest, dest_pos, length):
    for b4 in range(length):
        dest[b4 + dest_pos] = src[b4 + src_pos]
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
def fonk3(b2, b3, array):
    b4 = j = k = 0
    while b4 < len(b2) and j < len(b3):
        if b2[b4] < b3[j]:
            array[k] = b2[b4]
            b4 += 1
        else:
            array[k] = b3[j]
            j += 1
        k += 1
    fonk1(b2, b4, array, k, len(b2) - b4)
    fonk1(b3, j, array, k, len(b3) - j)
b5 = [7, 4, 8, 3, 1, 12, 9, 14]
for _ in range(5000):
    b5.append(random.randint(1, 99999))
b6 = timeit.default_timer()
fonk2(b5)
b7 = timeit.default_timer() - b6
print("Merge Sort: " + str(b7))
print(b5)