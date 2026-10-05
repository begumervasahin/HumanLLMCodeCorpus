import statistics
def pivot_position(givenlist,first,last) :
    low = givenlist[first]
    high = givenlist[last]
    mid = (first + last)
    pivot_val = statistics.median([low,givenlist[mid],high])
    if pivot_val == low :
        pivot_index = first
    elif pivot_val == high :
        pivot_index = last
    else :
        pivot_index = mid
    givenlist[last],givenlist[pivot_index] = givenlist[pivot_index], givenlist[last]
    pivot = givenlist[last]
    left = first
    right = last-1
    while True:
        while left<=right and givenlist[left] <= pivot:
            left = left + 1
        while left<=right and givenlist[right] >= pivot:
            right = right-1
        if right<left :
            break
        else :
            givenlist[left], givenlist[right] = givenlist[right], givenlist[left]
    givenlist[first], givenlist[right] = givenlist[right], givenlist[first]
    return right
def quicksort(givenlist,first,last) :
    if first<last :
        p = pivot_position(givenlist,first,last)
        quicksort(givenlist,first,p-1)
        quicksort(givenlist,p+1,last)
givenlist = [56,26,93,17,31,44]
n = len(givenlist)
quicksort(givenlist,0,n-1)
print(givenlist)