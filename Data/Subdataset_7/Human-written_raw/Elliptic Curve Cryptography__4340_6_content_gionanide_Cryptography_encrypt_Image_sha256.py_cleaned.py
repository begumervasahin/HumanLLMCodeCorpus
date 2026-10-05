from Tkinter import *
from tkFileDialog import *
import tkMessageBox
import os
from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import math
import hashlib
import binascii
import io
def fonk1(a,b):
	b1 = int(b,16)
	b2 = a^b1
	return b2
def fonk2():
	b3 = raw_input('Give me a b4: ')
	print ''
	b4 = b3 + '.jpg'
	b5 = hashlib.sha256(b4.encode()).hexdigest()
	print 'First sha256 pass: ' , b5 , '\n'
	b6 = hashlib.sha256(b5.encode()).hexdigest()
	print 'Second sha256 pass: ' , b6 , '\n'
	b7 = []
	b8 = []
	a1 = 0
	for x in range(len(b5)/2):
		b7.append(''.join(['0x',b5[a1:a1+2]]))
		b8.append(''.join(['0x',b6[a1:a1+2]]))
		a1+=2
	b9 = b7+b8
	return b9
def fonk3(b15):
	b10 = [ ]
	b9 = fonk2()
	b11 = Image.open(b15,mode='r')
	width,b12 = b11.size
	print 'Width: ',width,' Height: ',b12
	a1 = 0
	b2 = 0
	for y in range(b12):
		for x in range(width):
			b13 = b11.getpixel((x,y))
			b10.append(b13)
			b11.putpixel((x,y),(0,0,0))
	b11.show()
	b11.save('encrypted.jpg')
	b2 = 0
	with open('b9.txt','w') as private:
		for x in range(len(b10)):
			for y in range(3):
				private.write(str(fonk1(b10[x][y],b9[b2])))
				if(b2 = =len(b9)-1):
					b2 = 0
				else:
					b2+=1
				private.write('\n')
def fonk4(b15,private):
	b9 = fonk2()
	b14 = []
	b11 = Image.open(b15,mode='r')
	b2 = 0
	with open(private) as pk:
		for f in pk.readlines():
			b14.append(fonk1(int(f),b9[b2]))
			if(b2 = =len(b9)-1):
				b2 = 0
			else:
				b2+=1
	width,b12 = b11.size
	print 'Width: ',width,' Height: ',b12
	a2 = 0
	for y in range(b12):
		for x in range(width):
			b13 = b11.getpixel((x,y))
			b11.putpixel((x,y),(int(b14[a2]),int(b14[a2+1]),int(b14[a2+2])))
			a2+=3
	b11.show()
	b11.save('decrypted.jpg')
def fonk5():
	b15 = raw_input('Give the b15 of b11 : ')
	b16 = raw_input('b2 for encryption , b1 for decryption: ')
	if(b16 = ='b1'):
		b17 = raw_input('Give the private b9: ')
		fonk4(b15+'.jpg',b17+'.txt')
	elif(b16 = ='b2'):
		fonk3(b15+'.jpg')
	else:
		print 'Input Error'
fonk5()