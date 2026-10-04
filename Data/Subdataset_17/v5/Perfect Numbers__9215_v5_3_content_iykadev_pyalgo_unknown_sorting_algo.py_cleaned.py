a_unsorted = [6, 2, 7, 8, 3, 1, 10, 5, 4, 9]
a_sorted = []
while a_unsorted:
    a_min = min(a_unsorted)
    a_unsorted.remove(a_min)
    a_sorted.append(a_min)
print(a_sorted)