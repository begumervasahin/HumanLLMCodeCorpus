from pyspark import SparkConf, SparkContext
def fonk1(line):
    b1 = line.split()
    b2 = []
    b3 = int(b1[0])
    for b7 in b1[1:]:
        b2.append(int(b7))
    a1 = 9999
    b4 = "WHITE"
    if b3 = = a2:
        b4 = "GRAY"
        a1 = 0
    return (b3, (b2, a1, b4))
def fonk2(node):
    b3 = node[0]
    b2 = node[1][0]
    a1 = node[1][1]
    b4 = node[1][2]
    b5 = []
    if b4 = = "GRAY":
        for b7 in b2:
            b6 = a1 + 1
            if b7 = = a3:
                b15.add(1)
            b5.append((b7, ([], b6, "GRAY")))
        b4 = "BLACK"
    b5.append((b3, (b2, a1, b4)))
    return b5
def fonk3(data1, data2):
    edges1, b8 = data1[0], data2[0]
    dist1, b9 = data1[1], data2[1]
    b12, b10 = data1[2], data2[2]
    b11 = edges1 if len(edges1) > 0 else b8
    a1 = min(dist1, b9)
    b4 = b12
    if (b12 = = 'WHITE' and b10 in ('GRAY', 'BLACK')):
        b4 = b10
    elif (b12 = = 'GRAY' and b10 == 'BLACK'):
        b4 = b10
    elif (b10 = = 'WHITE' and b12 in ('GRAY', 'BLACK')):
        b4 = b12
    elif (b10 = = 'GRAY' and b12 == 'BLACK'):
        b4 = b12
    return (b11, a1, b4)
b13 = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
b14 = SparkContext(b13=b13)
a2 = 5306
a3 = 14
b15 = b14.accumulator(0)
b16 = b14.textFile("Data/Marvel-Graph.txt")
b17 = b16.map(convertToBFS)
for iteration in range(10):
    print(f"Running BFS iteration
    b18 = b17.flatMap(bfsMap)
    print(f"Processing {b18.count()} values")
    if b15.value > 0:
        print(f"Hit the target character! From {b15.value} different directions.")
        break
    b17 = b18.reduceByKey(bfsReduce)