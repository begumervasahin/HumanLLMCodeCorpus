import datetime
import statistics
def fonk1(arr):
    if len(arr) <= 1:
        return arr
    first, b4, b1 = arr[0], arr[len(arr)
    b2 = statistics.median([first, b4, b1])
    b3 = [x for x in arr if x < b2]
    b4 = [x for x in arr if x == b2]
    b5 = [x for x in arr if x > b2]
    return fonk1(b3) + b4 + fonk1(b5)
if b6 = = "__main__":
    b7 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    b8 = datetime.datetime.now()
    b9 = fonk1(b7)
    b10 = datetime.datetime.now()
    print("Sorted array:", b9)
    print("Time taken:", b10 - b8)