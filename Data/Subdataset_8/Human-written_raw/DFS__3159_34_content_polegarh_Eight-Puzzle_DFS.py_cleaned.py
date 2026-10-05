import sys
import os
import Queue as queue
from random import shuffle
class Puzzle:
    def __init__(self, arr):
        self.goal    = [1,2,3,8,0,4,7,6,5]
        self.state   = State(arr)
        self.initial = State(arr)
        self.isDone  = False
    def buildPathAction (self, end):
        path = []
        state = end
        while state.parent:
            path.append(state.action)
            state = state.parent
        path.pop()
        path = path[::-1]
        path.append("")
        return path
    def buildPath (self, end):
        path = []
        state = end
        while state.parent:
            path.append(state.arr)
            state = state.parent
        return path[::-1]
    def solve (self):
        self.solveDFS(self.state, [], 0)
    def solveDFS (self, state, visited, count):
        if self.isDone: return
        if (state.arr == self.goal):
            pathAction = self.buildPathAction(state)
            path = self.buildPath(state)
            print("The exact path and its move is:")
            for i in range(len(path)): print(str(path[i]) + '   ' + str(pathAction[i]))
            print("Depth = " + str(len(path)))
            print ("it took " + str(count) + " states")
            self.isDone = True
            return visited
        if state.arr not in visited:
            visited.append(state.arr)
            index_of_0 = state.arr.index(0)
            up   = state.moveUp(index_of_0)
            if (up is not None):
                self.solveDFS(up, visited, count + 1)
            left = state.moveLeft(index_of_0)
            if (left is not None):
                self.solveDFS(left, visited, count + 1)
            right= state.moveRight(index_of_0)
            if (right is not None):
                self.solveDFS(right, visited, count + 1)
            down = state.moveDown(index_of_0)
            if (down is not None ):
                self.solveDFS(down, visited, count + 1)
class State:
    def __init__(self, arr, parent=None, action=""):
        self.arr    = arr
        self.parent = parent
        self.goal   = [1,2,3,8,0,4,7,6,5]
        self.weight = 0
        self.action = action
        self.depth  = 0
    def swap (self, index_of_0, arr, i, action):
        if index_of_0 in arr:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 + i] = new_state[index_of_0 + i], new_state[index_of_0]
            return State(new_state, self, action)
        return None
    def moveUp (self, index_of_0):
        return self.swap(index_of_0, [3,4,5,6,7,8], -3, "U")
    def moveDown(self, index_of_0):
        return self.swap(index_of_0, [0,1,2,3,4,5], 3, "D")
    def moveRight(self, index_of_0):
        return self.swap(index_of_0, [0,1,3,4,6,7], 1, "R")
    def moveLeft(self, index_of_0):
        return self.swap(index_of_0, [1,2,4,5,7,8], -1, "L")
''' easy Puzzle - tested and it solves after looking at 557 states '''
''' medium Puzzle - tested and it solves after looking at 13 states '''
print("DFS Medium")
my_puzzle = Puzzle([2,8,1,0,4,3,7,6,5])
my_puzzle.solve()
''' hard Puzzle - tested and it does not solve it because it reaches max recursion '''