def bubble_sort(lst):
    n = len(lst)
    iteration_count = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            iteration_count += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return iteration_count
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", sample_list)
iterations = bubble_sort(sample_list)
print("Sorted list:", sample_list)
print("Number of iterations:", iterations)