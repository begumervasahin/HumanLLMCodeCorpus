import numpy as np
b1 = 'savefiles/640test_'
b2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
b3 = open('640_final.dat', 'w')
a1 = 0.0
a2 = 0
for b5 in b2:
    b4 = open(b1+str(b5)+'.dat', 'r')
    a3 = 0
    a4 = 0.0
    a5 = 0
    a6 = 0.0
    for line in b4:
        if b5 = = 1:
            b6 = line.split('[')
            b7 = b6[0]
            b8 = float(b7.split(' ')[0])
            b9 = int(b7.split(' ')[1])
            a4 = a1+b8
            a5 = a2+b9
            b10 = str(a4)+' '+str(a5)+' ['+b6[1]
            b3.write(b10)
        else:
            if a3 = = 0:
                b6 = line.split('[')
                b7 = b6[0]
                a6 = float(b7.split(' ')[0])
            if a3 >= 1:
                b6 = line.split('[')
                b7 = b6[0]
                b8 = float(b7.split(' ')[0])
                b9 = int(b7.split(' ')[1])
                a4 = a1+(b8-a6)
                a5 = a2+b9
                b10 = str(a4)+' '+str(a5)+' ['+b6[1]
                b3.write(b10)
        a3 = a3+1
    b4.close()
    print("Finished with file "+str(b5))
    a1 = a4
    a2 = a5