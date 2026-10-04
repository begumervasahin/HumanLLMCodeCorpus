def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if arr[b2] > arr[j]:
                b2 = j
        arr[i], arr[b2] = arr[b2], arr[i]
b3 = [64, 25, 12, 22, 11]
fonk1(b3)
print("Sorted array:")
for element in b3:
    print(element)