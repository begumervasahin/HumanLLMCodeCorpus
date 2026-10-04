import numpy as np
edges2= {
	"v_start": {"1_start":0 ,"2_start":0},
	"1_start": {"1_finish":40},
	"2_start": {"2_finish":36},
	"1_finish": {"v_finish":0},
	"2_finish": {"v_finish":0, "1_start":0}
}
def connections(v_start):
	return edges2.get(v_start)
def weight(start, finish):
	x=edges2.get(start)
	return x.get(finish)
def LongestPath(edges2, Ppaths):
	for i in Ppaths:
		for j in connections(i):
			Ppaths.append([i])
	print Ppaths
Ppaths=['v_start']
LongestPath(edges2, Ppaths)
def ShortestPath(edges2):
	Ppaths=[]
	Pweight=[]
	for i in edges2['v_start'].keys():
		Ppaths.append([i])
		Pweight.append(edges2['v_start'].get(i))
	for i in Ppaths:
		pathend= i[-1]
		if len(edges2[pathend].keys()) ==1:
			i.extend(edges2[pathend].keys())
			Pweight.extend(edges2[pathend].values())
		if len(edges2[pathend].keys())>1:
			for j in edges2[pathend].keys():
				Ppaths.append([i])
				Ppaths[-1].extend(j)
		for j in edges2[i].keys():
			Ppaths.append([])
	return Ppaths ,Pweight
print ShortestPath(edges2)