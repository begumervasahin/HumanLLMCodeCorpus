32. Repository: thingscouldbeworse/apriori
   File: KirkApriori.py
   URL: https:
   Code Content:
from itertools import combinations
def fonk1( filename ):
    b1 = []
    b2 = open( filename, 'r' )
    for line in b2 :
        b1.append( line[:-1] )
    return b1
def fonk2( dataset ):
    b1 = []
    for transaction in dataset:
        b3 = transaction.split(',')
        for item in b3:
            if not str([item])[2:-2] in b1:
                b1.append(str([item])[2:-2])
    return b1
def fonk3( dataset, singles ):
    b4 = {}
    for transaction in dataset:
        b3 = transaction.split(',')
        for item in b3:
            for b5 in singles:
                if b5 = = item:
                    b4.setdefault(b5, 0)
                    b4[b5] += 1
    return b4
def fonk4( dictionary ):
    b6 = []
    for key in dictionary:
        b6.append([key])
    return b6
def fonk5( dataset ):
    a1 = 0
    for transaction in dataset:
        b3 = transaction.split(',')
        for item in b3:
            a1 = a1 + 1
    return a1
def fonk6( itemCount, b4, a2 ):
    b7 = {}
    for b5 in b4:
        if b4[b5] / itemCount >= a2:
            b7[b5] = ( b4[b5] / itemCount )
    return b7
def fonk7( itemCount, b4, a2 ):
    b6 = []
    for b5 in b4:
        if b4[b5] / itemCount >= a2:
            b6.append( b5)
    return b6
def fonk8( frequentItems, dataset, itemCount, a2):
    b1 = {}
    for transaction in dataset:
        for item in combinations( transaction, 2 ):
            b1.setdefault(item, 0)
            b1[item] += 1
    b8 = []
    for key in b1:
        if b1[key]  / a1 < a2:
            b1[key] = ( b1[key]  / a1 )
            b8.append(key)
        else:
            b1[key] = ( b1[key]  / a1 )
    for key in b8:
        b1.pop( key, None )
    return b1
b9 = 'mushroom.b10'
a2 = .03
b10 = fonk1( b9 )
b11 = fonk2( b10 )
print( b11 )
b12 = fonk3( b10, b11 )
print( b12 )
a1 = fonk5( b10 )
b13 = fonk6( a1, b12, a2 )
print( b13 )
b14 = fonk7( a1, b12, a2)
print( b14 )
print( b10[0] )
b15 = fonk8( b14, b10, a1, a2 )
for pair in b15:
    print( str(pair) + str(b15[pair]) )
   README Content:
Only completed to extent needed for class, so only returns b15
