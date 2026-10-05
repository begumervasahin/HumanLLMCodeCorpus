import time
from random import randint
def partition(arr,low,high):
	i = ( low-1 )
	pivot = arr[high]
	for j in range(low , high):
		if arr[j] <= pivot:
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]
	arr[i+1],arr[high] = arr[high],arr[i+1]
	return ( i+1 )
def quickSort(arr,low,high):
	if low < high:
		pi = partition(arr,low,high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)
print("quick sort")
randlist = []
for x in range(10):
    randlist.append([])
startTimeList = []
for x in range(10):
    startTimeList.append([])
endTimeList = []
for x in range(10):
    endTimeList.append([])
inputSize = 100000
i = 0
while(inputSize <= 10000000):
    for x in range(inputSize):
        num = randint(1, inputSize)
        randlist[i].append(num)
    print("Clock {} is ticking....".format(i+1))
    startTimeList[i] = time.time()
    quickSort(randlist[i], 0, len(randlist[i]) - 1)
    endTimeList[i] = time.time()
    print("Time taken for InputSize({}) is {} second ".format(inputSize, endTimeList[i] - startTimeList[i]))
    inputSize = inputSize + 1100000
    i = i + 1
'''
From 100k to 10M
1.  100000
2.  1200000
3.  2300000
4.  3400000
5.  4500000
6.  5600000
7.  6700000
8.  7800000
9.  8900000
10. 10000000
'''