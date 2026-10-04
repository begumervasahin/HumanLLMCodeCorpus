import os
import sys
import math
b1 = []
b2 = []
b3 = []
b4 = []
b5 = True
while(b5 = = True):
    b6 = input("Enter a list of numbers:")
    b2 = b6.split(",")
    b1.extend(b2)
    for b7 in b1:
        if(b7.isdigit()==False):
            print(b7, "is not an integer value")
            b4.append(b7)
            if (b7 = = "Terminate"):
                b1.remove(b7)
                print("You terminated the program")
                b5 = False
            else:
                 b1.remove(b7)
while b1:
    b8 = b1[0]
    for x in b1:
        if x < b8:
            b8 = x
    b3.append(b8)
    b1.remove(b8)
print (b3)
for b13 in range(0,len(b3)):
    b3[b13] = int(b3[b13])
b9 = b3[-1]
b10 = b3[0]
b11 = b9 - b10
b12 = len(b3)
a1 = 0
for b13 in range (0,len(b3)):
    a1 = a1 + b3[b13]
    b13 = b13+1
b14 = a1/b12
a2 = 1
b13 = 0
print("1) The number of each individual number:")
for b13 in range (0,len(b3)):
    a2 = 0
    for j in range(1,len(b3)):
        if(b3[b13]== b3[j]):
            a2 = a2+1
    print(b3[b13], ":", a2)
for b13 in range(0,len(b3)):
    b15 = (b3[b13]- b14)**2
    b16 = b15/b12
b17 = math.sqrt(b16)
print("2) The Maximum value is:", b9)
print("3) The Minimum value is:", b10)
print("4) The Range of the two numbers is:", b11)
print("5) Arithmetic Mean of the two numbers is:", b14)
print("6) Variance of the two numbers si:", b16)
print("7) The Standard Deviation of two numbers is:",b17)
print("8)", b4)