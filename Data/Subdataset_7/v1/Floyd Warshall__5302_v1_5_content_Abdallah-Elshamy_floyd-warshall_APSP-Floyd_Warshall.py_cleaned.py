from math import inf
def fonk1(b4, num_vertices):
    b1 = [[[0 if b3 == j else inf for b2 in range(2)] for j in range(num_vertices + 1)] for b3 in range(num_vertices + 1)]
    for b3 in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            if (b3, j) in b4:
                b1[b3][j][0] = b4[(b3, j)]
    a1 = inf
    for b2 in range(1, num_vertices + 1):
        for b3 in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                b1[b3][j][1] = min(b1[b3][j][0], b1[b3][b2][0] + b1[b2][j][0])
                if b2 = = num_vertices:
                    a1 = min(a1, b1[b3][j][1])
                if b3 = = j and b1[b3][j][1] < 0:
                    return 'NULL'
                b1[b3][j][1], b1[b3][j][0] = b1[b3][j][0], b1[b3][j][1]
    return a1
b4 = {}
with open('g3.txt') as f:
    num_of_vertices, b5 = map(int, f.readline().split())
    b6 = f.readlines()
    for line in b6:
        b7 = list(map(int, line.split()))
        b8 = (b7[0], b7[1])
        if b8 not in b4 or b4[b8] > b7[2]:
            b4[b8] = b7[2]
print(fonk1(b4, num_of_vertices))