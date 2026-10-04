a1 = 20
a2 = 99999
def fonk1(b5):
    b1 = [[[0 for z in range(a1)] for b4 in range(a1)] for i in range(a1)]
    for i in range(a1):
        for b4 in range(a1):
            b1[i][b4][0] = b5[i][b4]
    for k in range(a1):
        for i in range(a1):
            for b4 in range(a1):
                b2 = b1[i][k][0]+b1[k][b4][0]
                if(b2<b1[i][b4][0]):
                    b1[i][b4][0] = b2
                    if b1[i][b4][1] == 0:
                        b1[i][b4][1] = k
                    else:
                        for n in range(a1):
                            if b1[i][b4][n] == 0:
                                b1[i][b4][n] = k
                                break
    return b1
def fonk2(b1):
    print("\nThe following matrix shows all minimum cost paths between any two cities.\n\n")
    for i in range(a1):
        for b4 in range(a1):
            if(b1[i][b4][0] == a2):
                print("%5s" %("a2"),b3 = '|'),
            else:
                print("%5d" %(b1[i][b4][0]),b3 = '|'),
            if b4 = = a1-1:
                print("\n---------------------------------------------------------------------------------------------------------------------------")
b5 = [
    [0,a2,a2,861,a2,211,a2,a2,a2,586,a2,753,382,896,a2,a2,a2,a2,a2,a2],
    [a2,0,423,617,365,a2,a2,a2,a2,357,a2,a2,806,a2,a2,a2,a2,a2,a2,a2],
    [a2,423,0,554,359,a2,a2,a2,a2,306,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2],
    [861,617,554,0,a2,a2,a2,a2,a2,656,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2],
    [a2,365,359,a2,0,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2],
    [211,a2,a2,a2,a2,0,988,a2,293,102,a2,870,399,a2,a2,a2,a2,a2,a2,a2],
    [a2,a2,a2,a2,a2,988,0,228,43,a2,573,663,a2,a2,a2,a2,a2,a2,a2,a2],
    [a2,a2,a2,a2,a2,a2,228,0,801,a2,31,a2,a2,a2,a2,a2,a2,a2,a2,a2],
    [a2,a2,a2,a2,a2,293,43,801,0,724,927,936,a2,a2,696,a2,a2,a2,a2,a2],
    [586,357,306,656,a2,102,a2,a2,724,0,a2,736,672,804,a2,a2,a2,a2,a2,a2],
    [a2,a2,a2,a2,a2,a2,573,31,927,a2,0,634,a2,a2,927,a2,a2,a2,a2,a2],
    [753,a2,a2,a2,a2,870,663,a2,936,736,634,0,8,71,798,a2,713,a2,a2,a2],
    [382,806,a2,a2,a2,399,a2,a2,a2,672,a2,844,0,21,a2,299,a2,a2,a2,a2],
    [896,a2,a2,a2,a2,a2,a2,a2,a2,804,a2,71,21,0,244,447,726,a2,a2,a2],
    [a2,a2,a2,a2,a2,a2,a2,a2,696,a2,927,798,a2,244,0,a2,387,a2,a2,a2],
    [a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,299,447,a2,0,503,113,431,a2],
    [a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,713,a2,726,387,503,0,916,490,a2],
    [a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,113,916,0,980,326],
    [a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,431,490,980,0,455],
    [a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,a2,326,455,0]
]
print('Add two cities to calculate the minnimum cost.')
b6 = int(input('b6 = '))
b7 = int(input('b7 = '))
b8 = []
for i in range(a1):
    if (fonk1(b5)[b6][b7][i] != 0 and i != 0):
        b8.append(fonk1(b5)[b6][b7][i])
print('The minimum cost between the b9 '+str(b6)+' and the b9 '+str(b7)+' is '+str(fonk1(b5)[b6][b7][0])+', intermediate b9 = '+str(b8))
fonk2(fonk1(b5))