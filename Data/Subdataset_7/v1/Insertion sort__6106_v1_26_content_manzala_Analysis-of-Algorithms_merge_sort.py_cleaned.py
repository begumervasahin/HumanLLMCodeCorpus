import timeit
import random
def fonk1(src, srcPos, dest, destPos, length):
    for i in range(length):
        dest[i + destPos] = src[i + srcPos]
def fonk2(array):
    if len(array) <= 1:
        return array
    b1 = array[0:len(array)
    b2 = array[len(array)
    fonk2(b1)
    fonk2(b2)
    fonk3(b1, b2, array)
    return array
def fonk3(b1, b2, array):
    a1 = 0
    a2 = 0
    a3 = 0
    while a2 < len(b1) and a1 < len(b2):
        if b1[a2] > b2[a1]:
            array[a3] = b2[a1]
            a1 += 1
        else:
            array[a3] = b1[a2]
            a2 += 1
        a3 += 1
    fonk1(b1, a2, array, a3, len(b1) - a2)
    fonk1(b2, a1, array, a3, len(b2) - a1)
b3 = [7, 4, 8, 3, 1, 12, 9, 14]
for x in range(0, 5000):
    b4 = random.randint(1, 99999)
    b3.append(b4)
b5 = timeit.default_timer()
fonk2(b3)
b6 = timeit.default_timer() - b5
print("Merge Sort: " + str(b6))
print(b3)