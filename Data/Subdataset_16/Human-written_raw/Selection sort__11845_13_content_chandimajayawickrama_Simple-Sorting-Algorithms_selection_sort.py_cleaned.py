import time
import random
def fonk1(array):
    b1 = time.time()
    for i in range(0,len(array)-1):
        b2 = i
        for j in range(i+1,len(array)):
            if array[b2] > array[j]:
                b2 = j
        array[i],array[b2] = array[b2],array[i]
    return array