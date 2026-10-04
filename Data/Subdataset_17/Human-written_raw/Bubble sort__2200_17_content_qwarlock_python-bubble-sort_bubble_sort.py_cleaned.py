counter = 0
def bubbleSort(list,counter):
    n = len(list)
    swapped = False
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            counter += 1
            if list[j] > list[j+1]:
                swapped=True
                swap = list[j]
                list[j] = list[j+1]
                list[j+1] = swap
            if swapped == False:
                break
    return counter
list = [1,2,3,4,5,6,7,8,9,10,]
print(list)
counter = bubbleSort(list,counter)
print(list)
print counter