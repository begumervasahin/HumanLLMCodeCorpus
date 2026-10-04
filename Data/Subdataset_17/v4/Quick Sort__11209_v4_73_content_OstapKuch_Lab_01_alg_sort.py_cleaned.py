from Student import Student
comparasion_times = 0
swap_times = 0
def bubble_sort(arr):
    global comparasion_times, swap_times
    is_sorted = True
    for i in range(len(arr) - 1):
        comparasion_times += 1
        if int(arr[i].rating) < int(arr[i + 1].rating):
            swap_times += 1
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            is_sorted = False
    if not is_sorted:
        bubble_sort(arr)
    else:
        print(f"BubbleSort\nComparison times: {comparasion_times}\nSwap times: {swap_times}")
        comparasion_times = 0
        swap_times = 0
def partition(arr, low, high):
    global swap_times, comparasion_times
    pivot = int(arr[low].growth)
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and int(arr[left].growth) <= pivot:
            comparasion_times += 1
            left += 1
        while int(arr[right].growth) >= pivot and right >= left:
            comparasion_times += 1
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
            swap_times += 1
    arr[low], arr[right] = arr[right], arr[low]
    swap_times += 1
    return right
def quick_sort(arr, low, high):
    if low < high:
        split_point = partition(arr, low, high)
        quick_sort(arr, low, split_point - 1)
        quick_sort(arr, split_point + 1, high)
    if low == 0 and high == len(arr) - 1:
        print(f"QuickSort\nComparison times: {comparasion_times}\nSwap times: {swap_times}")
        global comparasion_times, swap_times
        comparasion_times = 0
        swap_times = 0
if __name__ == '__main__':
    students = [
        Student("Alice", 90, 5.6),
        Student("Bob", 85, 5.8),
        Student("Charlie", 92, 5.7),
    ]
    print("Before Bubble Sort:")
    for student in students:
        print(f"{student.name}: {student.rating}")
    bubble_sort(students)
    print("After Bubble Sort:")
    for student in students:
        print(f"{student.name}: {student.rating}")
    students = [
        Student("Alice", 90, 5.6),
        Student("Bob", 85, 5.8),
        Student("Charlie", 92, 5.7),
    ]
    print("\nBefore Quick Sort:")
    for student in students:
        print(f"{student.name}: {student.growth}")
    quick_sort(students, 0, len(students) - 1)
    print("After Quick Sort:")
    for student in students:
        print(f"{student.name}: {student.growth}")