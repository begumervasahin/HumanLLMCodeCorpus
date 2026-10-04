def getPath(sender,start,sm,pathSum,htTimes):
    if start in htTimes:
        arr=htTimes[start]
        for x in arr:
            nwsm=sm+x[1]
            if pathSum[x[0]-1]==None or nwsm<pathSum[x[0]-1]:
                pathSum[x[0]-1]=nwsm
                pathSum=Solution.getPath(start,x[0],nwsm,pathSum,htTimes)
    return pathSum
times=[[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
N=5
K=5
htTimes={}
for i in times:
    if i[0] in htTimes:
        htTimes[i[0]].append([i[1],i[2]])
    else:
        htTimes[i[0]]=[[i[1],i[2]]]
pathSum=[None]*N
pathSum[K-1]=0
pathSum=getPath(K,K,0,pathSum,htTimes)
if None not in pathSum:
    return max(pathSum)
else:
    return -1