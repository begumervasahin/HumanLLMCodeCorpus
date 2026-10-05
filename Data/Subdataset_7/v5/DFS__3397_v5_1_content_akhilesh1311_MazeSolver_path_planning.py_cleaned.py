import random
class class1:
    def fonk1(self, b1 = 0, b2=0, maze_arr=[]):
        self.b1 = b1
        self.b2 = b2
        self.b3 = []
        if b1 != 0:
            self.fonk2()
        else:
            self.b3 = [['O' if b5 == ' ' else b5 for b5 in b4] for b4 in maze_arr]
            self.b1 = len(maze_arr)
    def fonk2(self):
        for i in range(self.b1):
            b4 = []
            for b12 in range(self.b1):
                b5 = 'X' if random.random() < self.b2 else 'O'
                b4.append(b5)
            self.b3.append(b4)
        self.b3[0][0] = 'S'
        self.b3[self.b1 - 1][self.b1 - 1] = 'G'
    def fonk3(self):
        for b4 in self.b3:
            print(*b4, b6 = ' ')
class class2(class1):
    def fonk4(self, maze_obj):
        super().fonk8(0, 0, maze_obj.b3)
        self.b7 = set()
        self.b8 = {}
        self.b9 = False
    def fonk5(self, cur_i, b11):
        self.b7.add((cur_i, b11))
        b10 = [(cur_i, b11)]
        while b10:
            cur_i, b11 = b10.pop()
            for i in range(cur_i - 1, cur_i + 2):
                for b12 in range(b11 - 1, b11 + 2):
                    if 0 <= i < self.b1 and 0 <= b12 < self.b1 and abs(i - cur_i) + abs(b12 - b11) == 1 \
                            and self.b3[i][b12] != 'X' and (i, b12) not in self.b7:
                        self.b8[(i, b12)] = (cur_i, b11)
                        b10.append((i, b12))
                        self.b7.add((i, b12))
                        if self.b3[i][b12] == 'G':
                            self.b9 = True
                            return
    def fonk6(self, goal_i, goal_j):
        i, b12 = goal_i, goal_j
        while (i, b12) != (0, 0):
            self.b3[i][b12] = ' '
            i, b12 = self.b8[(i, b12)]
    def fonk7(self):
        self.fonk9(0, 0)
        if self.b9:
            print("Displaying solution with DFS -")
            self.fonk10(self.b1 - 1, self.b1 - 1)
            self.fonk3()
        else:
            print("class1 is not solvable.")
class class3(class1):
    def fonk8(self, maze_obj):
        super().fonk8(0, 0, maze_obj.b3)
        self.b7 = set()
        self.b8 = {}
        self.b13 = []
        self.b9 = False
    def fonk9(self, cur_i, b11):
        self.b13.append((cur_i, b11))
        self.b7.add((cur_i, b11))
        while self.b13:
            cur_i, b11 = self.b13.pop(0)
            for i in range(cur_i - 1, cur_i + 2):
                for b12 in range(b11 - 1, b11 + 2):
                    if 0 <= i < self.b1 and 0 <= b12 < self.b1 and abs(i - cur_i) + abs(b12 - b11) == 1 \
                            and self.b3[i][b12] != 'X' and (i, b12) not in self.b7:
                        self.b8[(i, b12)] = (cur_i, b11)
                        self.b7.add((i, b12))
                        self.b13.append((i, b12))
                        if self.b3[i][b12] == 'G':
                            self.b9 = True
                            return
    def fonk10(self, goal_i, goal_j):
        i, b12 = goal_i, goal_j
        while (i, b12) != (0, 0):
            self.b3[i][b12] = ' '
            i, b12 = self.b8[(i, b12)]
    def fonk11(self):
        self.fonk9(0, 0)
        if self.b9:
            print("Displaying solution with BFS -")
            self.fonk10(self.b1 - 1, self.b1 - 1)
            self.fonk3()
        else:
            print("class1 is not solvable.")
if b14 = = '__main__':
    b15 = class1(4000, 0.1)
    b16 = class3(b15)
    print("class1 created successfully!")
    b16.fonk11()