def random_number():
    import random
    li = random.sample(xrange(100001), 100)
    return li
random_number()
def SelectionSort(li):
    print li
    for i in range(0,len(li)):
        minIndex = i
        for j in range(i,len(li)):
            if li[j]<li[minIndex]:
                minIndex = j
        temp = li[i]
        li[i] = li[minIndex]
        li[minIndex] = temp
    print li
SelectionSort(random_number())