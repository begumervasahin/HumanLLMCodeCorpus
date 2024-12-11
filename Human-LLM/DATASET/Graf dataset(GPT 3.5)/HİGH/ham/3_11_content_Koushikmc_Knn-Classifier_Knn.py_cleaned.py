import _csv as csv
import math
import operator
b1 = []
def fonk1(b11):
    try:
        b2 = open(b11)
        b3 = csv.reader(b2)
        for rec in b3:
            b4 = []
            for cols in rec:
                if rec.index(cols) != len(rec)-1:
                    b4.append(float(cols))
                else:
                    b4.append(cols)
            b1.append(b4)
        print ("training b3 loaded")
    except IOError:
        print ("File not available. Please check the filename")
        exit()
def fonk2(b2,b12):
    b5 = []
    for rec in b2:
        if len(rec[0:len(rec)-1]) != len(b12):
            print("Dimensions of b12 and b2 do not match")
            break
        else:
            a1 = 0
            for i in range(0,len(b12)):
                a1 += (b12[i]-rec[i])**2
        print ("Distance between the b12 point and training b3 " +str(b2.index(rec)+1)+ " " +str(round(math.sqrt(a1),3)))
        b5.append(round(math.sqrt(a1),3))
    return b5
def fonk3(a1,numofneighbors):
    b6 = sorted(range(len(a1)),key=lambda x:a1[x])
    b7 = b6[:numofneighbors]
    b8 = {}
    for n in b7:
        if b1[n][-1] in b8:
            b8[b1[n][-1]] +=1
        else:
            b8.update({b1[n][-1]:1})
    b9 = sorted(b8.items(), key=operator.itemgetter(1),reverse = True)[0][0]
    print (b9)
if b10 = = "__main__":
    print ("Place the input dataset csv file in the same directory of the python module ")
    b11 = input("Enter the name of the training dataset csv file :")
    fonk1(b11)
    b12 = [float(x) for x in (raw_input("Enter the values separated by ',': " ).split(","))]
    b13 = int(raw_input("Enter the number of b7 to consider :"))
    b14 = fonk2(b1,b12)
    fonk3(b14,b13)