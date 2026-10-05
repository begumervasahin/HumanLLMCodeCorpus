def partition(myList, start, end):
    pivot = myList[start]
    left = start + 1
    right = end
    while True:
        while left <= right and myList[left] <= pivot:
            left += 1
        while myList[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            myList[left], myList[right] = myList[right], myList[left]
    myList[start], myList[right] = myList[right], myList[start]
    return right
def quicksort(myList, start, end):
    if start < end:
        split = partition(myList, start, end)
        quicksort(myList, start, split - 1)
        quicksort(myList, split + 1, end)
    return myList
def main():
    myList = [int(x) for x in open("list.txt", "r").readlines()]
    sortedList = quicksort(myList, 0, len(myList) - 1)
    print(sortedList)
if __name__ == "__main__":
    main()