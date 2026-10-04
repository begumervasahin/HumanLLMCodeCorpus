def insertionSort(ar):
    for i in range(1, len(ar)):
        item = ar[i]
        j = i - 1
        while j >= 0 and item < ar[j]:
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = item
ar = [32, 13, 14, 15, 98]
insertionSort(ar)
print("Sorted array is:")
for i in range(len(ar)):
    print("%d" % ar[i])