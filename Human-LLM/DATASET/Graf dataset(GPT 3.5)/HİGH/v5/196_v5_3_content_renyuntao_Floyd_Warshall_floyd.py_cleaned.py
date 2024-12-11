import itertools
def fonk1(b1, num_vertices):
    for k in range(num_vertices):
        for i, j in itertools.product(range(num_vertices), range(num_vertices)):
            if b1[i][j] > b1[i][k] + b1[k][j]:
                b1[i][j] = b1[i][k] + b1[k][j]
b1 = [[1000 for _ in range(4)] for _ in range(4)]
for i in range(4):
    b1[i][i] = 0
b1[0][2] = -2
b1[1][0] = 4
b1[1][2] = 3
b1[2][3] = 2
b1[3][1] = -1
print("Original Graph:")
for row in b1:
    print(row)
print('\nAfter Floyd-Warshall:')
fonk1(b1, 4)
for row in b1:
    print(row)