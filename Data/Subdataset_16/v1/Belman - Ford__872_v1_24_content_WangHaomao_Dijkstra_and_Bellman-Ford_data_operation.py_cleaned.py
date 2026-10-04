from pyspark import SparkContext
from pprint import pprint
def fonk1(edge):
    u, v, b1 = edge.split(' ')
    if float(b1) < 0:
        return (u, [v + ":" + b1]), (v, []), (-1, [])
    return (u, [v + ":" + b1]), (v, [])
def fonk2(edge):
    b2 = edge.split(' ')
    if b2[0] != 'a':
        return []
    else:
        u, v, b1 = b2[1], b2[2], b2[3]
        if int(b1) < 0:
            return (u, [v + ":" + b1]), (v, []), (-1, [])
        return (u, [v + ":" + b1]), (v, [])
def fonk3(it):
    for i in it:
        if i[0] == -1:
            return i
    return (None, None)
def fonk4(node1, node2):
    if node1 is None:
        return node2
    else:
        return node1
def fonk5(filePath, b8):
    b3 = b8.textFile(filePath, 8)
    if '.gr' in filePath:
        b4 = b3.flatMap(gr_arrange_edges)
    else:
        b4 = b3.flatMap(arrange_edges)
    b5 = True if -1 in b4.mapPartitions(get_negative_flag).collect() else False
    b6 = b4.reduceByKey(lambda x, y: x + y).filter(lambda x: x[0] != -1).sortByKey()
    return b6, b5
if b7 = = '__main__':
    b8 = SparkContext.getOrCreate()
    b6, b9 = fonk5('b3/input_slides.dat', b8)
    pprint(b6.collect())
    print(f"Contains negative weights: {b9}")