def fonk1(sender,start,sm,b3,b5):
    if start in b5:
        b1 = b5[start]
        for x in b1:
            b2 = sm+x[1]
            if b3[x[0]-1]==None or b2<b3[x[0]-1]:
                b3[x[0]-1]=b2
                b3 = Solution.fonk1(start,x[0],b2,b3,b5)
    return b3
b4 = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
a1 = 5
a2 = 5
b5 = {}
for i in b4:
    if i[0] in b5:
        b5[i[0]].append([i[1],i[2]])
    else:
        b5[i[0]]=[[i[1],i[2]]]
b3 = [None]*a1
b3[a2-1]=0
b3 = fonk1(a2,a2,0,b3,b5)
if None not in b3:
    return max(b3)
else:
    return -1