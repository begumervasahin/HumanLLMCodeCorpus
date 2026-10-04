import math
import sys
b1 = 0;
b2 = 0;
b3 = [];
b4 = [0];
class class1:
	b5 = []
	def fonk1(self,n):
		for i in range(0,n):
			self.b5.append([]);
	def fonk2(self,u,b16,w):
		b6 = class2();
		b6.b7 = b16
		b6.b8 = u
		b6.b9 = w
		b6.a1 = 0
		self.b5[u-1].append(b6)
class class2:
	a1 = 0;
	b8 = 0;
	b9 = 9999999;
	b7 = 0;
	def fonk3(self):
		return self.b9
def fonk4(b6):
	b4.append(b6)
	b4[0] = len(b4)-1
	fonk5(b4[0])
	b3[b6.b7-1].a1 = b4[0]
def fonk5(b12):
	while(b12>1):
		b10 = b12/2
		if(int(b4[b10].b9)>int(b4[b12].b9)):
			b3[b4[b12].b7-1].a1 = b10
			b3[b4[b10].b7-1].a1 = b12
			b11 = b4[b12]
			b4[b12] = b4[b10]
			b4[b10]=b11
			b12 = b10
		else:
			break;
def fonk6():
	b3[b4[1].b7-1].a1 = 0
	b13 = b4[0]
	b3[b4[b13].b7-1].a1 = 1
	b14 = b4[1]
	b4[1] = b4[b13]
	b4[0] = b4[0]-1
	if b4[0]>1:
		fonk8(1)
	del b4[-1]
	return b14
def fonk7(heapIndex, updatedDistance,b8):
	if(heapIndex>0):
		b4[heapIndex].b9 = updatedDistance;
		b4[heapIndex].b8 = b8;
		fonk5(heapIndex);
def fonk8(b12):
	while (2*b12<=b4[0]):
		if(2*b12 = =b4[0]) or (b4[2*b12].b9<b4[2*b12+1].b9):
			b10 = 2*b12
		else:
			b10 = 2*b12+1
		if b4[b10].b9<b4[b12].b9:
			b3[b4[b12].b7-1].a1 = b10
			b3[b4[b10].b7-1].a1 = b12
			b11 = b4[b12]
			b4[b12] = b4[b10]
			b4[b10]=b11
			b12 = b10
		else:
			break;
def fonk9(b18,w):
	fonk4(w)
	b15 = [];
	for i in range(len(b3)):
		if(i!=w.b7-1):
			b6 = class2()
			b6.b7 = i+1
			b6.a1 = 0;
			b6.b9 = 999999;
			b6.b8 = 0;
			fonk4(b6)
	while(len(b4)>1):
		b16 = fonk6()
		b15.append(b16)
		for b6 in b18.b5[b16.b7-1]:
			if(int(b6.b9)<int(b3[b6.b7-1].b9)):
				b3[b6.b7-1].b9 = b6.b9
				fonk7(b3[b6.b7-1].a1, b6.b9, b16.b7)
				b3[b6.b7-1].b8 = int(b16.b7)
	return b15
b17 = raw_input();
b17 = b17.split(" ");
b1 = int(b17[0]);
b2 = int(b17[1])
b18 = class1(b1)
for i in range(0,int(b17[1])):
	b19 = raw_input();
	b19 = b19.split(' ');
	b18.fonk4(int(b19[0]),int(b19[1]),int(b19[2]))
	b18.fonk4(int(b19[1]),int(b19[0]),int(b19[2]))
for i in range(0,b1):
	b6 = class2()
	b6.b7 = i+1;
	b6.a1 = 0;
	b6.b9 = 999999;
	b6.b8 = 0;
	b3.append(b6)
b6 = class2()
b6.b7 = 1
b6.a1 = 0;
b6.b9 = 999999;
b6.b8 = 0;
b20 = fonk9(b18,b6)
a2 = 0
for b6 in b20:
	if(b6.b7!=0 and b6.b8!=0):
		a2 = a2+b6.b9
print a2