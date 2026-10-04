import random
def fonk1():
    return random.sample(range(100001), 100)
def fonk2(arr):
    b1 = len(arr)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if arr[j] < arr[b2]:
                b2 = j
        arr[i], arr[b2] = arr[b2], arr[i]
    return arr
def fonk3():
    b3 = fonk1()
    print("Unsorted list:")
    print(b3)
    b4 = fonk2(b3)
    print("Sorted list:")
    print(b4)
if b5 = = "__main__":
    fonk3()