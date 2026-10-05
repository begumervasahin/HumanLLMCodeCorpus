11. Repository: davedennis/DFS-and-BFS-Search
   File: dfbf.py
   URL: https:
   Code Content:
import sys
def fonk1(fnm,b7):
  b1 = open(fnm)
  b2 = {}
  for line in b1:
    b3 = line.strip().split(" ")
    if b7: print("b3:",b3,"len(b3):",len(b3))
    if b3 = =['']:continue
    b2[b3[0]]= ('white',b3[1:])
  return b2
def fonk2(b2):
  print("dumping b2: nodeName (color, [adj list]) ")
  for b5 in b2:
    print(b5, b2[b5])
def fonk3(b2,list):
  b4 = []
  b4.append(b9)
  b2[b9] = ("black", b2[b9][1], 0)
  if(len(b2[b9][1]) == 0):
    return list
  while b4:
    b5 = b4.pop(0)
    for i in b2[b5][1]:
      if b2[i][0] == "white":
        b2[i] = ('grey', b2[i][1], b2[b5][2] + 1)
        list.append((i, b2[i][2]))
        b4.append(i)
    b2[b5] = ("black", b2[b5][1])
  return list
def fonk4(b2) :
  for b5 in b2 :
    b8[b5] = ('white',b8[b5][1])
def fonk5(r):
   b8[r] = ("grey", b8[r][1])
   for v in b8[r][1]:
     if b8[v][0] == "white":
       fonk5(v)
     if b8[v][0] == "grey":
       print("cycle in {}".format(v))
   b8[r] = ("black", b8[r][1])
if b6 = = "__main__":
  b7 = len(sys.argv)>3
  b8 = fonk1(sys.argv[1],b7)
  b9 = sys.argv[2]
  if b7: fonk2(b8)
  print("b9 key:", b9)
  b8[b9] = ('black',b8[b9][1])
  b10 = fonk3(b8,[(b9,0)])
  print("BFS")
  print(b10)
  if b7: fonk2(b8)
  fonk4(b8)
  if b7: fonk2(b8)
  print("DFS");
  fonk5(b9)
  if b7: fonk2(b8)
   README Content:
- depth first search fonk5()
  - tells if there is a cycle in the b2
- breadth first search fonk3()
  - tells how far away each "b5" is from the b9
```
(venv) C:\school\cs320\graphsPA2>dfbf.py [input b2 you'd like to use] [b9 b5 you'd like to use] [debug mode (optional)
```
- Example output
```
(venv) C:\school\cs320\graphsPA2>dfbf.py in1.txt a
b9 key: a
BFS
[('a', 0), ('b', 1), ('c', 1), ('d', 1), ('e', 2), ('f', 2), ('g', 3)]
DFS
cycle in a
cycle in f
```
