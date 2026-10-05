import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
def merge_sort():
    counts = []
    def merge_sort_recursive(arr):
        nonlocal count
        if len(arr) > 1:
            mid = len(arr)
            left_half = arr[:mid]
            right_half = arr[mid:]
            merge_sort_recursive(left_half)
            merge_sort_recursive(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
                count += 1
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
                count += 1
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
                count += 1
    for file_name in cds.fileNames:
        values = []
        with open(file_name, "r") as reader:
            for value in reader.readlines():
                values.append(int(value))
        count = 0
        merge_sort_recursive(values)
        counts.append(count)
    return counts
def generate_cases(counts):
    best_case = []
    average_case = []
    worst_case = []
    for i in range(len(counts)):
        if i % 9 == 0 or i % 9 == 4:
            best_case.append(counts[i])
    for i in range(len(counts)):
        if i % 9 == 1 or i % 9 == 2 or i % 9 == 3:
            average_case.append(counts[i])
    for i in range(len(counts)):
        if i % 9 == 5:
            worst_case.append(counts[i])
    best_avg_case = [(best_case[i] + best_case[i + 1]) / 2 for i in range(len(best_case) - 1)]
    average_avg_case = [(average_case[i] + average_case[i + 1] + average_case[i + 2]) / 3 for i in range(len(average_case) - 2)]
    sizes = [200, 400, 600, 800, 1000]
    plt.plot(sizes, best_avg_case, '-ro', label="Best Case")
    plt.plot(sizes, average_avg_case, '-bo', label="Average Case")
    plt.plot(sizes, worst_case, '-go', label="Worst Case")
    plt.legend()
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if __name__ == "__main__":
    counts = merge_sort()
    generate_cases(counts)