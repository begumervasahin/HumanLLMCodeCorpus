import time
import random
def mergeSort(arr):
	if len(arr)>1:
		mid = len(arr)
		lHalf = arr[:mid]
		rHalf = arr[mid:]
		mergeSort(lHalf)
		mergeSort(rHalf)
		i = j = k = 0
		while ((i < len(lHalf)) and (j < len(rHalf))):
			if lHalf[i] < rHalf[j]:
				arr[k]=lHalf[i]
				i += 1
			else:
				arr[k]=rHalf[j]
				j += 1
			k += 1
		while i < len(lHalf):
			arr[k]=lHalf[i]
			i += 1
			k += 1
		while j < len(rHalf):
			arr[k]=rHalf[j]
			j += 1
			k += 1
def insertionSort(arr):
	for i in range(1, len(arr)):
		curVal = arr[i]
		pos = i
		while ((pos > 0) and (arr[pos-1] > curVal)):
			arr[pos] = arr[pos-1]
			pos -= 1
		arr[pos] = curVal
arrSize = [0,2000,8000,32000,128000,512000,1024000,4096000]
for i in arrSize:
	arr = []
	for index in range(i):
		arr.append(random.randint(1,1000))
	mt1 = time.time()
	mergeSort(arr)
	mt2 = time.time()
	mT = mt2 - mt1
	it1 = time.time()
	insertionSort(arr)
	it2 = time.time()
	iT = it2 - it1
	print ("Size i: "),
	print (i)
	print ("Merge Time: "),
	print (mT)
	print ("Insertion Time: "),
	print (iT)
	print ("\n")