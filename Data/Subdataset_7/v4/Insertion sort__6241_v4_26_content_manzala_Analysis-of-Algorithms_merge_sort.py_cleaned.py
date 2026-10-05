import timeit
import random
def fonk1(src, src_pos, dest, dest_pos, length):
    for i in range(length):
        dest[i + dest_pos] = src[i + src_pos]
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
    a1 = 0
    a2 = 0
    a3 = 0
    while a2 < len(b2) and a1 < len(b3):
        if b2[a2] > b3[a1]:
            array[a3] = b3[a1]
            a1 += 1
        else:
            array[a3] = b2[a2]
            a2 += 1
        a3 += 1
    fonk1(b2, a2, array, a3, len(b2) - a2)
    fonk1(b3, a1, array, a3, len(b3) - a1)
b4 = [7, 4, 8, 3, 1, 12, 9, 14]
for _ in range(5000):
    b5 = random.randint(1, 99999)
    b4.append(b5)
b6 = timeit.default_timer()
fonk2(b4)
b7 = timeit.default_timer() - b6
print("Merge Sort: " + str(b7))
print(b4)