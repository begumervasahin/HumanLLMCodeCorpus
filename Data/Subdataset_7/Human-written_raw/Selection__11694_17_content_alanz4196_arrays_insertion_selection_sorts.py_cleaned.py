import time
import random
def fonk1(arr):
    for k in range (0, len(arr)-1):
        b1 = k
        b2 = k+1
        while (b2 < len(arr)):
            if arr[b2] < arr[b1]:
                b1 = b2
            b2+=1
        b3 = arr[b1]
        arr[b1] = arr[k]
        arr[k] = b3
    return arr
def fonk2(arr):
    for k in range(1, len(arr)):
        b4 = arr[k]
        b5 = k
        while b5 > 0 and arr[b5-1] > b4:
            arr[b5] = arr[b5-1]
            b5 = b5 - 1
        arr[b5] = b4
    return arr
if b6 = = '__main__':
    a1 = 0
    a2 = 100
    a3 = 0.0
    a4 = 0.0
    b7 = [0] * 6
    b8 = int(input('How many values should be generated? '))
    b9 = [0] * b8
    b10 = [0] * b8
    b11 = [0] * b8
    b12 = [0] * b8
    b13 = [0] * b8
    b14 = [0] * b8
    b15 = [0] * b8
    b16 = [0] * 5
    b17 = [0] * 5
    b18 = [0] * 5
    b19 = [0] * 5
    b20 = [0] * 5
    b21 = [0] * 5
    b22 = [0] * 5
    for x in range(0,b8):
        b9[x] = x + 1
    b12 = b9
    for x in range(0,b8):
        b10[x] = b8 - x
    b13 = b10
    for x in range(0, b8):
        b11[x] = random.randint(a1, a2)
    b14 = b11
    b23 = [b9, b10, b11, \
    b12, b13, b14]
    b24 = [b16, b17, b18, \
    b19, b20, b21]
    for index in range(0, 3):
        for count in range(0,5):
            b15 = b23[index][:]
            a3 = time.clock()
            fonk1(b15)
            a4 = time.clock()
            b22[count] = a4 - a3
        b24[index] = b22[:]
    for index in range(3, 6):
        for count in range(0,5):
            b15 = b23[index][:]
            a3 = time.clock()
            fonk2(b15)
            a4 = time.clock()
            b22[count] = a4 - a3
        b24[index] = b22[:]
    for index in range(0,6):
        a5 = 0
        b22 = b24[index][:]
        for count in range(0,5):
            a5 = a5 + b22[count]
        b7[index] = a5 / 5
    print(str(b8) + '-Val Increasing Selection: ' + '{:.20f}'.format(b7[0]))
    print(str(b8) + '-Val Decreasing Selection: ' + '{:.20f}'.format(b7[1]))
    print(str(b8) + '-Val Random Selection:     ' + '{:.20f}'.format(b7[2]))
    print(str(b8) + '-Val Increasing Insertion: ' + '{:.20f}'.format(b7[3]))
    print(str(b8) + '-Val Decreasing Insertion: ' + '{:.20f}'.format(b7[4]))
    print(str(b8) + '-Val Random Insertion:     ' + '{:.20f}'.format(b7[5]))