def partition(my_list, start, end):
    pivot = my_list[start]
    left = start + 1
    right = end
    while True:
        while left <= right and my_list[left] <= pivot:
            left += 1
        while my_list[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            my_list[left], my_list[right] = my_list[right], my_list[left]
    my_list[start], my_list[right] = my_list[right], my_list[start]
    return right
def quicksort(my_list, start, end):
    global m
    if start < end:
        m += end - start
        split = partition(my_list, start, end)
        m += abs(start - (split - 1))
        quicksort(my_list, start, split - 1)
        m += abs((split + 1) - end)
        quicksort(my_list, split + 1, end)
    return my_list
def main():
    global m
    m = 0
    my_list = [int(x) for x in open("list.txt", "r").readlines()]
    sorted_list = quicksort(my_list, 0, len(my_list) - 1)
    print(sorted_list)
if __name__ == "__main__":
    main()
    print(m)