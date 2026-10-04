from Student import Student
comparison_times = 0
swap_times = 0
def bubble_sort(arr):
    global comparison_times, swap_times
    n = len(arr)
    for i in range(n):
        sorted = True
        for j in range(n - 1 - i):
            comparison_times += 1
            if int(arr[j].rating) < int(arr[j + 1].rating):
                swap_times += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False
        if sorted:
            break
    print(f"BubbleSort\nComparison times: {comparison_times}\nSwap times: {swap_times}")
    comparison_times = 0
    swap_times = 0
def partition(arr, low, high):
    global comparison_times, swap_times
    pivot = arr[high].growth
    i = low - 1
    for j in range(low, high):
        comparison_times += 1
        if int(arr[j].growth) <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swap_times += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swap_times += 1
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
if __name__ == '__main__':
    students = [Student(f'Student{i}', rating=i, growth=i * 2) for i in range(1, 6)]
    print("Original List (Bubble Sort):", [(student.name, student.rating) for student in students])
    bubble_sort(students)
    print("Sorted by Bubble Sort:", [(student.name, student.rating) for student in students])
    students = [Student(f'Student{i}', rating=6 - i, growth=i * 2) for i in range(1, 6)]
    print("Original List (Quick Sort):", [(student.name, student.growth) for student in students])
    quick_sort(students, 0, len(students) - 1)
    print("Sorted by Quick Sort:", [(student.name, student.growth) for student in students])