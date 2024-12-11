
import random
import time
def fonk1(b16, b6):
    random.seed(0)
    b1 = open(b16, 'w')
    a1 = 0
    while a1 < b6:
        b1.write(str(random.randrange(0,100)) + "\b6")
        a1 += 1
    b1.close()
def fonk2( b4, b5 ):
    b2 = []
    a2 = 0
    a3 = 0
    while a2 < len( b4 ) and a3 < len( b5 ):
        if b4[ a2 ] < b5[ a3 ]:
            b2.append( b4[ a2 ]  )
            a2 += 1
        else:
            b2.append( b5[ a3 ] )
            a3 += 1
    while a2 < len(b4):
        b2.append( b4[ a2 ] )
        a2 += 1
    while a3 < len( b5 ):
        b2.append( b5[ a3 ] )
        a3 += 1
    return b2
def fonk3( b2 ):
    if len( b2 ) <= 1:
        return b2
    else:
        b3 = len( b2 )
        b4 = fonk3( b2[ :b3 ] )
        b5 = fonk3( b2[b3:] )
        return fonk2( b4, b5 )
def fonk4( b2 ):
  b6 = len( b2 )
  for i in range( b6 - 1 ):
    b7 = i
    for j in range( i + 1, b6 ):
      if b2[ j ] < b2[ b7 ] :
        b7 = j
    b8 = b2[ i ]
    b2[ i ] = b2[ b7 ]
    b2[ b7 ] = b8
  return b2
def fonk5(b17, b18):
    b9 = time.time()
    b1 = open(b17, 'r')
    b10 = b1.readlines()
    b1.close()
    b11 = time.time()
    b12 = b11 - b9
    print("It took", round(b12, 6), "seconds to input values from file", b17)
    b9 = time.time()
    for i in range(len(b10)):
        b10[i] = int(b10[i])
    b13 = fonk3(b10)
    b11 = time.time()
    b14 = b11 - b9
    print("It took", round(b14, 6), "seconds to sort", b6, "values using merge sort")
    b9 = time.time()
    b1 = open(b18, 'w')
    for i in range(len(b13)):
        b13[i] = str(b13[i])
        b1.write(b13[i] + "\b6")
    b1.close()
    b11 = time.time()
    b15 = b11 - b9
    print("It took", round(b15, 6), "seconds to output", b6, "sorted values to file", b18)
    print("Total time the program took is", round((b12 + b14 + b15), 6), "seconds")
    print()
def fonk6(b17, b18):
    b9 = time.time()
    b1 = open(b17, 'r')
    b10 = b1.readlines()
    b1.close()
    b11 = time.time()
    b12 = b11 - b9
    print("It took", round(b12, 6), "seconds to input values from file", b17)
    b9 = time.time()
    for i in range(len(b10)):
        b10[i] = int(b10[i])
    b13 = fonk4(b10)
    b11 = time.time()
    b14 = b11 - b9
    print("It took", round(b14, 6), "seconds to sort", b6, "values using selection sort")
    b9 = time.time()
    b1 = open(b18, 'w')
    for i in range(len(b13)):
        b13[i] = str(b13[i])
        b1.write(b13[i] + "\b6")
    b1.close()
    b11 = time.time()
    b15 = b11 - b9
    print("It took", round(b15, 6), "seconds to output", b6, "sorted values to file", b18)
    print("Total time the program took is", round((b12 + b14 + b15), 6), "seconds")
b16 = input('Enter the b16: ')
b6 = int(input('Enter number of values: '))
fonk1(b16, b6)
b17 = b16
b18 = input('Please enter output file name: ')
fonk5(b17, b18)
fonk6(b17, b18)