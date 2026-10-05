""
import datetime
import statistics
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = [arr[0], arr[len(arr)
    b2 = statistics.median(b1)
    b3 = [x for x in arr if x < b2]
    b4 = [x for x in arr if x == b2]
    b5 = [x for x in arr if x > b2]
    return fonk1(b3) + b4 + fonk1(b5)
b6 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
b7 = datetime.datetime.now()
print (fonk1(b6))
b8 = datetime.datetime.now()
print ('time taken', b8-b7)