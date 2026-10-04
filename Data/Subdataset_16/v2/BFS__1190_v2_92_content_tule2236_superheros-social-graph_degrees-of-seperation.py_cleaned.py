from pyspark import SparkConf, SparkContext
def fonk1(line):
    b1 = line.split()
    b2 = int(b1[0])
    b3 = [int(b7) for b7 in b1[1:]]
    a1 = 9999
    b4 = "WHITE"
    if b2 = = a2:
        b4 = "GRAY"
        a1 = 0
    return (b2, (b3, a1, b4))
def fonk2(node):
    b2, (b3, a1, b4) = node
    b5 = []
    if b4 = = "GRAY":
        for b7 in b3:
            b6 = a1 + 1
            if b7 = = a3:
                b13.add(1)
            b5.append((b7, ([], b6, "GRAY")))
        b4 = "BLACK"
    b5.append((b2, (b3, a1, b4)))
    return b5
def fonk3(data1, data2):
    edges1, dist1, b8 = data1
    edges2, dist2, b9 = data2
    b10 = edges1 if edges1 else edges2
    a1 = min(dist1, dist2)
    b4 = max(b8, b9, key=lambda c: ("WHITE", "GRAY", "BLACK").index(c))
    return (b10, a1, b4)
b11 = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
b12 = SparkContext(b11=b11)
a2 = 5306
a3 = 14
b13 = b12.accumulator(0)
b14 = b12.textFile("Data/Marvel-Graph.txt")
b15 = b14.map(convert_to_bfs)
for iteration in range(10):
    print(f"Running BFS iteration
    b16 = b15.flatMap(bfs_map)
    print(f"Processing {b16.count()} values")
    if b13.value > 0:
        print(f"Hit the target character! From {b13.value} different directions.")
        break
    b15 = b16.reduceByKey(bfs_reduce)
b12.stop()