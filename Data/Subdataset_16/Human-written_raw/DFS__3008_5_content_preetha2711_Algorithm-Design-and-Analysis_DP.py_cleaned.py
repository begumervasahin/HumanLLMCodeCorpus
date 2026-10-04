a1 = 1000
a2 = 100
b1 = [[None for x in range(a2+1)] for y in range(a1+1)]
for x in range (1,a1+1):
    for b2 in range (1,a2+1):
            if (b2 = =1):
                b1[x][b2] = x
            elif (b2>x):
                b1[x][b2] = 0
            else:
                b1[x][b2] = b1[x-1][b2] + b1[x-1][b2-1]
print b1[a1][a2]