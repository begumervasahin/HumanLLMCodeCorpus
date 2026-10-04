import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def read_numbers_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()
    return [int(num) for num in content.split()]
def write_sorted_numbers_to_file(filename, sorted_list, running_time):
    with open(filename, "w") as file:
        file.write(" ".join(map(str, sorted_list)) + "\n")
        file.write(f"Running time: {running_time} Seconds\n")
def main():
    numbers = read_numbers_from_file("NUM.txt")
    bubble_sorted_numbers = numbers.copy()
    start_time = time.process_time()
    bubble_sort(bubble_sorted_numbers)
    bubble_sort_time = time.process_time() - start_time
    write_sorted_numbers_to_file("BUBBLE_SORTED.txt", bubble_sorted_numbers, bubble_sort_time)
    insertion_sorted_numbers = numbers.copy()
    start_time = time.process_time()
    insertion_sort(insertion_sorted_numbers)
    insertion_sort_time = time.process_time() - start_time
    write_sorted_numbers_to_file("INSERTION_SORTED.txt", insertion_sorted_numbers, insertion_sort_time)
if __name__ == "__main__":
    main()