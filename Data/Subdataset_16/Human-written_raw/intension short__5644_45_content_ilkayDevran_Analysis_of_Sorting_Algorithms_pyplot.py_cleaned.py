import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
a1 = 0
a2 = 0
def fonk1():
	print
	b1 = int(raw_input('>>> '))
	if b1 = = 4:
		fonk8(b1, fonk2(1,1))
	else:
		a1 = fonk6()
		a2 = fonk7()
		print '\n','Array Size: ', 10**a1, "Range 0 -",10**a2
		b2 = fonk2(10**a2,10**a1)
		fonk8(b1, b2)
def fonk2(length,a2):
	from random import randint
	b3 = [randint(0,length) for i in range(a2)]
	return b3
def fonk3(list):
	b4 = time.time()
	insertion_sort.insertionSort(list)
	b5 = (time.time() - b4)
	print("\nInsertion Sort --- %s  ---\n" % b5)
	print("\n")
def fonk4(list):
	b4 = time.time()
	selection_sort.selectionSort(list)
	b6 = (time.time() - b4)
	print("\nSelection Sort --- %s  ---\n" % b6)
	print("\n")
def fonk5(list):
	b4 = time.time()
	MERGE.mergeSort(list)
	b7 = (time.time() - b4)
	print("\nMerge Sort --- %s  ---\n" % b7)
	print("\n")
def fonk6():
	try:
		return int(raw_input('Enter the array a1 (10**a1): '))
	except ValueError:
		print "Not a number"
		return 0
def fonk7():
	try:
		return int(raw_input('Define the range (0 to ...): '))
	except ValueError:
		print "Not a number"
		return 0
def fonk8(b1,list):
	if b1 = = 1:
		return fonk3(list)
	elif b1 = = 2:
		return fonk4(list)
	elif b1 = = 3:
		return fonk5(list)
	elif b1 = = 4:
		return fonk9()
	else:
		print "Wrong sort code"
		return
def fonk9():
	allInOne.drawAllGraph()
if b8 = = '__main__':
	fonk1()