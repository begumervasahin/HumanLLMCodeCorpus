
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
sc = SparkContext(conf=conf)
START_CHARACTER_ID = 5306
TARGET_CHARACTER_ID = 14
hit_counter = sc.accumulator(0)
def convert_to_bfs(line):
    fields = line.split()
    hero_id = int(fields[0])
    connections = [int(connection) for connection in fields[1:]]
    distance = 9999
    color = "WHITE"
    if hero_id == START_CHARACTER_ID:
        color = "GRAY"
        distance = 0
    return (hero_id, (connections, distance, color))
def bfs_map(node):
    hero_id, (connections, distance, color) = node
    results = []
    if color == "GRAY":
        for connection in connections:
            new_distance = distance + 1
            if connection == TARGET_CHARACTER_ID:
                hit_counter.add(1)
            results.append((connection, ([], new_distance, "GRAY")))
        color = "BLACK"
    results.append((hero_id, (connections, distance, color))))
    return results
def bfs_reduce(data1, data2):
    (connections1, distance1, color1) = data1
    (connections2, distance2, color2) = data2
    edges = connections1 + connections2
    distance = min(distance1, distance2)
    color = "WHITE"
    if color1 in ["GRAY", "BLACK"] and color2 != "WHITE":
        color = color2
    elif color2 in ["GRAY", "BLACK"]:
        color = color1
    return (edges, distance, color)
graph = sc.textFile("Data/Marvel-Graph.txt")
rdd = graph.map(convert_to_bfs)
for iteration in range(10):
    print("Running BFS iteration
    mapper = rdd.flatMap(bfs_map)
    print("Processing " + str(mapper.count()) + " values")
    if hit_counter.value > 0:
        print("Hit the target character! From " + str(hit_counter.value) + " different directions.")
        break
    rdd = mapper.reduceByKey(bfs_reduce)