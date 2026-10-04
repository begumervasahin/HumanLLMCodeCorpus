def bubble_sort(lst):
    n = len(lst)
    counter = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            counter += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return counter
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", lst)
iterations = bubble_sort(lst)
print("Sorted list:", lst)
print("Number of iterations:", iterations)