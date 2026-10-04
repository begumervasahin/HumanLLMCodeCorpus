def shell_sort(A, verbose=0, desc=0):
    def insertion_sort_with_gap(gap, start):
        for i in range(start + gap, len(A), gap):
            current_value = A[i]
            position = i
            while position >= gap and A[position - gap] > current_value:
                A[position] = A[position - gap]
                position -= gap
            A[position] = current_value
    gap = len(A)
    while gap > 0:
        if verbose:
            print(f"Current gap: {gap}")
        for start_position in range(gap):
            insertion_sort_with_gap(gap, start_position)
        gap
    if desc:
        A.reverse()
    return A
if __name__ == "__main__":
    sample_array = [19, 2, 31, 45, 6, 11, 121, 27]
    sorted_array = shell_sort(sample_array, verbose=1)
    print("Sorted array:", sorted_array)