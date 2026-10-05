import statistics
def pivot_position(given_list, first, last):
    low = given_list[first]
    high = given_list[last]
    mid = (first + last)
    pivot_val = statistics.median([low, given_list[mid], high])
    if pivot_val == low:
        pivot_index = first
    elif pivot_val == high:
        pivot_index = last
    else:
        pivot_index = mid
    given_list[last], given_list[pivot_index] = given_list[pivot_index], given_list[last]
    pivot = given_list[last]
    left = first
    right = last - 1
    while left <= right:
        while left <= right and given_list[left] <= pivot:
            left += 1
        while left <= right and given_list[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            given_list[left], given_list[right] = given_list[right], given_list[left]
    given_list[first], given_list[right] = given_list[right], given_list[first]
    return right
def quicksort(given_list, first, last):
    if first < last:
        pivot = pivot_position(given_list, first, last)
        quicksort(given_list, first, pivot - 1)
        quicksort(given_list, pivot + 1, last)
if __name__ == "__main__":
    given_list = [56, 26, 93, 17, 31, 44]
    n = len(given_list)
    quicksort(given_list, 0, n - 1)
    print(given_list)