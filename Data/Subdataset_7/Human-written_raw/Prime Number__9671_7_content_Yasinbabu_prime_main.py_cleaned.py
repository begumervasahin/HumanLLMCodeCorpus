import numpy as np
import csv
a1 = 100
b1 = np.array([])
def fonk1(x,primeList):
    for b2 in primeList:
        if b2<=np.sqrt(x):
            if x%b2 = = 0:
                return False
        else:
            break
for i in range(2,a1+1):
    if fonk1(i,b1) != False:
        b1 = np.append(b1, i)
with open('prime_'+str(a1)+'_('+str(len(b1))+').csv', 'w', b3 = '') as csvfile:
    b4 = csv.writer(csvfile, delimiter=',')
    b4.writerow(b1)
print(str(a1))
print(str(len(b1)))