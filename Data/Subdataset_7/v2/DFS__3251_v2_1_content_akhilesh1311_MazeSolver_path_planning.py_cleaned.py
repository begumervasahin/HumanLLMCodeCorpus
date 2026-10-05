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
            for b4 in maze_arr:
                b6 = []
                for b5 in b4:
                    if b5 = = ' ':
                        b6.append('O')
                    else:
                        b6.append(b5)
                self.b2.append(b6)
            self.b1 = len(maze_arr)
    def fonk2(self):
        for b4 in self.b2:
            print(*b4, b7 = ' ')
class class2(class1):
    def fonk3(self, maze_obj):
        super().fonk7(0, 0, maze_obj.b2)
        self.b8 = set()
        self.b9 = dict()
        self.b10 = False
    def fonk4(self, cur_i, b12):
        self.b8.add((cur_i, b12))
        b11 = [(cur_i, b12)]
        while b11:
            cur_i, b12 = b11.pop()
            for i in range(cur_i - 1, cur_i + 2):
                for b13 in range(b12 - 1, b12 + 2):
                    if 0 <= i < self.b1 and 0 <= b13 < self.b1 and abs(i - cur_i) + abs(b13 - b12) == 1 \
                            and self.b2[i][b13] != 'X' and (i, b13) not in self.b8:
                        self.b9[(i, b13)] = (cur_i, b12)
                        b11.append((i, b13))
                        self.b8.add((i, b13))
                        if self.b2[i][b13] == 'G':
                            self.b10 = True
                            return
    def fonk5(self, goal_i, goal_j):
        i, b13 = goal_i, goal_j
        while (i, b13) != (0, 0):
            self.b2[i][b13] = ' '
            i, b13 = self.b9[(i, b13)]
    def fonk6(self):
        self.fonk8(0, 0)
        if self.b10:
            print("Displaying solution with DFS -")
            self.fonk9(self.b1 - 1, self.b1 - 1)
            self.fonk2()
        else:
            print("class1 is not solvable.")
class class3(class1):
    def fonk7(self, maze_obj):
        super().fonk7(0, 0, maze_obj.b2)
        self.b8 = set()
        self.b9 = dict()
        self.b14 = []
        self.b10 = False
    def fonk8(self, cur_i, b12):
        self.b14.append((cur_i, b12))
        self.b8.add((cur_i, b12))
        while self.b14:
            cur_i, b12 = self.b14.pop(0)
            for i in range(cur_i - 1, cur_i + 2):
                for b13 in range(b12 - 1, b12 + 2):
                    if 0 <= i < self.b1 and 0 <= b13 < self.b1 and abs(i - cur_i) + abs(b13 - b12) == 1 \
                            and self.b2[i][b13] != 'X' and (i, b13) not in self.b8:
                        self.b9[(i, b13)] = (cur_i, b12)
                        self.b8.add((i, b13))
                        self.b14.append((i, b13))
                        if self.b2[i][b13] == 'G':
                            self.b10 = True
                            return
    def fonk9(self, goal_i, goal_j):
        i, b13 = goal_i, goal_j
        while (i, b13) != (0, 0):
            self.b2[i][b13] = ' '
            i, b13 = self.b9[(i, b13)]
    def fonk10(self):
        self.fonk8(0, 0)
        if self.b10:
            print("Displaying solution with BFS -")
            self.fonk9(self.b1 - 1, self.b1 - 1)
            self.fonk2()
        else:
            print("class1 is not solvable.")
if b15 = = '__main__':
    b16 = class1(10, 0.2)
    b16.fonk2()
    b17 = class3(b16)
    b17.fonk10()
