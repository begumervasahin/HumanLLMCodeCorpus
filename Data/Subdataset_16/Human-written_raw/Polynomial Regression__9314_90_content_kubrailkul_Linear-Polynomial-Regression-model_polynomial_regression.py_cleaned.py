from numpy import *
from matplotlib.pyplot import *
import pandas as pd
from scipy import linalg
b1 = pd.read_csv("C:/Users/pc/Desktop/kurs/HW1_DATA.csv")
b2 = b1.b2
b3 = b1.b3
plot(b2,b3,'.')
show()
a1 = 0
b15 = 0
b4 = b3.dot(b2)
for i in range (0,1000):
    a1 = a1+b2[i]
    b15 = b15+b3[i]
def fonk1(num):
	return num/1000
b5 = fonk1(b2.dot(b2))-fonk1(a1)**2
b6 = fonk1(b4)-fonk1(a1)*fonk1(b15)
b6 = b6/b5
b7 = fonk1(b15)*fonk1(b2.dot(b2))-fonk1(b4)*fonk1(a1)
b7 = b7/b5
b8 = b6*b2+b7
plot(b2,b3,'.')
plot(b2,b8,'.')
show()
a3 = 0
a4 = 0
for i in range (0,999):
      a3 = a3+(b3[i]-b8[i])**2
      a4 = a4+(b3[i]-fonk1(b15))**2
b9 = 1-a3/a4
a4 = 0
for i in range (0,999):
    a4 = a4+(b3[i]-fonk1(b15))**2
def fonk2(p,b2):
    b8 = 0
    b10 = len(p)-1
    for i in range (0,len(p)):
        b8 = b8+p[i]*b2**(b10-i)
    return b8
def fonk3(b8,b3,a4):
    a3 = 0
    for i in range (0,999):
      a3 = a3+(b3[i]-b8[i])**2
    return 1-a3/a4
b11 = np.b11(1000)
b12 = np.c_[b2,b11]
b13 = np.linalg.solve(np.transpose(b12).dot(b12),np.transpose(b12).dot(b3) )
print(b13)
b12 = np.c_[b2**2,b12]
b13 = np.linalg.solve(np.transpose(b12).dot(b12),np.transpose(b12).dot(b3) )
print(b13)
b12 = np.c_[b2**3,b12]
b13 = np.linalg.solve(np.transpose(b12).dot(b12),np.transpose(b12).dot(b3) )
print(b13)
b12 = np.c_[b2**4,b12]
b13 = np.linalg.solve(np.transpose(b12).dot(b12),np.transpose(b12).dot(b3) )
print(b13)
b12 = np.c_[b2**5,b12]
b13 = np.linalg.solve(np.transpose(b12).dot(b12),np.transpose(b12).dot(b3) )
print(b13)
b12 = np.c_[b2**6,b12]
b13 = np.linalg.solve(np.transpose(b12).dot(b12),np.transpose(b12).dot(b3) )
print(b13)
b12 = np.c_[b2**7,b12]
b13 = np.linalg.solve(np.transpose(b12).dot(b12),np.transpose(b12).dot(b3) )
print(b13)
b14 = fonk2(b13,b2)
b15 = fonk3(b14,b3,a4)
plot(b2,b3,'.',b16 = 'b7')
plot(b2,b14,'.',b16 = 'g')