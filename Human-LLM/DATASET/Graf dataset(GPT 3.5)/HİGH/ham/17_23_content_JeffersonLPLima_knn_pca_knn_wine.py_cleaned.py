import csv
import random
import math
import operator
def fonk1(instance1, instance2, b2):
        a1 = 0
        for x in range(b2):
                a1 += pow((float(instance1[x]) - float(instance2[x])), 2)
        return math.sqrt(a1)
def fonk2(b9, testInstance, a4):
        b1 = []
        b2 = len(testInstance)-1
        for x in range(len(b9)):
                b3 = fonk1(testInstance, b9[x], b2)
                b1.append((b9[x], b3))
        b1.sort(b4 = operator.itemgetter(1))
        b5 = []
        for x in range(a4):
                b5.append(b1[x][0])
        return b5
def fonk3(b5):
        b6 = {}
        for x in range(len(b5)):
                b7 = b5[x][-1]
                if b7 in b6:
                        b6[b7] += 1
                else:
                        b6[b7] = 1
        b8 = sorted(b6.iteritems(), b4=operator.itemgetter(1), reverse=True)
        return b8[0][0]
def fonk4(b10, b16):
        a2 = 0
        for x in range(len(b10)):
                if b10[x][-1] == b16[x]:
                        a2 += 1
        return (a2/float(len(b10))) * 100.0
def fonk5():
        b9 = []
        b10 = []
        b11 = []
        b12 = []
        b13 = []
        with open('1.data', 'rb') as csvfile:
            b14 = csv.reader(csvfile, delimiter='	')
            b15 = list(b14)
            for x in range(len(b15)):
                b11.append(b15[x])
        with open('2.data', 'rb') as csvfile:
            b14 = csv.reader(csvfile, delimiter='	')
            b15 = list(b14)
            for x in range(len(b15)):
                b12.append(b15[x])
        with open('3.data', 'rb') as csvfile:
            b14 = csv.reader(csvfile, delimiter='	')
            b15 = list(b14)
            for x in range(len(b15)):
                b13.append(b15[x])
        print 'Training set: ' + repr(len(b9))
        print 'set: ' + repr(len(b11))
        print 'set: ' + repr(len(b12))
        print 'set: ' + repr(len(b13))
        for x in range(len(b11)):
                for y in range(13):
                    b11[x][y] = float(b11[x][y])
        for x in range(len(b12)):
                for y in range(13):
                    b12[x][y] = float(b12[x][y])
        for x in range(len(b13)):
                for y in range(13):
                    b13[x][y] = float(b13[x][y])
        a3 = 0
        for i in range (10):
                b9 = []
                b10 = []
                for x in range(len(b11)):
                      if((x>=(0.1*len(b11))*i)) & (x<(0.1*(len(b11))*(i+1))):
                            b10.append(b11[x])
                      else:
                            b9.append(b11[x])
                for x in range(len(b12)):
                      if((x>=(0.1*len(b12))*i)) & (x<(0.1*(len(b12))*(i+1))):
                            b10.append(b12[x])
                      else:
                            b9.append(b12[x])
                for x in range(len(b13)):
                      if((x>=(0.1*len(b13))*i)) & (x<(0.1*(len(b13))*(i+1))):
                            b10.append(b13[x])
                      else:
                            b9.append(b13[x])
                print "Treino " + str(len(b9))
                print "Teste "+ str(len(b10))
                b16 = []
                a4 = 1
                for x in range(len(b10)):
                       b5 = fonk2(b9, b10[x], a4)
                       b17 = fonk3(b5)
                       b16.append(b17)
                b18 = fonk4(b10, b16)
                print("fold "+str(i)+'    Accuracy:' + repr(b18) + '%')
                a3+=b18
        print a3/10
fonk5()