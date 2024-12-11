import sys
def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if arr[b2] > arr[j]:
                b2 = j
        arr[i], arr[b2] = arr[b2], arr[i]
if b3 = = "__main__":
    b4 = [64, 25, 12, 22, 11]
    fonk1(b4)
    print("Sorted array:", b5 = " ")
    for num in b4:
        print(num, b5 = " ")