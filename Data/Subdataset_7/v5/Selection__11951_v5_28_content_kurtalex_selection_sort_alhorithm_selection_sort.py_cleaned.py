def fonk1(arr):
    b1 = arr[0]
    a1 = 0
    for i in range(1, len(arr)):
        if arr[i] < b1:
            b1 = arr[i]
            a1 = i
    return a1
def fonk2(arr):
    b2 = []
    for _ in range(len(arr)):
        b1 = fonk1(arr)
        b2.append(arr.pop(b1))
    return b2
if b3 = = "__main__":
    b4 = [5, 3, 6, 2, 10]
    b5 = fonk2(b4)
    print(b5)