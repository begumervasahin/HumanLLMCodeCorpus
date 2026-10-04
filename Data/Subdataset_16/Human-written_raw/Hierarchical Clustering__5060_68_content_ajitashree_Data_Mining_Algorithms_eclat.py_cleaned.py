import sys
import pandas as pd
def fonk1(l1, l2):
	b1 = []
	for l in l1:
		if l in l2:
			b1 += [l]
	return list(set(b1))
def fonk2(l, m):
	for i in l:
		if i not in m:
			return False
	return True
def fonk3(b11, b13, b9, b15):
	if (len(b11) == 1):
		b15 += [b11[0]]
	for i in range(len(b11)):
		b9 += [b11[i]]
		b2 = []
		for j in range(i + 1, len(b11)):
			b3 = list(set(b11[i][0] + b11[j][0]));
			b4 = fonk1(b11[i][1], b11[j][1])
			if len(b4) >= b13:
				b2 += [(b3, b4, len(b3))]
		if(b2):
			fonk3(b2, b13, b9, b15)
		else:
			if (len(b11) != 1):
				b15 += [b11[i]]
def fonk4(l1, l2):
	b1 = []
	for l in l1:
		if l not in l2:
			b1 += [l]
	return b1
def fonk5(b12, b13, b10, b16):
	if (len(b12) == 1):
		b16 += [b12[0]]
	for i in range(len(b12)):
		b10 += [b12[i]]
		b5 = []
		for j in range(i + 1, len(b12)):
			b3 = list(set(b12[i][0] + b12[j][0]));
			b6 = fonk4(b12[j][2], b12[i][2])
			b7 = b12[i][1] - len(b6)
			if b7 >= b13:
				b5 += [(b3, b7, b6, len(b3))]
		if (b5):
			fonk5(b5, b13, b10, b16)
		else:
			if (len(b12) != 1):
				b16 += [b12[i]]
if b8 = = '__main__':
	b9 = []
	b10 = []
	b11 = []
	b12 = []
	print ""
	b13 = input('Enter b13: ')
	b14 = ["TID"]
	b15 = []
	b16 = []
	b17 = []
	b18 = pd.read_csv('./db.csv', header = None)
	for i in range(1, len(b18.b19)):
		b14 += [("i" + str(i))]
	b18.b19 = b14
	b20 = b18["TID"].count()
	del b18["TID"]
	b14.remove("TID")
	print ""
	print "Itemsets", b14
	b21 = [i + 1 for i in range(b20)]
	for colName in b14:
		b22 = [index + 1 for index in range(b20) if b18[colName][index] == 1]
		b17 = fonk4(b21, b22)
		if (len(b22) >= b13):
			b11 += [(colName,b22, 1)]
			b12 += [(colName, len(b22), b17, 1)]
	print " "
	print "     ECLAT Algorihtm   "
	fonk3(b11, b13, b9, b15)
	print "Freq Isets || Trans id's where pr"
	b15 = sorted(b15, key = lambda x: x[2] ,reverse = True)
	for a,b,c in b15:
		print ''.join(a), "=>", b
	b23 = []
	for f in b15:
		b24 = True
		for m in b23:
			if (fonk2(f[0], m[0])):
				b24 = False
		if (b24):
			b23 += [f]
	print " "
	print "MAximal Frequent set || Trans id's where pr"
	for a,b,c in b23:
		print ''.join(a), "=>", b
	print " "
	print "     DEclat  Algorithm   "
	fonk5(b12, b13, b10, b16)
	b23 = []
	print "Freq Isets || support of b14"
	b16 = sorted(b16, key = lambda x: x[3] ,reverse = True)
	for a,b,c,d in b16:
		print ''.join(a), "=>", b
	for f in b16:
		b24 = True
		for m in b23:
			if (fonk2(f[0], m[0])):
				b24 = False
		if (b24):
			b23 += [f]
	print " "
	print "MAximal Frequent set || Trans id's where pr"
	for a,b,c,d in b23:
		print ''.join(a), "=>", b