
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
sc = SparkContext(conf=conf)
startCharacterID = 5306
targetCharacterID = 14
hitCounter = sc.accumulator(0)
def convertToBFS(line):
    fields = line.split()
    heroID = int(fields[0])
    connections = [int(connection) for connection in fields[1:]]
    distance = 0 if heroID == startCharacterID else 9999
    color = "GRAY" if heroID == startCharacterID else "WHITE"
    return (heroID, (connections, distance, color))
def bfsMap(node):
    heroID, (connections, distance, color) = node
    results = []
    if color == "GRAY":
        for connection in connections:
            newDistance = distance + 1
            if connection == targetCharacterID:
                hitCounter.add(1)
            results.append((connection, ([], newDistance, "GRAY")))
        color = "BLACK"
    results.append((heroID, (connections, distance, color)))
    return results
def bfsReduce(data1, data2):
    connections1, distance1, color1 = data1
    connections2, distance2, color2 = data2
    edges = connections1 + connections2
    distance = min(distance1, distance2)
    color = max(color1, color2, key=lambda c: ["WHITE", "GRAY", "BLACK"].index(c))
    return (edges, distance, color)
graph = sc.textFile("Data/Marvel-Graph.txt")
rdd = graph.map(convertToBFS)
for iteration in range(10):
    print(f"Running BFS iteration
    mapper = rdd.flatMap(bfsMap)
    print(f"Processing {mapper.count()} values")
    if hitCounter.value > 0:
        print(f"Hit the target character! From {hitCounter.value} different directions.")
        break
    rdd = mapper.reduceByKey(bfsReduce)