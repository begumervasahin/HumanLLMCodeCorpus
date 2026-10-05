def quicksort(arr):
    def partition(arr, first, last):
        pivot_value = arr[first]
        left_mark = first + 1
        right_mark = last
        while True:
            while left_mark <= right_mark and arr[left_mark] <= pivot_value:
                left_mark += 1
            while arr[right_mark] >= pivot_value and right_mark >= left_mark:
                right_mark -= 1
            if right_mark < left_mark:
                break
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]
        arr[first], arr[right_mark] = arr[right_mark], arr[first]
        return right_mark
    def quicksort_helper(arr, first, last):
        if first < last:
            split_point = partition(arr, first, last)
            quicksort_helper(arr, first, split_point - 1)
            quicksort_helper(arr, split_point + 1, last)
    quicksort_helper(arr, 0, len(arr) - 1)
if __name__ == "__main__":
    arr = [57, 26, 93, 77, 33, 44, 50, 20]
    quicksort(arr)
    print(arr)