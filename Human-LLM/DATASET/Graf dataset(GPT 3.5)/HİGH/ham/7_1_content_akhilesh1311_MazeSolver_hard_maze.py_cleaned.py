import random
import copy
import sys
def fonk1(b17, b1 = False):
	b2 = []
	b3 = []
	b4 = set()
	b3.append((0, 0))
	b4.add((0, 0))
	b5 = {}
	while b3:
		cur_i, b6 = b3.pop(0)
		if b17[cur_i][b6] == 'G':
			a1 = 0
			while cur_i + b6:
				b2.append((cur_i, b6))
				cur_i, b6 = b5[(cur_i, b6)]
				a1 += 1
			if b1:
				for p, q in b2:
					if b17[p][q] in ['O', 'X']:
						b17[p][q] = '
				fonk3(b17)
				return
			else:
				return a1
		for i, j in [(cur_i - 1, b6), (cur_i + 1, b6), (cur_i, b6 - 1), (cur_i, b6 + 1)]:
			if 0 <= i < len(b17) and 0 <= j < len(b17) and b17[i][j] != 'X' and (i, j) not in b4:
				b3.append((i, j))
				b5[(i, j)] = (cur_i, b6)
				b4.add((i, j))
	return -1
def fonk2(b16):
	b7 = []
	for b18, b13 in enumerate(b16):
		b8 = fonk1(b13)
		b7.append((b8, random.random(), b18))
	b7.sort(b9 = True)
	return b7[0][-1]
def fonk3(b13):
	for row in b13:
		print(*row, b10 = ' ')
	print('\n\n')
if b11 = = '__main__':
	dim, p, b12 = 15, 0.3, 100
	b13 = []
	for i in range(dim):
		b14 = []
		for j in range(dim):
			b14.append('X' if random.random() < p else 'O')
		b13.append(b14)
	b13[0][0] = 'S'
	b13[dim - 1][dim - 1] = 'G'
	print("Displaying b13 from part-1: ")
	fonk3(b13)
	print("Displaying b13 from part-1 with the shortest b2: ")
	fonk1(b13, True)
	for i in range(dim):
		for j in range(dim):
			if b13[i][j] == '
				b13[i][j] = 'O'
	x, b15 = random.randint(0, dim - 1), random.randint(0, dim - 1)
	for _ in range(b12):
		b16 = [b13]
		for i, j in [(x - 1, b15), (x + 1, b15), (x, b15 - 1), (x, b15 + 1)]:
			if 0 <= i < dim and 0 <= j < dim and b13[i][j] in ['O', 'X']:
				b17 = copy.deepcopy(b13)
				b17[i][j] = 'O' if b17[i][j] == 'X' else 'X'
				b16.append(b17)
		b18 = fonk2(b16)
		b13 = b16[b18]
		if b18:
			x, b15 = [(x - 1, b15), (x + 1, b15), (x, b15 - 1), (x, b15 + 1)][b18 - 1]
		else:
			x, b15 = random.randint(0, dim - 1), random.randint(0, dim - 1)
	print("Displaying b13 after hill climbing: ")
	fonk3(b13)
	print("Displaying b13 with the shortest b2 after hill climbing: ")
	fonk1(b13, True)