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
    left_index, right_index, b4 = 0, 0, 0
    while left_index < len(b2) and right_index < len(b3):
        if b2[left_index] > b3[right_index]:
            array[b4] = b3[right_index]
            right_index += 1
        else:
            array[b4] = b2[left_index]
            left_index += 1
        b4 += 1
    fonk1(b2, left_index, array, b4, len(b2) - left_index)
    fonk1(b3, right_index, array, b4, len(b3) - right_index)
b5 = [7, 4, 3, 8, 1, 12, 9, 14]
for _ in range(5000):
    b6 = random.randint(1, 99999)
    b5.append(b6)
b7 = timeit.default_timer()
fonk2(b5)
b8 = timeit.default_timer() - b7
print("Merge Sort Time: " + str(b8))
print(b5)