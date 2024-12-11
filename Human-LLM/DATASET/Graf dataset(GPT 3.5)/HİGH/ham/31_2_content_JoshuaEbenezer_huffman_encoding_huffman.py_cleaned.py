import numpy as np
from scipy.misc import imread,imresize
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter
import queue
class class1:
	def fonk1(self):
		self.b1 = None
		self.b2 = None
		self.b3 = None
		self.b4 = None
		self.b5 = None
	def fonk2(self, other):
		if (self.b1 < other.b1):
			return 1
		else:
			return 0
	def fonk3(self, other):
		if (self.b1 > other.b1):
			return 1
		else:
			return 0
def fonk4(b20):
	b6 = np.rint(b20[:,:,0]*0.2989 + b20[:,:,1]*0.5870 + b20[:,:,2]*0.1140)
	b6 = b6.astype(int)
	return b6
def fonk5(b3):
    b7 = b9 = 1;
    b8 = b10=0
    for idx,element in enumerate(b3):
        if (element < b7):
            b9 = b7
            b10 = b8
            b7 = element
            b8 = idx
        elif (element < b9 and element != b7):
            b9 = element
    return b8,b7,b10,b9
def fonk6(b22):
	b11 = queue.PriorityQueue()
	for b18,probability in enumerate(b22):
		b12 = class1()
		b12.b3 = b18
		b12.b1 = probability
		b11.put(b12)
	while (b11.qsize()>1):
		b13 = class1()
		b14 = b11.get()
		b15 = b11.get()
		b13.b4 = b14
		b13.b5 = b15
		b16 = b14.b1+b15.b1
		b13.b1 = b16
		b11.put(b13)
	return b11.get()
def fonk7(b23,b24,b26):
	if (b23.b4 is not None):
		b24[huffman_traversal.a1] = 1
		huffman_traversal.a1+=1
		fonk7(b23.b4,b24,b26)
		huffman_traversal.a1-=1
	if (b23.b5 is not None):
		b24[huffman_traversal.a1] = 0
		huffman_traversal.a1+=1
		fonk7(b23.b5,b24,b26)
		huffman_traversal.a1-=1
	else:
		huffman_traversal.b25[b23.b3] = huffman_traversal.a1
		b17 = ''.join(str(cell) for cell in b24[1:huffman_traversal.a1])
		b18 = str(b23.b3)
		b19 = b18+' '+ b17+'\n'
		b26.write(b19)
	return
b20 = imread('tiger.bmp')
b20 = imresize(b20,10)
b6 = fonk4(b20)
b21 = np.bincount(b6.ravel(),minlength=256)
b22 = b21/np.sum(b21)
b23 = fonk6(b22)
b24 = np.ones([64],dtype=int)
huffman_traversal.b25 = np.empty(256,dtype=int)
huffman_traversal.a1 = 0
b26 = open('codes.txt','w')
fonk7(b23,b24,b26)
b27 = b20.shape[0]*b20.shape[1]*8
b28 = (1-np.sum(huffman_traversal.b25*b21)/b27)*100
print('Compression is ',b28,' percent')