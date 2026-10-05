import random
class class1:
    def fonk1(self, b1 = 0, b3=0, maze_arr=None):
        self.b2 = []
        self.b1 = b1
        self.b3 = b3
        if maze_arr is None:
            self.fonk2()
        else:
            self.b2 = [[b5 if b5 != ' ' else 'O' for b5 in b4] for b4 in maze_arr]
    def fonk2(self):
        for i in range(self.b1):
            b4 = []
            for b13 in range(self.b1):
                b5 = 'X' if random.random() < self.b3 else 'O'
                b4.append(b5)
            self.b2.append(b4)
        self.b2[0][0] = 'S'
        self.b2[self.b1 - 1][self.b1 - 1] = 'G'
    def fonk3(self):
        for b4 in self.b2:
            print(*b4, b6 = ' ')
class class2(class1):
    def fonk4(self, maze_obj):
        super().fonk10(maze_obj.b1, maze_obj.b3, maze_obj.b2)
        self.b7 = set()
        self.b8 = {}
        self.b9 = False
    def fonk5(self, start_i, start_j, move_offsets):
        self.b7.add((start_i, start_j))
        b10 = [(start_i, start_j)]
        while b10:
            cur_i, b11 = b10.pop(0)
            for i_offset, j_offset in move_offsets:
                new_i, b12 = cur_i + i_offset, b11 + j_offset
                if 0 <= new_i < self.b1 and 0 <= b12 < self.b1 and self.b2[new_i][b12] != 'X' and \
                        (new_i, b12) not in self.b7:
                    self.b8[(new_i, b12)] = (cur_i, b11)
                    b10.append((new_i, b12))
                    self.b7.add((new_i, b12))
                    if self.b2[new_i][b12] == 'G':
                        self.b9 = True
                        return
    def fonk6(self, goal_i, goal_j):
        i, b13 = goal_i, goal_j
        while (i, b13) != (0, 0):
            self.b2[i][b13] = ' '
            i, b13 = self.b8[(i, b13)]
    def fonk7(self, move_offsets):
        self.fonk5(0, 0, move_offsets)
        if self.b9:
            print(f"Displaying solution with {self.__class__.b14} -")
            self.fonk6(self.b1 - 1, self.b1 - 1)
            self.fonk3()
        else:
            print("class1 is not solvable.")
class class3(class2):
    def fonk8(self, maze_obj):
        super().fonk10(maze_obj)
    def fonk9(self):
        self.fonk7([(0, 1), (0, -1), (1, 0), (-1, 0)])
class class4(class2):
    def fonk10(self, maze_obj):
        super().fonk10(maze_obj)
    def fonk11(self):
        self.fonk7([(1, 0), (-1, 0), (0, 1), (0, -1)])
if b14 = = '__main__':
    b15 = class1(10, 0.2)
    b15.fonk3()
    b16 = class4(b15)
    b16.fonk11()