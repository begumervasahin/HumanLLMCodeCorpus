import sys
import re as re
import numpy as py
b1 = open('Graph.dat', 'r')
b2 = int(b1.readline())
a1 = 0
b3 = []
while (a1 != b2):
	b3.append(b1.readline())
	a1 = a1 + 1
b4 = ''
for i in range(1, b2 + 1):
	b4 += str(i) + '+' + '(.+)'
b5 = re.compile(b4)
a1 = 0
b6 = py.zeros(shape = (b2, b2))
for i in b3:
	b7 = str(i)
	b8 = b5.match(b7)
	for x in range(0, b2):
		b6[a1][x] = int(b8.group(x + 1))
	a1 += 1
b9 = open('Input.dat', 'r')
b10 = []
while True:
	b7 = str(b9.readline())
	if b7 = = str(0):
		break;
	b10.append(b7.split('\n')[0])
b10 = py.array(b10)
b11 = []
b12 = []
b13 = len(b10)
a1 = 0
while (a1 < b13):
	if (a1 % b14 = = 0):
		b11.append(b10[a1])
	if (a1 % b14 = = 1):
		b12.append(b10[a1])
	a1 += 1
b11 = py.array(b11)
b12 = py.array(b12)
a2 = 0
b15 = open('/Users/JcShang/Desktop/Output.dat', 'w+')
while (a2 != len(b11)):
	b16 = int(b11[a2]) - 1
	b17 = int(b12[a2]) - 1
	b18 = py.zeros(shape = (b2))
	b19 = py.array([])
	b19 = py.append(b19, [b16], axis = 0)
	b20 = py.zeros(shape = (b2))
	while True:
		a3 = 999
		for i in b19:
			for j in range(0, b2):
				if j not in b19:
					if b20[int(i)] + b6[int(i)][int(j)] < a3 and b6[int(i)][int(j)] > 0:
						a3 = b20[int(i)] + b6[int(i)][int(j)]
						b21 = j
						b22 = i
		b19 = py.append(b19, [b21], axis = 0)
		b20[b21] = b20[int(b22)] + b6[int(b22)][b21]
		b18[b21] = b22
		if b17 in b19:
			break
	b23 = py.array([])
	b23 = py.append(b23, [b17], axis = 0)
	while b16 not in b23:
		b23 = py.append(b23, [b18[int(b23[-1])]], axis = 0)
	b15.write(str(b20[b17]) + '\n')
	b24 = len(b23) - 1
	while (b24 >= 0):
		b15.write(str(b23[-1] + 1) + '\n')
		b23 = b23[:-1]
		b24 -= 1
	b15.write('FFFF' + '\n')
	a2 += 1
b15.write('0' + '\n')