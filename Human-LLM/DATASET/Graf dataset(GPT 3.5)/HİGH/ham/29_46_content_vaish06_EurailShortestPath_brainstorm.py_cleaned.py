from graph import Graph
from shortest_paths import *
from linked_stack import LinkedStack
b1 = Graph()
b2 = open('b2.txt','r')
b3 = dict()
b4 = set()
for line in b2.readlines():
    s, d, b5 = line.split(',')
    b6 = int(b5.split(':')[0])
    b7 = int(b5.split(':')[1])
    b4.add((s,d,b6*60+b7))
    b3.setdefault(s)
    b3.setdefault(d)
for city in b3:
    b3[city] = b1.insert_vertex(city)
for b10 in b4:
    s,d,b8 = b10
    b1.insert_edge(b3[s],b3[d],b8)
a1 = 0
b9 = False
for source in b3:
    for destination in b3:
        if source is destination:
            b9 = True
        if b9 and source is not destination :
            b10 = b1.get_edge(b3[source],b3[destination])
    b9 = False
b11 = shortest_path_lengths(b1,b3['London'])
b12 = shortest_path_tree(b1,b3['London'],b11)
print(b12)