def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        for j in range(0, b1-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
b2 = [100, 2993, 22, 1, 82, 11, 33]
fonk1(b2)
print("sorted:")
for i in range(len(b2)):
    print("%d" % b2[i], b3 = ' ')