b1 = 's'
import numpy as np
b2 = open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv');
a1 = 0
b3 = []
b4 = []
a2 = 0
a3 = 0
b5 = []
b6 = []
for line in iter(b2):
    if(a1 = =0):
        a1 = a1+1
    else :
        b7 = line.split(",")
        if a2 = = int(b7[0]) :
            b5 = []
            b5.append(b7[1])
            b5.append(str(b7[2]))
            b5.append(b7[3])
            b4.append(b5)
        else :
            a2 = int(b7[0])
            if len(b4)>0 :
                b3.append(b4)
            b4 = []
            b5 = []
            b6.append(b7[0])
            b5.append(b7[1])
            b5.append(str(b7[2]))
            b5.append(b7[3])
            b4.append(b5)
b3.append(b4)
print "loading done"
b8 = open('distance_matrix_final.csv')
b9 = np.zeros((8357,8357))
a4 = 0
for line in iter(b8):
   b10 = []
   b10 = line.split(",")
   if b6[a4]!=b10[0] :
       print 'error',a4
   a5 = 0
   a1 = 1
   while a1<len(b10):
       if float(b10[a1]) == float(0) :
           if a4!=a1-1:
               print "error at ",a4,a1-1
       b9[a4][a5] = b10[a1]
       a5+=1
       a1+=1
   a4+=1
a4 = 0
a5 = 0
while a4<8357:
    a5 = 0
    while a5<8357:
            if b9[a4][a5] != b9[a5][a4] :
                print "error at" , a4,a5
            a5+=1
    a4+=1