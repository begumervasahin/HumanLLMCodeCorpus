def shell_sort(A, verbose=0, desc=0):
    def insertion_sort_with_gap(array, gap):
        for i in range(gap, len(array)):
            current_value = array[i]
            position = i
            while position >= gap and array[position - gap] > current_value:
                array[position] = array[position - gap]
                position -= gap
            array[position] = current_value
    gap = len(A)
    while gap > 0:
        if verbose:
            print(f"Current gap: {gap}")
        insertion_sort_with_gap(A, gap)
        gap
    if desc:
        A.reverse()
    return A
if __name__ == "__main__":
    sample_array = [19, 2, 31, 45, 6, 11, 121, 27]
    sorted_array = shell_sort(sample_array, verbose=1)
    print("Sorted array:", sorted_array)