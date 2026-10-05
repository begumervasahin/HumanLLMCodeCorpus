'''
In the worst case, each pancake needs to be flipped two times. Once to bring it to the top,
and another time to bring it to the bottom. However, the second to last one would need only one
flip, and the very last one would not need to be flipped at all. So T(n) = 2(n-2) + 1 = 2n - 3.
'''
def largestPC(stack,size):
    largestPC = 0
    for pancake in range(0, size):
        if stack[pancake] > stack[largestPC]:
            largestPC = pancake
    return largestPC
def spatula(stack,n):
    for pancake in range(0,(n
        stack[pancake], stack[n] = stack[n], stack[pancake]
        n -= 1
def pancakeSort(stack):
    stackSize = len(stack)
    for i in range(stackSize, 0, -1):
        largest = largestPC(stack, i)
        spatula(stack,largest)
        spatula(stack, stackSize-1)
        stackSize = stackSize - 1
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)
        lefthalf = []
        for i in range(0,mid):
            lefthalf.append(alist[i])
        righthalf = []
        for i in range(mid,len(alist)):
            righthalf.append(alist[i])
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1