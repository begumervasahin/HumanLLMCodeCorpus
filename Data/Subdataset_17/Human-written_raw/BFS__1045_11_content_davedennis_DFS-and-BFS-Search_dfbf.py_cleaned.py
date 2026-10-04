11. Repository: davedennis/DFS-and-BFS-Search
   File: dfbf.py
   URL: https:
   Code Content:
import sys
def read(fnm,db):
  file = open(fnm)
  graph = {}
  for line in file:
    l = line.strip().split(" ")
    if db: print("l:",l,"len(l):",len(l))
    if l==['']:continue
    graph[l[0]]= ('white',l[1:])
  return graph
def dump(graph):
  print("dumping graph: nodeName (color, [adj list]) ")
  for node in graph:
    print(node, graph[node])
def bfs(graph,list):
  queue = []
  queue.append(root)
  graph[root] = ("black", graph[root][1], 0)
  if(len(graph[root][1]) == 0):
    return list
  while queue:
    node = queue.pop(0)
    for i in graph[node][1]:
      if graph[i][0] == "white":
        graph[i] = ('grey', graph[i][1], graph[node][2] + 1)
        list.append((i, graph[i][2]))
        queue.append(i)
    graph[node] = ("black", graph[node][1])
  return list
def white(graph) :
  for node in graph :
    gr[node] = ('white',gr[node][1])
def dfs(r):
   gr[r] = ("grey", gr[r][1])
   for v in gr[r][1]:
     if gr[v][0] == "white":
       dfs(v)
     if gr[v][0] == "grey":
       print("cycle in {}".format(v))
   gr[r] = ("black", gr[r][1])
if __name__ == "__main__":
  db = len(sys.argv)>3
  gr = read(sys.argv[1],db)
  root = sys.argv[2]
  if db: dump(gr)
  print("root key:", root)
  gr[root] = ('black',gr[root][1])
  q = bfs(gr,[(root,0)])
  print("BFS")
  print(q)
  if db: dump(gr)
  white(gr)
  if db: dump(gr)
  print("DFS");
  dfs(root)
  if db: dump(gr)
   README Content:
- depth first search dfs()
  - tells if there is a cycle in the graph
- breadth first search bfs()
  - tells how far away each "node" is from the root
```
(venv) C:\school\cs320\graphsPA2>dfbf.py [input graph you'd like to use] [root node you'd like to use] [debug mode (optional)
```
- Example output
```
(venv) C:\school\cs320\graphsPA2>dfbf.py in1.txt a
root key: a
BFS
[('a', 0), ('b', 1), ('c', 1), ('d', 1), ('e', 2), ('f', 2), ('g', 3)]
DFS
cycle in a
cycle in f
```
