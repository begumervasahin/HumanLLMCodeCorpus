def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)
if __name__ == "__main__":
    test_array = [1, 3, 5, 2]
    sorted_array = quicksort(test_array)
    print(sorted_array)
