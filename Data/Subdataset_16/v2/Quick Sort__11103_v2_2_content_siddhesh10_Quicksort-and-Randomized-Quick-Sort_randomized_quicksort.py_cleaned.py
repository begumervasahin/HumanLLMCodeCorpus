import random
def fonk1(arr, low, high):
    b1 = random.randint(low, high)
    b2 = arr[b1]
    arr[b1], arr[high] = arr[high], arr[b1]
    b3 = low
    for j in range(low, high):
        if arr[j] <= b2:
            arr[b3], arr[j] = arr[j], arr[b3]
            b3 += 1
    arr[b3], arr[high] = arr[high], arr[b3]
    return b3
def fonk2(arr, low, high):
    if low < high:
        b4 = fonk1(arr, low, high)
        fonk2(arr, low, b4 - 1)
        fonk2(arr, b4 + 1, high)
if b5 = = '__main__':
    b6 = [10, 7, 8, 9, 1, 5]
    b7 = len(b6)
    fonk2(b6, 0, b7 - 1)
    print("Sorted array is:")
    print(b6)