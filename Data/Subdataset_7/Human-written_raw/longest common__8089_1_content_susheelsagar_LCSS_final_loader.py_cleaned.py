import numpy as np
b1 = open("distance_matrix_full.csv","r+")
a1 = 0
a2 = 0
b2 = []
b3 = np.zeros((8357,8357))
for line in iter(b1) :
    b4 = []
    a1 = 0
    a3 = 1
    b4 = line.split(",")
    b2.append(b4[0])
    while(a3<len(b4)):
        b3[a2][a1] = b4[a3]
        b3[a1][a2] = b3 [a2][a1]
        a1 +=1
        a3 +=1
    a2 +=1
a4 = 0
b5 = open("distance_matrix_1698.csv","r+")
for line in iter(b5) :
    print a2
    b4 = []
    a3 = 1
    a1 = a2
    b4 = line.split(",")
    b2.append(b4[0])
    while(a3<len(b4)):
        if a2 = = 8356 :
            print a3,a1
        b3[a2][a1] = b4[a3]
        b3[a1][a2] = b3 [a2][a1]
        a1+=1
        a3+=1
    a2+=1
a2 = 0
b6 = open("distance_matrix_final.csv","r+")
b7 = open("distance_matrix_final_withoutid.csv","r+")
while a2<8357:
    a1 = 0
    b6.write(str(b2[a2]))
    b6.write(",")
    b6.write(str(b3[a2][a1]))
    b7.write(str(b3[a2][a1]))
    a1 = 1
    while a1<8357:
        b6.write(",")
        b6.write(str(b3[a2][a1]))
        b7.write(",")
        b7.write(str(b3[a2][a1]))
        a1+=1
    b6.write("\n")
    b7.write("\n")
    a2+=1