def fonk1(edge):
    u,v,b1 = edge.split(' ')
    if (float(b1) < 0):
        return (u, [v + ":" + b1]), (v, []), (-1, [])
    return (u,[v+":"+b1]),(v,[])
def fonk2(edge):
    b2 = edge.split(' ')
    if(b2[0] !='a'): return []
    else:
        u, v, b1 = b2[1],b2[2],b2[3]
        if(int(b1)<0):
            return (u, [v + ":" + b1]), (v, []),(-1,[])
        return (u, [v + ":" + b1]), (v, [])
def fonk3(it):
    for i in it:
        if(i[0]==-1):return i
    return (None,None)
def fonk4(b3,node2):
    if(b3 = = None):
        return node2
    else:
        return b3
def fonk5(filePath,b9):
    b4 = b9.textFile(filePath,8)
    if('.gr' in filePath):
        b5 = b4.flatMap(gr_arrange_edges)
    else:
        b5 = b4.flatMap(arrange_edges)
    b6 = True if -1 in b5.mapPartitions(get_negative_flag).collect() else False
    b7 = b5.\
        reduceByKey(lambda x, y: x + y).\
        filter(lambda x:x[0]!=-1).sortByKey()
    return b7,b6
from pyspark import SparkContext
from pprint import pprint
if b8 = = '__main__':
    b9 = SparkContext.getOrCreate()
    a,b10 = fonk5('b4/input_slides.dat', b9)
    pprint(a.collect())