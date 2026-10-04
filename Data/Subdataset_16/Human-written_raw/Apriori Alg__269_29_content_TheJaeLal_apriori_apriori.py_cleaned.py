29. Repository: TheJaeLal/apriori
   File: apriori.py
   URL: https:
   Code Content:
def fonk1(fname):
	b1 = open(fname,'r')
	b2 = b1.read().split('\n')
	b2 = [line.split(':')[1].split(',') for line in b2 if not (line.startswith('
	b1.close()
	return b2
def fonk2(b5,b10):
	return [b8 for b8 in b5 if b5[b8] >= b10]
def fonk3(b12):
	b3 = list()
	for i in range(len(b12)):
		for j in range(i+1,len(b12)):
			b4 = b12[i].union(b12[j])
			b3.append(b4)
	return b3
def fonk4(b3,b7):
	b5 = dict()
	for b8 in b3:
		for entry in b7:
			if b8.issubset(entry):
				if b8 in b5:
					b5[b8] += 1
				else:
					b5[b8] = 1
	return b5
b6 = 'input.dat'
b7 = fonk1(b6)
b7 = [frozenset(entry) for entry in b7]
for d in b7:
	print(d)
b5 = dict()
for entry in b7:
	for b8 in entry:
		b8 = frozenset([b8])
		if b8 in b5:
			b5[b8]+=1
		else:
			b5[b8]=1
print('***Initial Frequency Count***')
for b8 in b5:
	print(b8,':',b5[b8])
print('Enter Support_Threshold:')
print('>>> ',b9 = '')
b10 = int(input())
print('b10 = ',b10)
b11 = b5
while(True):
	b12 = fonk2(b5,b10)
	print('\n****Frequent Items****')
	for f in b12:
		print(f)
	if len(b12)<1:
		b12 = b11
		break
	print("\n***New Iteration***")
	b3 = fonk3(b12)
	b11 = b12
	b5 = fonk4(b3,b7)
	print('\n***Frequency Count***')
	for b8 in b5:
		print(b8,':',b5[b8])
print('\n***************************************************************')
print('The most frequenty associated items are:')
for b8 in b12:
	b13 = list()
	for i in b8:
		b13.append(i)
	print('{','{}'.format(" ,".join(b13)),'}')
print('\n')
   README Content:
Implementation of Association Rule Mining using Apriori Algorithm
