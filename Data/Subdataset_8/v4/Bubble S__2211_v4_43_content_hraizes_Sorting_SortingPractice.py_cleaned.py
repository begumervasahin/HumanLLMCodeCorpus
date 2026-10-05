
def find_largest_pancake(stack, size):
    largest_pancake_index = 0
    for pancake in range(size):
        if stack[pancake] > stack[largest_pancake_index]:
            largest_pancake_index = pancake
    return largest_pancake_index
def flip_stack(stack, n):
    for pancake in range(n
        stack[pancake], stack[n] = stack[n], stack[pancake]
        n -= 1
def pancake_sort(stack):
    stack_size = len(stack)
    for i in range(stack_size, 0, -1):
        largest = find_largest_pancake(stack, i)
        flip_stack(stack, largest)
        flip_stack(stack, stack_size - 1)
        stack_size -= 1
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
        i = j = k = 0
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
if __name__ == "__main__":
    stack = [3, 1, 5, 4, 2]
    print("Original stack:", stack)
    pancake_sort(stack)
    print("After pancake sorting:", stack)
    alist = [54,26,93,17,77,31,44,55,20]
    print("Original list:", alist)
    bubble_sort(alist)
    print("After bubble sorting:", alist)
    another_list = [54,26,93,17,77,31,44,55,20]
    print("Original list:", another_list)
    merge_sort(another_list)
    print("After merge sorting:", another_list)