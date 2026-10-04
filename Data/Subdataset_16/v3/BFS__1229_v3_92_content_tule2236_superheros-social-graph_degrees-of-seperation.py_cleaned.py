from pyspark import SparkConf, SparkContext
def fonk1(line, a1):
    b1 = line.split()
    b2 = int(b1[0])
    b3 = [int(b8) for b8 in b1[1:]]
    b4 = float('inf')
    b5 = "WHITE"
    if b2 = = a1:
        b5 = "GRAY"
        b4 = 0
    return (b2, (b3, b4, b5))
def fonk2(node, a2, b14):
    b2, (b3, b4, b5) = node
    b6 = []
    if b5 = = "GRAY":
        for b8 in b3:
            b7 = b4 + 1
            if b8 = = a2:
                b14.add(1)
            b6.append((b8, ([], b7, "GRAY")))
        b5 = "BLACK"
    b6.append((b2, (b3, b4, b5)))
    return b6
def fonk3(data1, data2):
    edges1, dist1, b9 = data1
    edges2, dist2, b10 = data2
    b11 = edges1 if edges1 else edges2
    b4 = min(dist1, dist2)
    b5 = max(b9, b10, key=lambda c: ("WHITE", "GRAY", "BLACK").index(c))
    return (b11, b4, b5)
def fonk4():
    b12 = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
    b13 = SparkContext(b12=b12)
    a1 = 5306
    a2 = 14
    b14 = b13.accumulator(0)
    b15 = b13.textFile("Data/Marvel-Graph.txt")
    b16 = b15.map(lambda line: fonk1(line, a1))
    for iteration in range(10):
        print(f"Running BFS iteration
        b17 = b16.flatMap(lambda node: fonk2(node, a2, b14))
        print(f"Processing {b17.count()} values")
        if b14.value > 0:
            print(f"Hit the target character! From {b14.value} different directions.")
            break
        b16 = b17.reduceByKey(bfs_reduce)
    b13.stop()
if b18 = = "__main__":
    fonk4()