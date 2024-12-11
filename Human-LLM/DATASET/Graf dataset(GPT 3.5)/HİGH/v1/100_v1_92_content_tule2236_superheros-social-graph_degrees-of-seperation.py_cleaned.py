from pyspark import SparkConf, SparkContext
b1 = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
b2 = SparkContext(b1=b1)
a1 = 5306
a2 = 14
b3 = b2.accumulator(0)
def fonk1(line):
    b4 = line.split()
    b5 = int(b4[0])
    b6 = [int(b10) for b10 in b4[1:]]
    a3 = 9999
    b7 = "WHITE"
    if b5 = = a1:
        b7 = "GRAY"
        a3 = 0
    return (b5, (b6, a3, b7))
def fonk2(node):
    b5, (b6, a3, b7) = node
    b8 = []
    if b7 = = "GRAY":
        for b10 in b6:
            b9 = a3 + 1
            if b10 = = a2:
                b3.add(1)
            b8.append((b10, ([], b9, "GRAY")))
        b7 = "BLACK"
    b8.append((b5, (b6, a3, b7)))
    return b8
def fonk3(data1, data2):
    (connections1, distance1, b12) = data1
    (connections2, distance2, b13) = data2
    b11 = connections1 + connections2
    a3 = min(distance1, distance2)
    b7 = "WHITE"
    if b12 = = "GRAY" or (b12 == "BLACK" and b13 != "WHITE"):
        b7 = b12
    if b13 = = "GRAY" or (b13 == "BLACK" and b12 != "WHITE"):
        b7 = b13
    return (b11, a3, b7)
b14 = b2.textFile("Data/Marvel-Graph.txt")
b15 = b14.map(convertToBFS)
for iteration in range(10):
    print("Running BFS iteration
    b16 = b15.flatMap(bfsMap)
    print("Processing " + str(b16.count()) + " values")
    if b3.value > 0:
        print("Hit the target character! From " + str(b3.value) + " different directions.")
        break
    b15 = b16.reduceByKey(bfsReduce)