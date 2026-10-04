from Student import Student
comparison_times = 0
swap_times = 0
def bubble_sort(arr):
    global comparison_times, swap_times
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            comparison_times += 1
            if int(arr[i].rating) < int(arr[i + 1].rating):
                swap_times += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    print("BubbleSort\nComparison times:", comparison_times, "\nSwap times:", swap_times)
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
    students = [Student('Student' + str(i), rating=i, growth=i * 2) for i in range(1, 6)]
    print("Original List:", [(student.name, student.rating) for student in students])
    bubble_sort(students)
    print("Sorted by Bubble Sort:", [(student.name, student.rating) for student in students])
    students = [Student('Student' + str(i), rating=6 - i, growth=i * 2) for i in range(1, 6)]
    print("Original List:", [(student.name, student.growth) for student in students])
    quick_sort(students, 0, len(students) - 1)
    print("Sorted by Quick Sort:", [(student.name, student.growth) for student in students])