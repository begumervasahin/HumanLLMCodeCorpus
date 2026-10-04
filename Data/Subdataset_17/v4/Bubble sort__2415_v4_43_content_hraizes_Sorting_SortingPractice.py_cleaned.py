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
    for size in range(len(stack), 1, -1):
        largest = largest_pancake(stack, size)
        if largest != size - 1:
            flip(stack, largest)
            flip(stack, size - 1)
def bubble_sort(alist):
    n = len(alist)
    for passnum in range(n - 1, 0, -1):
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
    pancakes = [3, 6, 2, 8, 4]
    print("Original stack of pancakes:", pancakes)
    pancake_sort(pancakes)
    print("Sorted stack of pancakes:", pancakes)
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("\nOriginal list for bubble sort:", alist)
    bubble_sort(alist)
    print("Sorted list after bubble sort:", alist)
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("\nOriginal list for merge sort:", alist)
    merge_sort(alist)
    print("Sorted list after merge sort:", alist)