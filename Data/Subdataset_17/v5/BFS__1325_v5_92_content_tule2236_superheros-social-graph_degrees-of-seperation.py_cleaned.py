
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
sc = SparkContext(conf=conf)
startCharacterID = 5306
targetCharacterID = 14
hitCounter = sc.accumulator(0)
def convert_to_bfs(line):
    fields = line.split()
    hero_id = int(fields[0])
    connections = [int(connection) for connection in fields[1:]]
    distance = 0 if hero_id == startCharacterID else 9999
    color = "GRAY" if hero_id == startCharacterID else "WHITE"
    return (hero_id, (connections, distance, color))
def bfs_map(node):
    hero_id, (connections, distance, color) = node
    results = []
    if color == "GRAY":
        for connection in connections:
            new_distance = distance + 1
            if connection == targetCharacterID:
                hitCounter.add(1)
            results.append((connection, ([], new_distance, "GRAY")))
        color = "BLACK"
    results.append((hero_id, (connections, distance, color)))
    return results
def bfs_reduce(data1, data2):
    connections1, distance1, color1 = data1
    connections2, distance2, color2 = data2
    edges = connections1 + connections2
    distance = min(distance1, distance2)
    color = max(color1, color2, key=lambda c: ["WHITE", "GRAY", "BLACK"].index(c))
    return (edges, distance, color)
graph = sc.textFile("Data/Marvel-Graph.txt")
rdd = graph.map(convert_to_bfs)
for iteration in range(10):
    print(f"Running BFS iteration
    mapper = rdd.flatMap(bfs_map)
    print(f"Processing {mapper.count()} values")
    if hitCounter.value > 0:
        print(f"Hit the target character! From {hitCounter.value} different directions.")
        break
    rdd = mapper.reduceByKey(bfs_reduce)
sc.stop()