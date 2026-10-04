def largest_pancake(stack, size):
    largest_index = 0
    for i in range(size):
        if stack[i] > stack[largest_index]:
            largest_index = i
    return largest_index
def flip(stack, n):
    start = 0
    while start < n:
        stack[start], stack[n] = stack[n], stack[start]
        start += 1
        n -= 1
def pancake_sort(stack):
    size = len(stack)
    for current_size in range(size, 1, -1):
        largest_index = largest_pancake(stack, current_size)
        if largest_index != current_size - 1:
            flip(stack, largest_index)
            flip(stack, current_size - 1)
def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
if __name__ == '__main__':
    pancake_stack = [3, 6, 1, 9, 7, 4, 8]
    print("Original pancake stack:", pancake_stack)
    pancake_sort(pancake_stack)
    print("Sorted pancake stack:", pancake_stack)
    bubble_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list for bubble sort:", bubble_list)
    bubble_sort(bubble_list)
    print("Sorted list using bubble sort:", bubble_list)
    merge_list = [38, 27, 43, 3, 9, 82, 10]
    print("Original list for merge sort:", merge_list)
    merge_sort(merge_list)
    print("Sorted list using merge sort:", merge_list)