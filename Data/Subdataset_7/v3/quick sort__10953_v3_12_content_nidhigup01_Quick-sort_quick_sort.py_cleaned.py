import datetime
import statistics
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    b1 = fonk2(arr)
    b4, b5, b2 = fonk3(arr, b1)
    return fonk1(b4) + b5 + fonk1(b2)
def fonk2(arr):
    b3 = [arr[0], arr[len(arr)
    return statistics.median(b3)
def fonk3(arr, b1):
    b4 = [x for x in arr if x < b1]
    b5 = [x for x in arr if x == b1]
    b2 = [x for x in arr if x > b1]
    return b4, b5, b2
def fonk4():
    b6 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    b7 = datetime.datetime.now()
    b8 = fonk1(b6)
    b9 = datetime.datetime.now()
    print("Sorted list:", b8)
    print("Time taken:", b9 - b7)
if b10 = = "__main__":
    fonk4()