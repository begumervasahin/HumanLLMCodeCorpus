import networkx as nx
import csv
import math
def fonk1(b15,b16):
	b1 = b15[0]
	b2 = b15[1]
	b3 = b16[0]
	b4 = b16[1]
	b5 = float(math.pow(math.pow((b3-b1),2)+math.pow((b4-b2),2),0.5))
	return b5
b6 = open("bnk_node.csv",'w')
b7 = csv.writer(b6)
b8 = []
b9 = {}
b10 = open("q_result.csv",'r')
b11 = csv.reader(b10)
b12 = open("bnk_edge.csv",'w')
b13 = csv.writer(b12)
a1 = 1
for l in b11:
	print(l)
	b14 = str(l[0]).split()
	b15 = (float(b14[1]),float(b14[2]))
	b16 = (float(b14[4]),float(b14[5]))
	if(b15 not in b8):
		b8.append(b15)
		b7.writerow([a1,b15[0],b15[1]])
		b9[b15]=a1
		a1+=1
	if(b16 not in b8):
		b8.append(b16)
		b7.writerow([a1,b16[0],b16[1]])
		b9[b16]=a1
		a1+=1
	b13.writerow([b9[b15] , b9[b16] , int(b14[8]),fonk1(b15,b16)])
	b13.writerow([b9[b16] , b9[b15] , int(b14[8]),fonk1(b15,b16)])
b6.close()
b12.close()
b10.close()