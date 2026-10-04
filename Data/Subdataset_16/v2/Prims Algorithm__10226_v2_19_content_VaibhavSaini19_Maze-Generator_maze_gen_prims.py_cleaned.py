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
                b11 = (wall_x - 1, b10)
                b12 = (wall_x + 1, b10)
                if self.b4[b11] == 1 and self.b4[b12] == -1:
                    self.b4[wall_x, b10] = 1
                    self.b4[b12] = 1
                    self.fonk3(b12)
                elif self.b4[b11] == -1 and self.b4[b12] == 1:
                    self.b4[wall_x, b10] = 1
                    self.b4[b11] = 1
                    self.fonk3(b11)
                self.b3.remove((wall_x, b10))
            if self.fonk2((wall_x, b10), 0, 1) and self.fonk2((wall_x, b10), 0, -1):
                b13 = (wall_x, b10 - 1)
                b14 = (wall_x, b10 + 1)
                if self.b4[b13] == 1 and self.b4[b14] == -1:
                    self.b4[wall_x, b10] = 1
                    self.b4[b14] = 1
                    self.fonk3(b14)
                elif self.b4[b13] == -1 and self.b4[b14] == 1:
                    self.b4[wall_x, b10] = 1
                    self.b4[b13] = 1
                    self.fonk3(b13)
                self.b3.remove((wall_x, b10))
            if self.b2:
                plt.figure(1)
                plt.clf()
                plt.imshow(self.b4, b15 = 'gray')
                plt.title('Maze')
                plt.pause(0.005)
        plt.pause(5)
        for row in range(self.b1):
            for col in range(self.b1):
                if self.b4[row, col] == 1:
                    self.b5[row, col] = True
        return self.b5
if b16 = = "__main__":
    b1 = int(input("Enter b1 of b5 (example: 10): "))
    b8 = (0, 0)
    b17 = class1(b1)
    b5 = b17.fonk4(b8).tolist()
    plt.figure(b18 = (10, 5))
    plt.imshow(b5, b19 = 'nearest', b15='gray')
    plt.xticks([]), plt.yticks([])
    plt.show()