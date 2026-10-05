import time
import random
def bubble_sort(array):
    start_time = time.time()
    swapped = False
    if len(array)==0:
      array =[]
      return array
    while not swapped :
        for i,val in enumerate(array):
            for j,val1 in enumerate(array):
                if (array[i]>array[j]):
                    array[i],array[j] = array[j],array[i]
                    swapped = True
    return array
try:
    l = input().split(' ')
    l = [int(x) for x in l]
    bubble_sort(l)
except:
    print("[]")
bubble_sort(l)