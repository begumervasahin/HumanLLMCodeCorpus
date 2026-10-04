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
def fonk3(b2, b3):
    b4 = []
    l_index, b5 = 0, 0
    while l_index < len(b2) and b5 < len(b3):
        if b2[l_index] <= b3[b5]:
            b4.append(b2[l_index])
            l_index += 1
        else:
            b4.append(b3[b5])
            b5 += 1
    b4.extend(b2[l_index:])
    b4.extend(b3[b5:])
    return b4
b6 = [7, 4, 3, 8, 1, 12, 9, 14]
for _ in range(5000):
    b6.append(random.randint(1, 99999))
b7 = timeit.default_timer()
b8 = fonk2(b6)
b9 = timeit.default_timer() - b7
print("Merge Sort: " + str(b9))
print(b8)