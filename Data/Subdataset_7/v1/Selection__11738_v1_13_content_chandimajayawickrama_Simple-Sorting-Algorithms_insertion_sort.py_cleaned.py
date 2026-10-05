import time
def fonk1(array):
    b1 = time.time()
    for i in range(1,len(array)):
        b2 = i
        while ((b2>0)and (array[b2]<array[b2-1])):
            array[b2],array[b2-1] = array[b2-1],array[b2]
            b2 = b2-1
    return array
try:
    b3 = input("Enter a list of integers separated by spaces: ").split(' ')
    b3 = [int(x) for x in b3]
    b4 = fonk1(b3)
    print("Sorted list:", b4)
except ValueError:
    print("[]")