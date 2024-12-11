from math import inf
def fonk1(b5, num_vertices):
    b1 = [[[0 if b4 == j else inf for _ in range(2)] for j in range(num_vertices + 1)] for b4 in range(num_vertices + 1)]
    for b4 in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            if (b4, j) in b5:
                b1[b4][j][0] = b5[(b4, j)]
    a1 = inf
    for b3 in range(1, num_vertices + 1):
        for b4 in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                b2 = b1[b4][b3][0] + b1[b3][j][0]
                b1[b4][j][1] = min(b1[b4][j][0], b2)
                if b3 = = num_vertices:
                    a1 = min(a1, b1[b4][j][1])
                if b4 = = j and b1[b4][j][1] < 0:
                    return 'NULL'
                b1[b4][j][0], b1[b4][j][1] = b1[b4][j][1], b1[b4][j][0]
    return a1
b5 = {}
with open('g3.txt') as file:
    num_vertices, b6 = map(int, file.readline().split())
    for line in file.readlines():
        b4, j, b7 = map(int, line.split())
        b8 = (b4, j)
        if b8 not in b5 or b5[b8] > b7:
            b5[b8] = b7
print(fonk1(b5, num_vertices))