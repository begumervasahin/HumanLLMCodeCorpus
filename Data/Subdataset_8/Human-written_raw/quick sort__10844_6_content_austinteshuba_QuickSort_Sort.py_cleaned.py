def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right
m=0
def quicksort(myList, start, end):
    global m
    if start < end:
        m+=end-start
        split = partition(myList, start, end)
        m+=abs(start-(split-1))
        quicksort(myList, start, split-1)
        m+=abs((split+1)-end)
        quicksort(myList, split+1, end)
    return myList
'''
def partition(myList, start, end):
    pivot = myList[start]
    print("pivot!", pivot)
    i = start+1
    j = start
    right = end
    finished=False
    while right>j:
        print("compare", pivot, myList[right], right, j)
        if myList[right]<pivot:
             myList = myList[:start] + [myList[right]] + myList[start:]
             del myList[right+1]
             right+=1
                if right!=len(myList)-1:
                    myList = [myList[:j]] + [myList[right]]+ [myList[j]] + [myList[j+1:right]] + [myList[right+1:]]
                else:
                    myList = myList[:j] + [myList[right]] + [myList[j]] + [myList[j+1:right]]
             j+=1
        right-=1
        print(myList)
    return j
def quicksort(myList, start, end):
    if end>start:
        split = partition(myList, start, end)
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList
'''
def main():
    myList = [int(x) for x in open("list.txt", "r").readlines()]
    sortedList = quicksort(myList,0,len(myList)-1)
    print(sortedList)
main()
print(m)