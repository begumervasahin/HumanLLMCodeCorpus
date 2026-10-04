import random
def fonk1(b1 = 100, upper_limit=100000):
    return random.sample(range(upper_limit + 1), b1)
def fonk2(arr):
    b2 = len(arr)
    for i in range(b2):
        b3 = i
        for j in range(i + 1, b2):
            if arr[j] < arr[b3]:
                b3 = j
        arr[i], arr[b3] = arr[b3], arr[i]
    return arr
def fonk3():
    b4 = fonk1()
    print("Original list:")
    print(b4)
    b5 = fonk2(b4)
    print("Sorted list:")
    print(b5)
if b6 = = "__main__":
    fonk3()