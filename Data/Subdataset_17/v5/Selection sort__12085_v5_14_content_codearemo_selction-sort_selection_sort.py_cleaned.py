def selection_sort(items):
    n = len(items)
    for step in range(n):
        min_index = step
        for i in range(step + 1, n):
            if items[i] < items[min_index]:
                min_index = i
        items[step], items[min_index] = items[min_index], items[step]
    print("Sorted items:", items)
    print("Total number of items:", n)
items = [64, 25, 12, 22, 11]
selection_sort(items)