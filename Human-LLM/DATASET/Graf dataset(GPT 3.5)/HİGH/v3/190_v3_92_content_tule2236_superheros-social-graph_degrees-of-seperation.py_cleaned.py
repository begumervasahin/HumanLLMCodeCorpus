from pyspark import SparkConf, SparkContext
b1 = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
b2 = SparkContext(b1=b1)
a1 = 5306
a2 = 14
b3 = b2.accumulator(0)
def fonk1(line):
    b4 = line.split()
    b5 = int(b4[0])
    b6 = [int(b11) for b11 in b4[1:]]
    b7 = float('inf')
    b8 = "WHITE"
    if b5 = = a1:
        b8 = "GRAY"
        b7 = 0
    return (b5, (b6, b7, b8))
def fonk2(node):
    b5, (b6, b7, b8) = node
    b9 = []
    if b8 = = "GRAY":
        for b11 in b6:
            b10 = b7 + 1
            if b11 = = a2:
                b3.add(1)
            b9.append((b11, ([], b10, "GRAY")))
        b8 = "BLACK"
    b9.append((b5, (b6, b7, b8)))
    return b9
def fonk3(data1, data2):
    (connections1, distance1, b13) = data1
    (connections2, distance2, b14) = data2
    b12 = connections1 + connections2
    b7 = min(distance1, distance2)
    b8 = "WHITE"
    if b13 = = "GRAY" or (b13 == "BLACK" and b14 != "WHITE"):
        b8 = b13
    if b14 = = "GRAY" or (b14 == "BLACK" and b13 != "WHITE"):
        b8 = b14
    return (b12, b7, b8)
b15 = b2.textFile("Data/Marvel-Graph.txt")
b16 = b15.map(convert_to_bfs)
for iteration in range(10):
    print("Running BFS iteration
    b17 = b16.flatMap(bfs_map)
    print("Processing " + str(b17.count()) + " values")
    if b3.value > 0:
        print("Hit the target character! From " + str(b3.value) + " different directions.")
        break
    b16 = b17.reduceByKey(bfs_reduce)