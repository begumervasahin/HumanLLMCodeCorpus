def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lowVal = [x for x in arr if x < pivot]
    pivoter = [x for x in arr if x == pivot]
    highVal = [x for x in arr if x > pivot]
    sorted_low = quicksort(lowVal)
    sorted_high = quicksort(highVal)
    return sorted_low + pivoter + sorted_high
if __name__ == "__main__":
    test_array = [1, 3, 5, 2]
    sorted_array = quicksort(test_array)
    print(sorted_array)
