import time
from random import randint
def fonk1(arr,low,high):
	b1 = ( low-1 )
	b2 = arr[high]
	for j in range(low , high):
		if arr[j] <= b2:
			b1 = b1+1
			arr[b1],arr[j] = arr[j],arr[b1]
	arr[b1+1],arr[high] = arr[high],arr[b1+1]
	return ( b1+1 )
def fonk2(arr,low,high):
	if low < high:
		b3 = fonk1(arr,low,high)
		fonk2(arr, low, b3-1)
		fonk2(arr, b3+1, high)
print("quick sort")
b4 = []
for x in range(10):
    b4.append([])
b5 = []
for x in range(10):
    b5.append([])
b6 = []
for x in range(10):
    b6.append([])
a1 = 100000
b1 = 0
while(a1 <= 10000000):
    for x in range(a1):
        b7 = randint(1, a1)
        b4[b1].append(b7)
    print("Clock {} is ticking....".format(b1+1))
    b5[b1] = time.time()
    fonk2(b4[b1], 0, len(b4[b1]) - 1)
    b6[b1] = time.time()
    print("Time taken for InputSize({}) is {} second ".format(a1, b6[b1] - b5[b1]))
    a1 = a1 + 1100000
    b1 = b1 + 1
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