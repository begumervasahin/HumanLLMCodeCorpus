import itertools
def fonk1(b1,vertex_num):
	for k in range(vertex_num):
		for b2,j in itertools.product(range(vertex_num),range(vertex_num)):
			if b1[b2][j] > b1[b2][k] + b1[k][j]:
				b1[b2][j] = b1[b2][k] + b1[k][j]
b1 = [[1000 for j in range(4)] for b2 in range(4)]
for b2,j in itertools.product(range(4),range(4)):
	if b2 = = j:
		b1[b2][j] = 0
b1[0][2] = -2
b1[1][0] = 4
b1[1][2] = 3
b1[2][3] = 2
b1[3][1] = -1
for b2 in range(4):
	print(b1[b2])
print('after floyd...')
fonk1(b1,4)
for b2 in range(4):
	print(b1[b2])