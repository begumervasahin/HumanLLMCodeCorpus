import time
import random
def fonk1(array):
    b1 = time.time()
    for i in range(1,len(array)):
        b2 = i
        while ((b2>0)and (array[b2]<array[b2-1])):
            array[b2],array[b2-1] = array[b2-1],array[b2]
            b2 = b2-1
    return array