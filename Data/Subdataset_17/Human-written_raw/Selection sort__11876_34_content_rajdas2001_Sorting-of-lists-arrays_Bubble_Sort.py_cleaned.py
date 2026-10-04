def bubbleSort(ar):
    n = len(ar)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]
ar = [110, 34, 25, 32, 28, 10, 90]
bubbleSort(ar)
print("Sorted array is:")
for i in range(len(ar)):
    print("%d" % ar[i]),