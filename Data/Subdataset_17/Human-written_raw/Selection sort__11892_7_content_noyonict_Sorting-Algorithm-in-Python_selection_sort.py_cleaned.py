def selection_sort(a):
    for i in range(0, len(a)-1):
        min_index = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
array = [12, 3, 43, 43, 9, 3, 2, 2, 43, 23, 53, 3, 3, 23, 23, 12, 53, 91, 1]
print(array)
selection_sort(array)
print(array)