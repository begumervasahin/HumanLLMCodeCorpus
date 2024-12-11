import csv
import math
import operator
def fonk1(set1, set2, b2):
	a1 = 0
	for x in range(b2):
		a1 += pow((set1[x] - set2[x]), 2)
	return math.sqrt(a1)
def fonk2(givendata, sample, b12):
	b1 = []
	b2 = len(sample)
	for x in range(len(givendata)):
		b3 = fonk1(sample, givendata[x], b2)
		b1.append((givendata[x], b3))
	print '\n'.join(map(str,b1))
	b1.sort(b4 = operator.itemgetter(1))
	b5 = []
	for x in range(b12):
		b5.append(b1[x][0])
	return b5
def fonk3(neighbors):
	b6 = {}
	for x in range(len(neighbors)):
		b7 = neighbors[x][-1]
		print b7
		if b7 in b6:
			b6[b7] += 1
		else:
			b6[b7] = 1
	b8 = sorted(b6.iteritems(), b4=operator.itemgetter(1), reverse=True)
	print b8
	return b8[0][0]
def fonk4():
    with open('data.csv','rb') as csvfile:
        b9 = csv.reader(csvfile)
        b10 = list(b9)
        for x in range(len(b10)):
            for b11 in range(3):
                if b11 = = 3:
                    if b10[x][b11] == 'M':
                        b10[x][b11] = 1
                    else:
                        b10 [x][b11] = 2
                b10[x][b11]=float(b10[x][b11])
            b10.append(b10[x])
    b12 = input('enter number of predictions to use')
    b13 = input('enter data to be predicted')
    b14 = fonk2(b10,b13,b12)
    b15 = fonk3(b14)
    print 'nearest neibhbors are'
    print b14
    print'Prediction for gender with given data is'
    if b15 = = 1:
        print 'M'
    else:
        print 'w'
fonk4()