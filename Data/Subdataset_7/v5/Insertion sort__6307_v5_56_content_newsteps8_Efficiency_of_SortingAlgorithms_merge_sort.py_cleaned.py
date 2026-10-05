import time
a1 = 0
def fonk1(arr):
    if len(arr) > 1:
        b1 = len(arr)
        b2 = arr[:b1]
        b3 = arr[b1:]
        fonk1(b2)
        fonk1(b3)
        fonk2(arr, b2, b3)
def fonk2(arr, b2, b3):
    global a1
    b4 = j = k = 0
    while b4 < len(b2) and j < len(b3):
        a1 += 1
        if b2[b4] < b3[j]:
            arr[k] = b2[b4]
            b4 += 1
        else:
            arr[k] = b3[j]
            j += 1
        k += 1
    while b4 < len(b2):
        a1 += 1
        arr[k] = b2[b4]
        b4 += 1
        k += 1
    while j < len(b3):
        a1 += 1
        arr[k] = b3[j]
        j += 1
        k += 1
def fonk3(arr):
    for num in arr:
        print(num, b5 = " ")
    print()
if b6 = = '__main__':
    b7 = time.time()
    with open("case") as file:
        b8 = list(map(int, file.read().split()))
    fonk1(b8)
    print("Sorted array:")
    fonk3(b8)
    print("Total comparisons:", a1)
    b9 = time.time()
    print("Execution time:", b9 - b7)