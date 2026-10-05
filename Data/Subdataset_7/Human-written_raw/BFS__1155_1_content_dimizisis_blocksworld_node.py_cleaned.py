1. Repository: dimizisis/blocksworld
   File: node.py
   URL: https:
   Code Content:
class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        return self.b3 < other.b3
   README Content:
![alt text](https:
The blocks world is one of the most famous planning domains in artificial intelligence. The algorithm is similar to b5 set of wooden blocks of various shapes and colors sitting on b5 table. The goal is to build one or more vertical stacks of blocks. Only one block may be moved at b5 time: it may either be placed on the table or placed atop another block. Because of this, any blocks that are, at b5 given time, under another block cannot be moved. Moreover, some kinds of blocks cannot have other blocks stacked on top of them.
The simplicity of this toy world lends itself readily to classical symbolic artificial intelligence approaches, in which the world is modeled as b5 set of abstract symbols which may be reasoned about.
It is b5 Blocks World puzzle game solver, with different kinds of algorithms. This project is created as an assignment of Artificial Inteligence university course.
* A* Search Algorithm (astar)
* Best First Search Algorithm (best)
* readth First Search Algorithm (breadth)
* Depth First Search Algorithm (depth)
```
python main.py <search_method> <input_file> <output_file>
```
```
[START]
b4 = 3,3
b5 = 0,2
b6 = 1,2
b7 = 2,2
[GOAL]
b5 = 1,1
b6 = 1,2
```
```
b5 ('0, 2')
b6 ('1, 2')
----------
Nodes expanded: 1
----------
b5 ('0, 2')
b6 ('1, 2')
----------
Nodes expanded: 2
  .
  .
  .
----------
b5 ('1, 1')
b6 ('1, 2')
----------
Nodes expanded: 242
----------
--- Execution time (seconds): 0.006296873092651367 ---
```
