import time
import random
import sys
def fonk1(arr):
    for b11 in range(len(arr)):
        for b3 in range(len(arr)-b11-1):
            if arr[b3]>arr[b3+1]:
                arr[b3],arr[b3+1] = arr[b3+1],arr[b3]
def fonk2(arr):
    for b11 in range(len(arr)-1):
        b1 = b11
        for b3 in range(b11+1,len(arr)):
            if arr[b3]<arr[b1]:
                b1 = b3
        arr[b11],arr[b1] = arr[b1],arr[b11]
def fonk3(arr):
    for b11 in range(1,len(arr)):
        b2 = arr[b11]
        b3 = b11-1
        while (b3>=0 and arr[b3]>b2):
            arr[b3+1] = arr[b3]
            b3 -= 1
        arr[b3+1] = b2
def fonk4(arr, b14, b9, b15):
    b4 = b9 - b14 + 1
    b5 = b15 - b9
    b6 = []
    b7 = []
    for b11 in range(b4):
        b6.append(arr[b14 + b11])
    for b3 in range(b5):
        b7.append(arr[b9 + 1 + b3])
    b11,b3,b8 = 0,0,b14
    while (b11<b4 and b3<b5):
        if b6[b11] <= b7[b3]:
            arr[b8] = b6[b11]
            b11+=1
        else:
            arr[b8] = b7[b3]
            b3+=1
        b8+=1
    while (b11<b4):
        arr[b8] = b6[b11]
        b11+=1
        b8+=1
    while (b3 < b5):
        arr[b8] = b7[b3]
        b3+=1
        b8+=1
def fonk5(arr, b14, b15):
    if b14<b15:
        b9 = b14 + (b15-b14)
        fonk5(arr, b14, b9)
        fonk5(arr, b9+1, b15)
        fonk4(arr, b14, b9, b15)
def fonk6(arr):
    fonk5(arr, 0, len(arr)-1)
def fonk7(arr, low, high):
    b10 = arr[high]
    b11 = low - 1
    for b3 in range(low, high):
        if arr[b3]<=b10:
            b11+=1
            arr[b11], arr[b3] = arr[b3], arr[b11]
    arr[b11+1], arr[high] = arr[high], arr[b11+1]
    return b11+1
def fonk8(arr,low,high):
    if low<high:
        b12 = fonk7(arr,low, high)
        fonk8(arr,low,b12-1)
        fonk8(arr, b12+1, high)
def fonk9(arr):
    fonk8(arr,0,len(arr)-1)
def fonk10(arr, b16, b11):
    b13 = b11
    b14 = 2*b11 + 1
    b15 = 2*b11 + 2
    if(b14<b16 and arr[b14]>arr[b13]):
        b13 = b14
    if(b15<b16 and arr[b15]>arr[b13]):
        b13 = b15
    if(b13 != b11):
        arr[b11], arr[b13] = arr[b13], arr[b11]
        fonk10(arr, b16, b13)
def fonk11(arr):
    b16 = len(arr)
    for b11 in range((b16
        fonk10(arr, b16, b11)
    for b11 in range(b16-1, -1, -1):
        arr[0], arr[b11] = arr[b11], arr[0]
        fonk10(arr, b11, 0)
if b17 = = "__main__":
    sys.setrecursionlimit(10000000)
    a1 = 0
    b18 = []
    for b11 in range(4000):
        b18.append(random.randrange(0,1000000000))
    b18.sort()
    for b11 in range(100000
        b19 = b18.copy()
        b20 = time.time()
        fonk9(b19)
        a1 += time.time()-b20
    print("Time taken is "+str(a1/(100000
    print(b19)
    sys.setrecursionlimit(1000)