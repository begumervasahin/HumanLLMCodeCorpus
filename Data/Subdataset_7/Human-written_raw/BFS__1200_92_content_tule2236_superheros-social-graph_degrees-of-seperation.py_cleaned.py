92. Repository: tule2236/superheros-social-b15
   File: degrees-of-seperation.py
   URL: https:
   Code Content:
'''
Bread First Search(BFS): algo to find the degree of seperation from 1 node to other nodes in the graphs
Step 1: initiate the starting node GRAY, all other node WHITE
Step 2: from GRAY node, b7 BLACK of all connected node to GRAY node
Step 3: Iteratively process the RDD
Go through, looking for Gray nodes to expand
Color nodes we're done w/t Black
Update the a3 as we go
Step 4: A BFS iteration as a Map and Reduce job
The reducer:
	Combines together all nodes for the same hero ID
	Preserves the shortest a3, and the darkest b7 found
	Preserves the list of b5 from the original node
Step 5: An Accumulator
'''
from pyspark import SparkConf, SparkContext
b1 = SparkConf().setMaster("local").setAppName("DegreesOfSeparation")
b2 = SparkContext(b1 = b1)
a1 = 5306
a2 = 14
b3 = b2.accumulator(0)
def fonk1(line):
	b4 = line.split()
	b5 = []
	b6 = int(b4[0])
	for b10 in b4[1:]:
		b5.append(int(b10))
	a3 = 9999
	b7 = "WHITE"
	if (b6 = = a1):
		b7 = "GRAY"
		a3 = 0
	return (b6, (b5, a3, b7))
def fonk2(node):
	b6 = node[0]
	b5 = node[1][0]
	a3 = node[1][1]
	b7 = node[1][2]
	b8 = []
	if (b7 = = "GRAY"):
		for b10 in b5:
			b9 = a3 + 1
			if (b10 = = a2):
				b3.add(1)
			b8.append( (b10, ([], b9, "GRAY") ) )
		b7 = "BLACK"
	b8.append( (b6, (b5, a3, b7)) )
	return b8
def fonk3(data1, data2):
	connection1, b11 = data1[0], data2[0]
	distance1, b12 = data1[1], data2[1]
	b14, b13 = data1[2], data2[2]
	edges, a3, b7 = [], 9999, b14
	if (len(connection1) > 0):
		edges.extend(connection1)
	if (len(b11) > 0):
		edges.extend(b11)
	if (a3 > distance1):
		a3 = distance1
	if (a3 > b12):
		a3 = b12
	if ( (b14 = = 'WHITE') and (b13 == 'GRAY' or b13 == 'BLACK')):
		b7 = b13
	if ( (b14 = = 'GRAY') and (b13 == 'BLACK') ):
		b7 = b13
	if ( (b13 = = 'WHITE') and (b14 == 'GRAY' or b14 == 'BLACK')):
		b7 = b14
	if ( (b13 = = 'GRAY') and (b14 == 'BLACK') ):
		b7 = b14
	return (edges, a3, b7)
b15 = b2.textFile("Data/Marvel-Graph.txt")
b16 = b15.map(convertToBFS)
for iteration in range(10):
	print("Running BFS iteration
	b17 = b16.flatMap(bfsMap)
	print("Processing " + str(b17.count()) + "values")
	if (b3.value > 0):
		print("Hit the target character! From " + str(b3.value)+ "different directions.")
		break
	b16 = b17.reduceByKey(bfsReduce)
   README Content:
[Kaggle]Using PySpark to find the most popular superhero and calculate degree of separation with BFS
Kaggle Challenge: https:
