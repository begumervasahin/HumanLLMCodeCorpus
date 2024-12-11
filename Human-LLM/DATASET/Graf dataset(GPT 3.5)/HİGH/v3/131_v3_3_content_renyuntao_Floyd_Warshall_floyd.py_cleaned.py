import itertools
def fonk1(b1, num_vertices):
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if b1[i][j] > b1[i][k] + b1[k][j]:
                    b1[i][j] = b1[i][k] + b1[k][j]
b1 = [
    [1000, 1000, -2, 1000],
    [4, 1000, 3, 1000],
    [1000, 1000, 1000, 2],
    [1000, -1, 1000, 1000]
]
print("Original Graph:")
for row in b1:
    print(row)
print('\nAfter Floyd-Warshall:')
fonk1(b1, 4)
for row in b1:
    print(row)