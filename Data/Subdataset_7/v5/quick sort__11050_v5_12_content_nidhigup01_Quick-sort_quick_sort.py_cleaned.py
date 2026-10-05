import datetime
import statistics
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = statistics.median([arr[0], arr[len(arr)
    b2 = [x for x in arr if x < b1]
    b3 = [x for x in arr if x == b1]
    b4 = [x for x in arr if x > b1]
    return fonk1(b2) + b3 + fonk1(b4)
b5 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
b6 = datetime.datetime.now()
b7 = fonk1(b5)
b8 = datetime.datetime.now()
print("Sorted list:", b7)
print("Time taken:", b8 - b6)