import random
RED = "\x1B[31m"
GREEN = "\x1B[32m"
RESET = "\x1B[0m"
def main():
    print("------------------")
    print("| codedrome.com  |")
    print("| Selection Sort |")
    print("------------------\n")
    data = populate_data()
    selection_sort(data)
def populate_data():
    data = []
    for i in range(0, 16):
        data.append(random.randint(1, 99))
    return data
def print_data(data, sortedto):
    for i in range(0, len(data)):
        if i < sortedto:
            print(GREEN + "%-3d " % data[i] + RESET, end="")
        else:
            print(RED + "%-3d " % data[i] + RESET, end="")
    print("\n")
def selection_sort(data):
    print("Unsorted...")
    print_data(data, 0)
    print("Selection Sorting...")
    sorted_to = 0
    while sorted_to < len(data) - 1:
        index_of_lowest = find_lowest_index(data, sorted_to)
        swap(data, sorted_to, index_of_lowest)
        sorted_to += 1
        print_data(data, sorted_to)
    print("Sorted!")
def swap(data, i1, i2):
    if i1 != i2:
        data[i1], data[i2] = data[i2], data[i1]
def find_lowest_index(data, start):
    lowest_index = start
    for i in range(start, len(data)):
        if data[i] < data[lowest_index]:
            lowest_index = i
    return lowest_index
if __name__ == "__main__":
    main()