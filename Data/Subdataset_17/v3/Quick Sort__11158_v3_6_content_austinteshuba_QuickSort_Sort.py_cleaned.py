def partition(my_list, start, end):
    pivot = my_list[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and my_list[left] <= pivot:
            left += 1
        while right >= left and my_list[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            my_list[left], my_list[right] = my_list[right], my_list[left]
    my_list[start], my_list[right] = my_list[right], my_list[start]
    return right
def quicksort(my_list, start, end, operations_count):
    if start < end:
        operations_count += end - start
        split = partition(my_list, start, end)
        operations_count += abs(start - (split - 1))
        my_list, operations_count = quicksort(my_list, start, split - 1, operations_count)
        operations_count += abs((split + 1) - end)
        my_list, operations_count = quicksort(my_list, split + 1, end, operations_count)
    return my_list, operations_count
def main():
    try:
        with open("list.txt", "r") as file:
            my_list = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print("Error: The file 'list.txt' was not found.")
        return
    except ValueError:
        print("Error: The file 'list.txt' contains non-integer values.")
        return
    sorted_list, total_operations = quicksort(my_list, 0, len(my_list) - 1, 0)
    print("Sorted list:", sorted_list)
    print("Total operations:", total_operations)
if __name__ == '__main__':
    main()