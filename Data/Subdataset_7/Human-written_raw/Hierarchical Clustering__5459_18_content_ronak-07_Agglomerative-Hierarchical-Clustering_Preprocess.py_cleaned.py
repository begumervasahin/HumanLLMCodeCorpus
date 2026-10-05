import distance
import time
import numpy as np
def fonk1():
	global b10
	for i in range(0,a1+1):
		for j in range(0,i):
			if i!=j:
				b10[i][j]=distance.levenshtein(b7[i],b7[j])
				b10[j][i]=b10[i][j]
				b8.insert(i,b10[i][j])
				print(i)
	b8.sort()
	return b10
def fonk2():
    global a1
    b1 = len(b6)
    for i in range(len(b6)):
        b2 = b6[i]
        if b2[0]=='>':
            b3 = ""
            i+=1
            b2 = b6[i]
            while(b2[0]!='>'):
                b3+=b2
                i+=1
                if i < b1:
                    b2 = b6[i]
                else:
                    break
            a1+=1
            b7[a1]=b3
b4 = open("data_amino2.txt","b3").read()
b5 = open("edited.txt","w")
b6 = b4.splitlines()
b7 = dict()
b8 = list()
a1 = -1
b9 = time.time()
fonk2()
print("Preprocessing done\b1" +str(time.time()-b9))
b10 = np.zeros(shape=(a1+1,a1+1))
b9 = time.time()
b11 = fonk1()
print("Distance Matrix Calculation done\b1" + str(time.time()-b9))
np.save('distance_matrix.npy',b11)