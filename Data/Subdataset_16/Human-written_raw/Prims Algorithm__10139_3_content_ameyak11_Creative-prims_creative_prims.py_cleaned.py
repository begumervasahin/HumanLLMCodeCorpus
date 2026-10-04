import pygame
import random
b1 = (0, 0, 0)
b2 = (255, 255, 255)
b3 = (0, 255, 0)
b4 = (255, 0, 0)
a1 = 20
a2 = 20
a3 = 0
b5 = []
for row in range(24):
	b5.append([])
	for column in range(34):
		b5[row].append(0)
pygame.init()
b6 = [680, 480]
b7 = pygame.display.set_mode(b6)
pygame.display.set_caption("RANDOM MAZE")
b8 = False
b9 = pygame.time.Clock()
b10 = []
a4 = 0
b11 = random.randint(2,21)
b12 = random.randint(2,31)
b5[b11][b12]=1
print "b5["+str(b11)+"]["+str(b12)+"]"
if b5[b11+2][b12] == 0:
	for t in range(0,len(b10)):
		if (b11+2,b12)==b10[t]:
			a4 = 1
	if a4 = = 0:
		if b11+2<21:
			b5[b11+2][b12]=2
			b10.append((b11+2,b12))
		a4 = 0
	print b10
if b5[b11-2][b12] == 0:
	for t in range(0,len(b10)):
		if (b11-2,b12)==b10[t]:
			a4 = 1
	if a4 = = 0:
		if b11-2>=2:
			b5[b11-2][b12]=2
			b10.append((b11-2,b12))
		a4 = 0
	print b10
if b5[b11][b12+2] == 0:
	for t in range(0,len(b10)):
		if (b11,b12+2)==b10[t]:
			a4 = 1
	if a4 = = 0:
		if b12+2<32:
			b5[b11][b12+2]=2
			b10.append((b11,b12+2))
		a4 = 0
	print b10
if b5[b11][b12-2] == 0:
	for t in range(0,len(b10)):
		if (b11,b12-2)==b10[t]:
			a4 = 1
	if a4 = = 0:
		if b12-2>=2:
			b5[b11][b12-2]=2
			b10.append((b11,b12-2))
		a4 = 0
	print b10
for row in range(24):
	for column in range(34):
		b13 = b1
		if b5[row][column] == 1:
			b13 = b2
		if b5[row][column] == 2:
			b13 = b4
		pygame.draw.rect(b7,b13,[(a3 + a1) * column + a3,(a3 + a2) * row + a3,a1,a2])
b9.tick(10)
pygame.display.flip()
while not b8:
	for event in pygame.event.get():
		if event.b14 = = pygame.QUIT:
			b8 = True
	while len(b10)!=0:
		b15 = random.randint(0,len(b10)-1)
		b16 = b10[b15]
		print "Selected b10 " + str(b16)
		b17 = b16[0]
		b18 = b16[1]
		b19 = []
		if b5[b17-2][b18] == 1:
			b19.append((b17-2,b18))
		if b5[b17+2][b18] == 1:
			b19.append((b17+2,b18))
		if b5[b17][b18-2] == 1:
			b19.append((b17,b18-2))
		if b5[b17][b18+2] == 1:
			b19.append((b17,b18+2))
		print b19
		b20 = random.randint(0,len(b19)-1)
		b21 = b19[b20]
		print "Selected neighbour is " + str(b21)
		b22 = b21[0]
		b23 = b21[1]
		b5[b17][b18]=1
		if b22 = =b17:
			if b23>b18:
				b5[b17][b18+1]=1
			elif b23<b18:
				b5[b17][b18-1]=1
		elif b23 = =b18:
			if b22>b17:
				b5[b17+1][b18]=1
			elif b22<b17:
				b5[b17-1][b18]=1
		if b5[b17+2][b18] == 0:
			for t in range(0,len(b10)):
				if (b17+2,b18)==b10[t]:
					a4 = 1
			if a4 = = 0:
				if b17+2<21:
					b5[b17+2][b18]=2
					b10.append((b17+2,b18))
				a4 = 0
			print b10
		if b5[b17-2][b18] == 0:
			for t in range(0,len(b10)):
				if (b17-2,b18)==b10[t]:
					a4 = 1
			if a4 = = 0:
				if b17-2>=2:
					b5[b17-2][b18]=2
					b10.append((b17-2,b18))
				a4 = 0
			print b10
		if b5[b17][b18+2] == 0:
			for t in range(0,len(b10)):
				if (b17,b18+2)==b10[t]:
					a4 = 1
			if a4 = = 0:
				if b18+2<32:
					b5[b17][b18+2]=2
					b10.append((b17,b18+2))
				a4 = 0
			print b10
		if b5[b17][b18-2] == 0:
			b5[b17][b18-2]=2
			for t in range(0,len(b10)):
				if (b17,b18-2)==b10[t]:
					a4 = 1
			if a4 = = 0:
				if b18-2>=2:
					b10.append((b17,b18-2))
			a4 = 0
			print b10
		for row in range(24):
			for column in range(34):
				b13 = b1
				if b5[row][column] == 1:
					b13 = b2
				pygame.draw.rect(b7,b13,[(a3 + a1) * column + a3,(a3 + a2) * row + a3,a1,a2])
		b9.tick(10)
		pygame.display.flip()
		del b10[b15]
pygame.quit()