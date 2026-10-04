import random
import time
def fonk1(arr, start, end):
    if start < end:
        b1 = fonk2(arr, start, end)
        fonk1(arr, start, b1)
        fonk1(arr, b1 + 1, end)
def fonk2(arr, start, end):
    b2 = arr[start]
    b3 = start - 1
    b4 = end + 1
    while True:
        b3 += 1
        while arr[b3] < b2:
            b3 += 1
        b4 -= 1
        while arr[b4] > b2:
            b4 -= 1
        if b3 >= b4:
            return b4
        arr[b3], arr[b4] = arr[b4], arr[b3]
def fonk3(arr, start, end):
    if start < end:
        b2 = arr[start]
        low, mid, b5 = start, start, end
        while mid <= b5:
            if arr[mid] < b2:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == b2:
                mid += 1
            else:
                arr[mid], arr[b5] = arr[b5], arr[mid]
                b5 -= 1
        fonk3(arr, start, low - 1)
        fonk3(arr, b5 + 1, end)
def fonk4():
    print()
    b6 = int(input("Enter the list size: "))
    b7 = int(input("Enter the maximum element number for the list (minimum is set to 1): \b6"
                  "(Hint: Lower numbers result in more duplicate elements for speed testing): "))
    b8 = [random.randint(1, b7) for _ in range(b6)]
    b9 = b8[:]
    b10 = time.time()
    fonk1(b8, 0, b6 - 1)
    b11 = time.time()
    print("\nTime taken for 2-way sort: %.8f seconds" % (b11 - b10))
    b12 = time.time()
    fonk3(b9, 0, b6 - 1)
    b13 = time.time()
    print("\nTime taken for 3-way sort: %.8f seconds" % (b13 - b12))
    print()
if b14 = = "__main__":
    fonk4()