import random
import time
import sys
def fonk1(insArr):
    for x in range(0,len(insArr),1):
        b1 = insArr[x]
        b2 = x
        while (b2>0 and b1<insArr[b2-1]):
            insArr[b2]=insArr[b2-1]
            b2-=1
        insArr[b2]=b1
    return insArr
def fonk2(insArr):
    for x in range(0,len(insArr),1):
        b1 = insArr[x]
        b2 = x
        while (b2>0 and b1>insArr[b2-1]):
            insArr[b2]=insArr[b2-1]
            b2-=1
        insArr[b2]=b1
    return insArr
def fonk3(qPArr,b6,b5):
    b3 = b5 - b6 + 1
    b4 = [0]*(b3)
    a1 = -1
    a1 = a1 + 1
    b4[a1] = b6
    a1 = a1 + 1
    b4[a1] = b5
    while a1 >= 0:
        b5 = b4[a1]
        a1 = a1 - 1
        b6 = b4[a1]
        a1 = a1 - 1
        b7 = ( b6-1 )
        b8 = qPArr[b5]
        for j in range(b6,b5,1):
            if   qPArr[j] <= b8:
                b7 = b7+1
                qPArr[b7],qPArr[j] = qPArr[j],qPArr[b7]
        qPArr[b7+1],qPArr[b5] = qPArr[b5],qPArr[b7+1]
        b8 = b7+1
        if abs(b6-b8)<abs(b8-b5):
            if b8+1 < b5:
                a1 = a1 + 1
                b4[a1] = b8 + 1
                a1 = a1 + 1
                b4[a1] = b5
            if b8-1 > b6:
                a1 = a1 + 1
                b4[a1] = b6
                a1 = a1 + 1
                b4[a1] = b8 - 1
        else:
            if b8-1 > b6:
                a1 = a1 + 1
                b4[a1] = b6
                a1 = a1 + 1
                b4[a1] = b8 - 1
            if b8+1 < b5:
                a1 = a1 + 1
                b4[a1] = b8 + 1
                a1 = a1 + 1
                b4[a1] = b5
def fonk4(qPArr,b6,b5):
    b3 = b5 - b6 + 1
    b4 = [0]*(b3)
    a1 = -1
    a1 = a1 + 1
    b4[a1] = b6
    a1 = a1 + 1
    b4[a1] = b5
    while a1 >= 0:
        b5 = b4[a1]
        a1 = a1 - 1
        b6 = b4[a1]
        a1 = a1 - 1
        b7 = ( b6-1 )
        b9 = random.randrange(b6,b5+1,1)
        qPArr[b5],qPArr[b9]=qPArr[b9],qPArr[b5]
        b8 = qPArr[b5]
        for j in range(b6,b5,1):
            if   qPArr[j] <= b8:
                b7 = b7+1
                qPArr[b7],qPArr[j] = qPArr[j],qPArr[b7]
        qPArr[b7+1],qPArr[b5] = qPArr[b5],qPArr[b7+1]
        b8 = b7+1
        if abs(b6-b8)<abs(b8-b5):
            if b8+1 < b5:
                a1 = a1 + 1
                b4[a1] = b8 + 1
                a1 = a1 + 1
                b4[a1] = b5
            if b8-1 > b6:
                a1 = a1 + 1
                b4[a1] = b6
                a1 = a1 + 1
                b4[a1] = b8 - 1
        else:
            if b8-1 > b6:
                a1 = a1 + 1
                b4[a1] = b6
                a1 = a1 + 1
                b4[a1] = b8 - 1
            if b8+1 < b5:
                a1 = a1 + 1
                b4[a1] = b8 + 1
                a1 = a1 + 1
                b4[a1] = b5
print ("Hi, Question 1 - Assignment 2 Algorithm has started, Plotting of graph to compare sorting algorithms will be done. - Gurleen Singh Dhody")
while True:
    print ("There are 4 modules listed as [A,B,C,D] for Question 1 and only 1 module can be run at one time. Press E for exit.")
    if sys.version_info[0] <3:
        b10 = raw_input("Please enter which part of Question 1 you want to run (Example : A): ")
        print("")
        b11 = int(raw_input("Enter b3 of array N : ").strip())
    else:
        b10 = input("Please enter which part of Question 1 you want to run (Example : A): ")
        print("")
        b11 = int(input("Enter b3 of array N : ").strip())
    b10 = b10.lower();
    if b10 = ="a":
        b12 = []
        b12.append(b11)
        plotAlgo1,b13 = [],[]
        a2 = 0
        for x in b12:
            b14 = x
            b15 = random.sample(range(b14),b14)
            testSample1,b16 = b15[:],b15[:]
            plotAlgo1.append(time.time())
            fonk1(testSample1)
            plotAlgo1[a2]=(abs(plotAlgo1[a2]-time.time()))
            b13.append(time.time())
            fonk3(b16,0,b14-1)
            b13[a2]=(abs(b13[a2]-time.time()))
            a2+=1
        print("\nTest Sample Size : \n")
        print(b12)
        print ("Insertion")
        print (plotAlgo1)
        print ("QuickSort Normal")
        print (b13)
    elif b10 = ="b":
        b12 = []
        b12.append(b11)
        b13,b17 = [],[]
        a2 = 0
        for x in b12:
            b14 = x
            b15 = random.sample(range(b14),b14)
            testSample1,b16 = b15[:],b15[:]
            b13.append(time.time())
            fonk3(testSample1,0,b14-1)
            b13[a2]=(abs(b13[a2]-time.time()))
            b17.append(time.time())
            fonk4(b16,0,b14-1)
            b17[a2]=(abs(b17[a2]-time.time()))
            a2+=1
        print("\nTest Sample Size : \n")
        print(b12)
        print ("Quicksort Normal")
        print (b13)
        print ("Quicksort Random")
        print (b17)
    elif b10 = ="c":
        b12 = []
        b12.append(b11)
        plotAlgo1,b13 = [],[]
        a2 = 0
        for x in b12:
            b14 = x
            b15 = list(range(b14))
            testSample1,b16 = b15[:],b15[:]
            plotAlgo1.append(time.time())
            fonk1(testSample1)
            plotAlgo1[a2]=(abs(plotAlgo1[a2]-time.time()))
            b13.append(time.time())
            fonk3(b16,0,b14-1)
            b13[a2]=(abs(b13[a2]-time.time()))
            a2+=1
        print("\nTest Sample Size : \n")
        print(b12)
        print ("Insertion")
        print (plotAlgo1)
        print ("QuickSort Normal")
        print (b13)
    elif b10 = ="d":
        b12 = []
        b12.append(b11)
        plotAlgo1,b13 = [],[]
        a2 = 0
        for x in b12:
            b14 = x
            b15 = list(range(b14))
            b15 = fonk2(b15)
            testSample1,b16 = b15[:],b15[:]
            plotAlgo1.append(time.time())
            fonk1(testSample1)
            plotAlgo1[a2]=(abs(plotAlgo1[a2]-time.time()))
            b13.append(time.time())
            fonk3(b16,0,b14-1)
            b13[a2]=(abs(b13[a2]-time.time()))
            a2+=1
        print("\nTest Sample Size : \n")
        print(b12)
        print ("Insertion")
        print (plotAlgo1)
        print ("QuickSort Normal")
        print (b13)
    elif b10 = ="e":
        break
    else:
        print ("Wrong Input. Please try again. Or press E to exit.")
    print("");
    print("");
    print("");
    b10 = ""