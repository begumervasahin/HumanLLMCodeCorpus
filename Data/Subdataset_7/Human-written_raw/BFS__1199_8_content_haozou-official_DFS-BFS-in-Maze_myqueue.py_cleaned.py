8. Repository: haozou-official/DFS-BFS-in-Maze
   File: myqueue.py
   URL: https:
   Code Content:
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, item):
        self.b1.insert(0,item)
    def fonk3(self):
        return self.b1.pop()
    def fonk4(self):
        return self.b1 = = []
    def fonk5(self):
        return len(self.b1)
def fonk6():
    b2 = class1()
    b2.fonk2(1)
    b2.fonk2(2)
    b2.fonk2(3)
    b2.fonk2(4)
    b2.fonk2(5)
    print(b2.fonk5())
    while not b2.fonk4():
        print(b2.fonk3())
    print(b2.fonk5())
if b3 = = '__main__':
    fonk6()
   README Content:
Depth-First-Search &amp; Breadth-First-Search in finding the optimal path of labyrinth.
There two ways in implementing BFS algorithms: class1 & OPEN-CLOSED table.
```
Input:
  A graph G and a vertex b5 of G
  b8 is a DICT, initialized with {}
Output:
  return: GOAL or None
  b8 is changed
def fonk7(G, V, b8):
  b4 = class1()
  b4.fonk2(b5)
  b8[b5] = None
  while not b4.fonk4():
    b5 = b4.fonk3()
    if b5 is not labeled as discovered:
      if b5 is a goal:
        return b5
      else:
        label b5 as discovered
        for all edges from b5 to w in G.adjacentEdges(b5):
          if w is not labeled as discovered:
            b4.fonk2(w)
            b8[w] = b5
  return None
```
```
Input:
  A graph G and a vertex b5 of G
  b8 is a DICT, initialized with {}
Output:
  return: GOAL or None
  b8 is changed
def fonk8(G, V, b8):
  b6 = [b5]
  b7 = []
  b8[b5] = None
  while b6 is not empty:
    remove an element from the front of b6, call it b5
    if b5 is a goal:
      return b5
    else:
      put b5 on b7
      for all edges from b5 to w in G.adjacentEdges(b5):
        if w is not in b7:
          put w at the back of b6
          b8[w] = b5
  return None
```
There two ways in implementing DFS algorithms: Recursive & Non-recursive.
```
Input:
  A graph G and a vertex b5 of G
  b8 is a DICT, initialized with {}
Output:
  return: GOAL or None
  b8 is changed
def fonk9(G, V, b8):
  if b8 = = {}:
    b8[b5] = None
  if b5 is a goal:
    return b5
  label b5 as discovered
  for all edges from b5 to w in G.adjacentEdges(b5):
    if vertex w is not labeled as discovered:
      b8[w] = b5
      b9 = fonk10(G, W, b8)
      if b9 is a goal:
        return b9
  return None
```
```
Input:
  A graph G and a vertex b5 of G
  b8 is a DICT, initialized with {}
Output:
  return: GOAL or None
  b8 is changed
def fonk10(G, V, b8):
  b4 = Stack()
  b4.push(b5)
  b8[b5] = None
  while not b4.fonk4():
    b5 = b4.pop()
    if b5 is not labeled as discovered:
      if b5 is a goal:
        return b5
      else:
        label b5 as discovered
        for all edges from b5 to w in G.adjacentEdges(b5):
          b4.push(w)
          b8[w] = b5
  return None
```
