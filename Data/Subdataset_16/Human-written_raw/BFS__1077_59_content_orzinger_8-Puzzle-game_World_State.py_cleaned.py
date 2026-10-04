59. Repository: orzinger/8-Puzzle-game
   File: class1.py
   URL: https:
   Code Content:
class class1:
    def fonk1(self, _state, _operate, _parent, _depth, _f_value):
        self.b1 = _state
        self.b2 = _operate
        self.b3 = _parent
        self.b4 = _depth
        self.b5 = _f_value
    def fonk2(self, other):
        return self.b1 = = other.b1
    def fonk3(self, other):
        return self.b5 < other.b5
   README Content:
Solving 8-puzzle game with BFS, A*, IDS algorithms
The program reading file build-in as "intput.txt",
so you need your input file at the same directory with
the python files.
input file standart:
  num - Algorithm to be used:
  1 - IDS
  2 - BFS
  3 - A*
  num - size of board (b6 = root(b6,b6) )
  <0,1,2...,b6^2> - initial b1 as sequence of numbers.
  you can order them as you want.
  "0" means empty square
