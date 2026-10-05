class Student:
    def __init__(self, rating, growth):
        self.rating = rating
        self.growth = growth
comparisons = 0
swaps = 0
def bubble_sort(arr):
    global comparisons, swaps
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            comparisons += 1
            if arr[i].rating < arr[i + 1].rating:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
    print("Bubble Sort:\nComparison times:", comparisons, "\nSwap times:", swaps)
    comparisons = 0
    swaps = 0
def partition(pivot_index, start, end, arr):
    global swaps, comparisons
    pivot_value = arr[pivot_index].growth
    arr[pivot_index], arr[end - 1] = arr[end - 1], arr[pivot_index]
    left_ptr = start
    for right_ptr in range(start, end - 1):
        comparisons += 1
        if arr[right_ptr].growth < pivot_value:
            arr[left_ptr], arr[right_ptr] = arr[right_ptr], arr[left_ptr]
            swaps += 1
            left_ptr += 1
    arr[left_ptr], arr[end - 1] = arr[end - 1], arr[left_ptr]
    swaps += 1
    return left_ptr
def quick_sort(start, end, arr):
    global swaps, comparisons
    if start < end:
        pivot_index = (start + end)
        new_pivot_index = partition(pivot_index, start, end, arr)
        quick_sort(start, new_pivot_index, arr)
        quick_sort(new_pivot_index + 1, end, arr)
if __name__ == "__main__":
    students = [
        Student(80, 170),
        Student(75, 165),
        Student(85, 175),
        Student(70, 160),
        Student(90, 180)
    ]
    print("Bubble Sort:")
    bubble_sort(students[:])
    print()
    print("Quick Sort:")
    quick_sort(0, len(students), students)
    print("Comparison times:", comparisons)
    print("Swap times:", swaps)