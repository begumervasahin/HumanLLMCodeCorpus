import csv
import random
import math
def fonk1(data):
        b1 = {}
        b2 = len(data)
        for i in range(len(data)):
                b3 = data[i]
                if (b3[-1] not in b1):
                        b1[b3[-1]] = []
                b1[b3[-1]].append(b3)
        return b1
def fonk2(numbers):
        return sum(numbers)/float(len(numbers))
def fonk3(numbers):
        b4 = fonk2(numbers)
        b5 = sum([pow(b11-b4,2) for b11 in numbers])/float(len(numbers)-1)
        return math.sqrt(b5)
def fonk4(data):
        b6 = [(fonk2(feature), fonk3(feature)) for feature in zip(*data)]
        del b6[-1]
        return b6
def fonk5(data):
        b7 = fonk1(data)
        b6 = {}
        for clsslabel, instances in b7.iteritems():
                b6[clsslabel] = fonk4(instances)
        return b6
def fonk6(b11, mean, b10):
        b8 = math.exp(-(math.pow(b11-mean,2)/(2*math.pow(b10,2))))
        return (1 / (math.sqrt(2*math.pi) * b10)) * b8
def fonk7(b21, sample):
        b9 = {}
        for clsslabel,b6  in b21.iteritems():
                b9[clsslabel] = 1
                for i in range(len(b6)):
                        mean, b10 = b6[i]
                        b11 = sample[i]
                        b12 = fonk6(b11,mean,b10)
                        print 'prob densities'
                        print b12
                        b9[clsslabel] *=b12
        print 'ClssProbabilities(b11/c)'
        print b9
        return b9
def fonk8(b21, sample):
        b13 = fonk7(b21, sample)
        b15, b14 = None, -1
        for clsslabel, probability in b13.iteritems():
                if b15 is None or probability > b14:
                        b14 = probability
                        b15 = clsslabel
        return b15
def fonk9(b21, b22):
    b16 = fonk8(b21, b22)
    return b16
def fonk10():
    b17 = []
    with open('data.csv','rb') as csvfile:
        b18 = csv.reader(csvfile)
        b19 = list(b18)
        for b11 in range(len(b19)):
            for b20 in range(4):
                if b20 = = 3:
                    if b19[b11][b20] == 'M':
                        b19[b11][b20] = 1
                    else:
                        b19 [b11][b20] = 2
                b19[b11][b20]=float(b19[b11][b20])
            b17.append(b19[b11])
    b21 = fonk5(b17)
    print('Summary by class class1: {0}').format(b21)
    b22 = input('enter data for b23')
    b23 = fonk9(b21,b22)
    if b23 = = 1:
            print 'M'
    else:
            print 'W'
fonk10()