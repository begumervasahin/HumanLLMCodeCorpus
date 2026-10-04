from pyspark import SparkConf, SparkContext
def convert_to_bfs(line):
    fields = line.split()
    hero_id = int(fields[0])
    connections = [int(connection) for connection in fields[1:]]
    distance = 9999
    color = "WHITE"
    if hero_id == start_character_id:
        color = "GRAY"
        distance = 0
    return (hero_id, (connections, distance, color))
def bfs_map(node):
    hero_id, (connections, distance, color) = node
    results = []
    if color == "GRAY":
        for connection in connections:
            new_distance = distance + 1
            if connection == target_character_id:
                hit_counter.add(1)
            results.append((connection, ([], new_distance, "GRAY")))
        color = "BLACK"
    results.append((hero_id, (connections, distance, color)))
    return results
def bfs_reduce(data1, data2):
    edges1, dist1, color1 = data1
    edges2, dist2, color2 = data2
    edges = edges1 if edges1 else edges2
    distance = min(dist1, dist2)
    color = max(color1, color2, key=lambda c: ("WHITE", "GRAY", "BLACK").index(c))
    return (edges, distance, color)
conf = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
sc = SparkContext(conf=conf)
start_character_id = 5306
target_character_id = 14
hit_counter = sc.accumulator(0)
graph = sc.textFile("Data/Marvel-Graph.txt")
rdd = graph.map(convert_to_bfs)
for iteration in range(10):
    print(f"Running BFS iteration
    mapper = rdd.flatMap(bfs_map)
    print(f"Processing {mapper.count()} values")
    if hit_counter.value > 0:
        print(f"Hit the target character! From {hit_counter.value} different directions.")
        break
    rdd = mapper.reduceByKey(bfs_reduce)
sc.stop()