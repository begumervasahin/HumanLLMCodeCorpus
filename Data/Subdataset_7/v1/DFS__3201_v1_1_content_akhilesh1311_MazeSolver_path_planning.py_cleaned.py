import random
class class1:
    def fonk1(self, b1 = 0, b3=0, maze_arr=[]):
        self.b2 = []
        if b1 != 0:
            self.b1 = b1
            self.b3 = b3
            for i in range(b1):
                b4 = []
                for b13 in range(b1):
                    b5 = 'X' if random.random() < b3 else 'O'
                    b4.append(b5)
                self.b2.append(b4)
            self.b2[0][0] = 'S'
            self.b2[b1 - 1][b1 - 1] = 'G'
        else:
            for i in range(len(maze_arr)):
                b4 = []
                for b13 in range(len(maze_arr[i])):
                    if maze_arr[i][b13] == ' ':
                        b4.append('O')
                    else:
                        b4.append(maze_arr[i][b13])
                self.b2.append(b4)
            self.b1 = len(maze_arr)
    def fonk2(self):
        for i in range(self.b1):
            print(*self.b2[i], b6 = ' ')
class class2(class1):
    b7 = []
    b8 = []
    def fonk3(self, MazeObject):
        super().fonk7(0, 0, MazeObject.b2)
        self.b9 = set()
        self.b10 = dict()
        self.b11 = False
    def fonk4(self, cur_i, b12):
        self.b9.add((cur_i, b12))
        self.b8.append((cur_i, b12))
        while self.b8:
            cur_i, b12 = self.b8.pop()
            for i in range(cur_i - 1, cur_i + 2):
                for b13 in range(b12 - 1, b12 + 2):
                    if 0 <= i < self.b1 and 0 <= b13 < self.b1 and abs(i - cur_i) + abs(b13 - b12) == 1 and self.b2[i][b13] != 'X' and (i, b13) not in self.b9:
                        self.b10[(i, b13)] = (cur_i, b12)
                        self.b8.append((i, b13))
                        self.b9.add((i, b13))
                        if self.b2[i][b13] == 'G':
                            self.b11 = True
                            return
    def fonk5(self, goal_i, goal_j):
        i, b13 = goal_i, goal_j
        while (i, b13) != (0, 0):
            self.b7.append((i, b13))
            i, b13 = self.b10[(i, b13)]
        self.b7.pop(0)
        for i, b13 in self.b7:
            self.b2[i][b13] = ' '
    def fonk6(self):
        self.fonk8(0, 0)
        if self.b11:
            print("Displaying solution with DFS -")
            self.fonk9(self.b1 - 1, self.b1 - 1)
            for i in range(self.b1):
                print(*self.b2[i], b6 = ' ')
        else:
            print("class1 is not solvable.")
class class3(class1):
    b7 = []
    def fonk7(self, MazeObject):
        super().fonk7(0, 0, MazeObject.b2)
        self.b9 = set()
        self.b10 = dict()
        self.b14 = []
        self.b11 = False
    def fonk8(self, cur_i, b12):
        self.b14.append((cur_i, b12))
        self.b9.add((cur_i, b12))
        while self.b14:
            cur_i, b12 = self.b14.pop(0)
            for i in range(cur_i - 1, cur_i + 2):
                for b13 in range(b12 - 1, b12 + 2):
                    if 0 <= i < self.b1 and 0 <= b13 < self.b1 and abs(i - cur_i) + abs(b13 - b12) == 1 and self.b2[i][b13] != 'X' and (i, b13) not in self.b9:
                        self.b10[(i, b13)] = (cur_i, b12)
                        self.b9.add((i, b13))
                        self.b14.append((i, b13))
                        if self.b2[i][b13] == 'G':
                            self.b11 = True
                            return
    def fonk9(self, goal_i, goal_j):
        i, b13 = goal_i, goal_j
        while (i, b13) != (0, 0):
            i, b13 = self.b10[(i, b13)]
            self.b7.append((i, b13))
        self.b7.pop()
        for i, b13 in self.b7:
            self.b2[i][b13] = ' '
    def fonk10(self):
        self.fonk8(0, 0)
        if self.b11:
            print("Displaying solution with BFS -")
            self.fonk9(self.b1 - 1, self.b1 - 1)
            for i in range(self.b1):
                print(*self.b2[i], b6 = ' ')
        else:
            print("class1 is not solvable.")
if b15 = = '__main__':
    b16 = class1(10, 0.2)
    b16.fonk2()
    b17 = class3(b16)
    b17.fonk10()
