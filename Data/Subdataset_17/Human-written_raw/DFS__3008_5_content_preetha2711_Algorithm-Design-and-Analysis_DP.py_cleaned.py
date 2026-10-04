i = 1000
k = 100
p = [[None for x in range(k+1)] for y in range(i+1)]
for x in range (1,i+1):
    for j in range (1,k+1):
            if (j==1):
                p[x][j] = x
            elif (j>x):
                p[x][j] = 0
            else:
                p[x][j] = p[x-1][j] + p[x-1][j-1]
print p[i][k]