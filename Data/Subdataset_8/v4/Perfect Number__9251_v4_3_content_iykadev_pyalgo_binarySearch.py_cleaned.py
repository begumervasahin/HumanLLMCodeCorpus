def binary_search(sorted_list, target):
    first = 0
    last = len(sorted_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)
        if sorted_list[midpoint] == target:
            found = True
        else:
            if target < sorted_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))