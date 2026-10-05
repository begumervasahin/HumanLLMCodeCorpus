import datetime
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
quick_sort_config = config['quicksort']
bubble_sort_config = config['bubblesort']
quick_sort_elements = int(quick_sort_config['elements'])
quick_sort_step = int(quick_sort_config['step'])
quick_sort_iteration = int(quick_sort_config['iter'])
bubble_sort_elements = int(bubble_sort_config['elements'])
bubble_sort_step = int(bubble_sort_config['step'])
bubble_sort_iteration = int(bubble_sort_config['iter'])
def open_input_file(input_file):
    with open(input_file, "r") as f:
        data = eval(f.readline())
    return data
def bubble_sort_algorithm(element_list, n):
    for i in range(n):
        for j in range(n - i - 1):
            if element_list[j] > element_list[j + 1]:
                element_list[j], element_list[j + 1] = element_list[j + 1], element_list[j]
def quick_sort_algorithm(element_list, l=0, r=None):
    if r is None:
        r = len(element_list) - 1
    i, j = l, r
    mid = (l + r)
    pivot = element_list[mid]
    while i <= j:
        while element_list[i] < pivot:
            i += 1
        while element_list[j] > pivot:
            j -= 1
        if i <= j:
            element_list[i], element_list[j] = element_list[j], element_list[i]
            i += 1
            j -= 1
    if l < j:
        quick_sort_algorithm(element_list, l, j)
    if r > i:
        quick_sort_algorithm(element_list, i, r)
def main():
    data = open_input_file("input.txt")
    ans = True
    while ans:
        print()
        ans = input()
        if ans == "1":
            print("Sorting with Bubble Sort")
            start = datetime.datetime.now()
            for i in range(0, bubble_sort_elements + bubble_sort_step, bubble_sort_step):
                for x in range(bubble_sort_elements):
                    bubble_sort_algorithm(data, i)
            end = datetime.datetime.now() - start
            print(data)
            print("Sorted in " + str(end.seconds) + " seconds.")
        elif ans == "2":
            print("Sorting with Quick Sort")
            start = datetime.datetime.now()
            for j in range(0, quick_sort_elements + quick_sort_step, quick_sort_step):
                for i in range(quick_sort_iteration):
                    quick_sort_algorithm(data, 0, j - 1)
            end = datetime.datetime.now() - start
            print(data)
            print("Sorted in " + str(end.seconds) + " seconds.")
        elif ans == "w":
            print("Exiting program.")
            break
        elif ans != "":
            print("Unknown option")
if __name__ == '__main__':
    main()