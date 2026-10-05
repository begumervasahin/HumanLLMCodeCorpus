92. Repository: tule2236/superheros-social-graph
   File: degrees-of-seperation.py
   URL: https:
   Code Content:
'''
Bread First Search(BFS): algo to find the degree of seperation from 1 node to other nodes in the graphs
Step 1: initiate the starting node GRAY, all other node WHITE
Step 2: from GRAY node, color BLACK of all connected node to GRAY node
Step 3: Iteratively process the RDD
Go through, looking for Gray nodes to expand
Color nodes we're done w/t Black
Update the distance as we go
Step 4: A BFS iteration as a Map and Reduce job
The reducer:
	Combines together all nodes for the same hero ID
	Preserves the shortest distance, and the darkest color found
	Preserves the list of connections from the original node
Step 5: An Accumulator
'''
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
sc = SparkContext(conf = conf)
startCharacterID = 5306
targetCharacterID = 14
hitCounter = sc.accumulator(0)
def convertToBFS(line):
	fields = line.split()
	connections = []
	heroID = int(fields[0])
	for connection in fields[1:]:
		connections.append(int(connection))
	distance = 9999
	color = "WHITE"
	if (heroID == startCharacterID):
		color = "GRAY"
		distance = 0
	return (heroID, (connections, distance, color))
def bfsMap(node):
	heroID = node[0]
	connections = node[1][0]
	distance = node[1][1]
	color = node[1][2]
	results = []
	if (color == "GRAY"):
		for connection in connections:
			newDistance = distance + 1
			if (connection == targetCharacterID):
				hitCounter.add(1)
			results.append( (connection, ([], newDistance, "GRAY") ) )
		color = "BLACK"
	results.append( (heroID, (connections, distance, color)) )
	return results
def bfsReduce(data1, data2):
	connection1, connection2 = data1[0], data2[0]
	distance1, distance2 = data1[1], data2[1]
	color1, color2 = data1[2], data2[2]
	edges, distance, color = [], 9999, color1
	if (len(connection1) > 0):
		edges.extend(connection1)
	if (len(connection2) > 0):
		edges.extend(connection2)
	if (distance > distance1):
		distance = distance1
	if (distance > distance2):
		distance = distance2
	if ( (color1 == 'WHITE') and (color2 == 'GRAY' or color2 == 'BLACK')):
		color = color2
	if ( (color1 == 'GRAY') and (color2 == 'BLACK') ):
		color = color2
	if ( (color2 == 'WHITE') and (color1 == 'GRAY' or color1 == 'BLACK')):
		color = color1
	if ( (color2 == 'GRAY') and (color1 == 'BLACK') ):
		color = color1
	return (edges, distance, color)
graph = sc.textFile("Data/Marvel-Graph.txt")
rdd = graph.map(convertToBFS)
for iteration in range(10):
	print("Running BFS iteration
	mapper = rdd.flatMap(bfsMap)
	print("Processing " + str(mapper.count()) + "values")
	if (hitCounter.value > 0):
		print("Hit the target character! From " + str(hitCounter.value)+ "different directions.")
		break
	rdd = mapper.reduceByKey(bfsReduce)
   README Content:
[Kaggle]Using PySpark to find the most popular superhero and calculate degree of separation with BFS
Kaggle Challenge: https:
