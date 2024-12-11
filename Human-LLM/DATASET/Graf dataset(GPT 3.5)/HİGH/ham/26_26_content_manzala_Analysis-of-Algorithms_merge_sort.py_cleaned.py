import timeit
import random
b1 = [7, 4, 8, 3, 1, 12, 9, 14]
def fonk1(src, srcPos, dest, destPos, length):
    for i in range(length):
        dest[i + destPos] = src[i + srcPos]
def fonk2(array):
    if len(array) <= 1:
        return array
    b2 = array[0:(len(array) / 2)]
    b3 = array[(len(array) / 2):len(array)]
    fonk2(b2)
    fonk2(b3)
    fonk3(b2,b3,array)
    return array
def fonk3(b2,b3,array):
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
    fonk1(b2,a2,array,a3, len(b2)-a2)
    fonk1(b3,a1, array, a3, len(b3) - a1)
b1 = [7,4,3,8,1,12,9,14]
for x in range(0,5000):
    b4 = random.randint(1,99999)
    b1.append(b4)
b5 = timeit.default_timer()
fonk2(b1)
b6 = timeit.default_timer() - b5
print("Merge Sort: " + str(b6))
print(b1)