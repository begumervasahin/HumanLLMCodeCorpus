import math
import sys
b1 = 0;
b2 = [];
b3 = [0];
class class1:
	b4 = []
	def fonk1(self,n):
		for b19 in range(0,n):
			self.b4.append([]);
	def fonk2(self,u,b15,w):
		b5 = class2();
		b5.b6 = b15
		b5.b7 = u
		b5.b8 = w
		b5.a1 = 0
		self.b4[u-1].append(b5)
class class2:
	a1 = 0;
	b7 = 0;
	b8 = 9999999;
	b6 = 0;
	def fonk3(self):
		return self.b8
def fonk4(b5):
	b3.append(b5)
	b3[0] = len(b3)-1
	fonk5(b3[0])
	b2[b5.b6-1].a1 = b3[0]
def fonk5(b11):
	while(b11>1):
		b9 = int(b11/2)
		if(int(b3[b9].b8)>int(b3[b11].b8)):
			b2[b3[b11].b6-1].a1 = b9
			b2[b3[b9].b6-1].a1 = b11
			b10 = b3[b11]
			b3[b11] = b3[b9]
			b3[b9]=b10
			b11 = b9
		else:
			break;
def fonk6():
	b2[b3[1].b6-1].a1 = 0
	b12 = b3[0]
	b2[b3[b12].b6-1].a1 = 1
	b13 = b3[1]
	b3[1] = b3[b12]
	b3[0] = b3[0]-1
	if b3[0]>1:
		fonk8(1)
	del b3[-1]
	return b13
def fonk7(heapIndex, updatedDistance,b7):
	if(heapIndex>0):
		b3[heapIndex].b8 = updatedDistance;
		b3[heapIndex].b7 = b7;
		fonk5(heapIndex);
def fonk8(b11):
	while (2*b11<=b3[0]):
		if(2*b11 = =b3[0]) or (b3[2*b11].b8<b3[2*b11+1].b8):
			b9 = 2*b11
		else:
			b9 = 2*b11+1
		if b3[b9].b8<b3[b11].b8:
			b2[b3[b11].b6-1].a1 = b9
			b2[b3[b9].b6-1].a1 = b11
			b10 = b3[b11]
			b3[b11] = b3[b9]
			b3[b9]=b10
			b11 = b9
		else:
			break;
def fonk9(b21,w):
	fonk4(w)
	b14 = [];
	for b19 in range(len(b2)):
		if(b19!=w.b6-1):
			b5 = class2()
			b5.b6 = b19+1
			b5.a1 = 0;
			b5.b8 = 999999;
			b5.b7 = 0;
			fonk4(b5)
	while(len(b3)>1):
		b15 = fonk6()
		b14.append(b15)
		for b5 in b21.b4[b15.b6-1]:
			if(int(b5.b8)<int(b2[b5.b6-1].b8)):
				b2[b5.b6-1].b8 = b5.b8
				fonk7(b2[b5.b6-1].a1, b5.b8, b15.b6)
				b2[b5.b6-1].b7 = int(b15.b6)
	return b14
b16 = sys.argv[1]
b17 = sys.argv[2]
b18 = [line.rstrip('\n') for line in open(b16,"r")]
for b19 in range(0,len(b18)):
	if b19 = =0:
		b20 = b18[b19].split(' ');
		for b9 in range(0,len(b20)):
			if b9 = =0:
				b1 = int(b20[b9])
		b21 = class1(int(b1))
	else:
		b20 = b18[b19].split(' ');
		b21.fonk4(int(b20[0]),int(b20[1]),int(b20[2]))
		b21.fonk4(int(b20[1]),int(b20[0]),int(b20[2]))
for b19 in range(0,b1):
	b5 = class2()
	b5.b6 = b19+1;
	b5.a1 = 0;
	b5.b8 = 999999;
	b5.b7 = 0;
	b2.append(b5)
b5 = class2()
b5.b6 = 1
b5.a1 = 0;
b5.b8 = 999999;
b5.b7 = 0;
b22 = fonk9(b21,b5)
a2 = 0
for b5 in b22:
	if(b5.b6!=0 and b5.b7!=0):
		if(b5.b6 > b5.b7):
			b5.b7, b5.b6 = b5.b6, b5.b7
		a2 = a2+b5.b8
b22 = sorted(b22, key=lambda class2:(class2.b6,class2.b7))
b23 = open(b17,"w")
b23.write(str(a2))
for b5 in b22:
	if(b5.b6!=0 and b5.b7!=0):
		b23.write("\n")
		b23.write(str(b5.b6))
		b23.write(" ")
		b23.write(str(b5.b7))
		b23.write(" ")
		b23.write(str(b5.b8))