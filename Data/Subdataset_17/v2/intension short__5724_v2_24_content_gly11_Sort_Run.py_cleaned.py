import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
with open("NUM.txt", "r") as file:
    document = file.read()
    list_b = [int(num) for num in document.split()]
list_i = list_b.copy()
start_b = time.process_time()
bubble_sort(list_b)
end_b = time.process_time()
running_time_b = end_b - start_b
start_i = time.process_time()
insertion_sort(list_i)
end_i = time.process_time()
running_time_i = end_i - start_i
with open("BUBBLE_SORTED.txt", "w") as file_bubble:
    file_bubble.write(" ".join(map(str, list_b)) + "\n")
    file_bubble.write(f"Running time: {running_time_b} Seconds\n")
with open("INSERTION_SORTED.txt", "w") as file_insertion:
    file_insertion.write(" ".join(map(str, list_i)) + "\n")
    file_insertion.write(f"Running time: {running_time_i} Seconds\n")