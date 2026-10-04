
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
    b7 = 0 if b5 == a1 else 9999
    b8 = "GRAY" if b5 == a1 else "WHITE"
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
    connections1, distance1, b12 = data1
    connections2, distance2, b13 = data2
    b14 = connections1 + connections2
    b7 = min(distance1, distance2)
    b8 = max(b12, b13, key=lambda c: ["WHITE", "GRAY", "BLACK"].index(c))
    return (b14, b7, b8)
b15 = b2.textFile("Data/Marvel-Graph.txt")
b16 = b15.map(convertToBFS)
for iteration in range(10):
    print(f"Running BFS iteration
    b17 = b16.flatMap(bfsMap)
    print(f"Processing {b17.count()} values")
    if b3.value > 0:
        print(f"Hit the target character! From {b3.value} different directions.")
        break
    b16 = b17.reduceByKey(bfsReduce)