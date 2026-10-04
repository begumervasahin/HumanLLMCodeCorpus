class Student:
    def __init__(self, name, rating, growth):
        self.name = name
        self.rating = rating
        self.growth = growth
    def __repr__(self):
        return f"{self.name} (Rating: {self.rating}, Growth: {self.growth})"
comparison_times = 0
swap_times = 0
def bubble_sort(arr):
    global comparison_times, swap_times
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparison_times += 1
            if arr[j].rating < arr[j + 1].rating:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_times += 1
                swapped = True
        if not swapped:
            break
    print(f"BubbleSort\nComparison times: {comparison_times}\nSwap times: {swap_times}")
    comparison_times, swap_times = 0, 0
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def partition(arr, low, high):
    global comparison_times, swap_times
    pivot = arr[high].growth
    i = low - 1
    for j in range(low, high):
        comparison_times += 1
        if arr[j].growth < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swap_times += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swap_times += 1
    return i + 1
if __name__ == '__main__':
    students = [
        Student("Alice", 85, 160),
        Student("Bob", 70, 170),
        Student("Charlie", 90, 155),
        Student("David", 75, 180)
    ]
    print("Original list:")
    print(students)
    bubble_sort(students)
    print("Sorted list by rating (Bubble Sort):")
    print(students)
    students = [
        Student("Alice", 85, 160),
        Student("Bob", 70, 170),
        Student("Charlie", 90, 155),
        Student("David", 75, 180)
    ]
    quick_sort(students, 0, len(students) - 1)
    print(f"QuickSort\nComparison times: {comparison_times}\nSwap times: {swap_times}")
    comparison_times, swap_times = 0, 0
    print("Sorted list by growth (Quick Sort):")
    print(students)