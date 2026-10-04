import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, b1 = 25, b2=True):
        self.b1 = (b1
        self.b2 = b2
        self.b3 = []
        self.b4 = np.full((self.b1, self.b1), -50, dtype=int)
        self.b5 = np.zeros((self.b1, self.b1), dtype=bool)
        for i in range(b1
            for j in range(b1
                self.b4[i * 2, j * 2] = -1
    def fonk2(self, curr, dx, dy):
        x, b6 = curr
        return 0 <= x + dx < self.b1 and 0 <= b6 + dy < self.b1
    def fonk3(self, curr):
        b7 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dx, dy in b7:
            if self.fonk2(curr, dx, dy):
                self.b3.append((curr[0] + dx, curr[1] + dy))
    def fonk4(self, b8):
        b8 = ((b8[0]
        self.b4[b8[0], b8[1]] = 1
        self.fonk3(b8)
        while self.b3:
            b9 = np.random.randint(0, len(self.b3))
            wall_x, b10 = self.b3[b9]
            if self.fonk2((wall_x, b10), -1, 0) and self.fonk2((wall_x, b10), 1, 0):
                self.fonk5((wall_x, b10), (-1, 0), (1, 0))
            if self.fonk2((wall_x, b10), 0, 1) and self.fonk2((wall_x, b10), 0, -1):
                self.fonk5((wall_x, b10), (0, -1), (0, 1))
            self.b3.remove((wall_x, b10))
            if self.b2:
                self.fonk6()
        plt.pause(5)
        self.fonk7()
        return self.b5
    def fonk5(self, wall, dir1, dir2):
        b11 = (wall[0] + dir1[0], wall[1] + dir1[1])
        b12 = (wall[0] + dir2[0], wall[1] + dir2[1])
        if self.b4[b11] == 1 and self.b4[b12] == -1:
            self.b4[wall] = 1
            self.b4[b12] = 1
            self.fonk3(b12)
        elif self.b4[b11] == -1 and self.b4[b12] == 1:
            self.b4[wall] = 1
            self.b4[b11] = 1
            self.fonk3(b11)
    def fonk6(self):
        plt.figure(1)
        plt.clf()
        plt.imshow(self.b4, b13 = 'gray')
        plt.title('Maze')
        plt.pause(0.005)
    def fonk7(self):
        for row in range(self.b1):
            for col in range(self.b1):
                if self.b4[row, col] == 1:
                    self.b5[row, col] = True
if b14 = = "__main__":
    b1 = int(input("Enter b1 of b5 (example: 10): "))
    b8 = (0, 0)
    b15 = class1(b1)
    b5 = b15.fonk4(b8).tolist()
    plt.figure(b16 = (10, 5))
    plt.imshow(b5, b17 = 'nearest', b13='gray')
    plt.xticks([]), plt.yticks([])
    plt.show()