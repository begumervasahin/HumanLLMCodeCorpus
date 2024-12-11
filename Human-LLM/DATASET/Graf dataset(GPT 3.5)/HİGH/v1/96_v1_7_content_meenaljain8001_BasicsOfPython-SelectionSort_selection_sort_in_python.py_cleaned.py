def fonk1(arr):
    for i in range(len(arr)):
        b1 = i
        for j in range(i + 1, len(arr)):
            if arr[b1] > arr[j]:
                b1 = j
        arr[i], arr[b1] = arr[b1], arr[i]
    return arr
def fonk2():
    b2 = [64, 25, 12, 22, 11]
    b3 = fonk1(b2)
    print("Sorted array:")
    for num in b3:
        print(num, b4 = " ")
if b5 = = "__main__":
    fonk2()