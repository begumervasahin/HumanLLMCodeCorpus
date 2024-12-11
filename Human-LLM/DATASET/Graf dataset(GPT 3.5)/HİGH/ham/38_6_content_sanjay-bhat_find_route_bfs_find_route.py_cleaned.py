6. Repository: sanjay-bhat/b21
   File: class1.py
   URL: https:
   Code Content:
import romania
import sys
class class1:
    def fonk1(self):
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        b3 = sys.argv[3]
        a1 = 0
        b4 = []
        b5 = romania.romania(0).getDataRomania(b1)
        b6 = b5[0]
        b7 = b5[1]
        b8 = [False] * b7
        for i in range(b7):
            if b8[i] == False:
                self.fonk2(b6, b2, b8, b4)
        b9 = [float("Inf")] * b7
        b9[b6.keys().index(b2)] = 0.0
        b10 = [0] * b7
        b11 = [0] * b7
        b12 = [0] * b7
        while b4:
            b13 = b4.pop()
            for b15, distance in b6[b13]:
                b14 = float(b9[b6.keys().index(b13)]) + float(distance)
                if float(b9[b6.keys().index(b15)]) > b14:
                    b9[b6.keys().index(b15)] = b14
                    b10[b6.keys().index(b15)] = b13
                    b11[b6.keys().index(b15)] = b15
                    b12[b6.keys().index(b15)] = float(distance)
                    if b15 = = b3:
                        a1 = b14
        b13 = 0
        b16 = []
        b17 = a1
        while a1 != 0:
            if b11[b13] == b3:
                    b16.append(b10[b13])
                    b16.append(b11[b13])
                    b16.append(str(b12[b13]))
                    a1 = b9[b13] - b12[b13]
                    b3 = b10[b13]
                    b13 = 0
            else:
                b13 = b13 + 1
        b16.reverse()
        if b17 = = 0:
            b18 = "distance: infinity\nroute:\nnone\n"
        else:
            b18 = "distance: " + str(b17) + " km\n" + "route:\n"
            b13 = 0
            while b13 < len(b16):
                b18 += b16[b13 + 2] + " to " + b16[b13 + 1] + ", " + b16[b13] + " km\n"
                b13 = b13 + 3
        print b18
    def fonk2(self, b6, b2, b8, b4):
        b8[b6.keys().index(b2)] = True
        if b2 in b6.keys():
            for d, distance in b6[b2]:
                if b8[b6.keys().index(d)] == False:
                    self.fonk2(b6, d, b8, b4)
        b4.append(b2)
def fonk3():
    b19 = class1()
    b19.fonk1()
if b20 = = "__main__":
    fonk3()
   README Content:
b21 = =====
[![Build Status](https:
find-route calculates optimal distance between two b7 by also taking into accont thier weights. In this case the b7 are cities and weights are distances between them and we use BSF in an attempt to find shortest route between any 2 given cities provided a path exists.
Files included
--------------
1. romania.py - Contains the details on converting the text containing b7 and their respective distances into b6.
2. class1.py - Find the optimal path between b15 1 and b15 2, i.e: source and b15, using BSF
3. input1.txt - File containing b7 and their respective distances
Steps to run the code
---------------------
1. Place the files [1], [2] and [3] in desired directory and change permissions of all the 3 files from existing (0644) permissions to -rwxrwxrwx, i.e: 0777.
2. Open terminal.
3. Traverse to the directory where the files are held using 'cd'.
4. Invoke the code using the following command, '[san @ubuntu]$ python class1.py input1.txt Berlin Munich' and hit enter to find the BFS shortest path between Berlin and Munich.
5. Change input1.txt file and cities following it as per need.
