import queue
class class1:
    def fonk1(self, b2, b3, b1 = 10000):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = queue.Queue()
        self.b5 = []
        self.a1 = 0
        self.a2 = 0
        self.b6 = []
        self.b7 = []
        self.b8 = []
    def fonk2(self):
        self.b9 = int(self.b2 * self.b1)
        self.b10 = [1 / self.b2] * self.b9
        self.b11 = [1 / self.b3] * self.b9
        self.b12 = [sum(self.b10[:i + 1]) for i in range(self.b9)]
    def fonk3(self):
        self.b7.clear()
        self.b6.clear()
        self.b8.clear()
        self.b5.clear()
        self.a2 = 0
        self.a1 = 0
        while not self.b4.empty():
            self.b4.get()
    def fonk4(self):
        self.fonk3()
        for i in range(len(self.b12)):
            while self.a1 > 0 and self.b7[self.a1] < self.b12[i] and not self.b4.empty():
                self.a1 = self.b4.get()
            if self.a2 > self.b12[i]:
                self.b8.append(self.a2 - self.b12[i])
                self.a2 += self.b11[i]
                self.b5.append(self.b4.qsize() + 1)
                self.b7.append(self.a2)
                self.b6.append(self.a2 - self.b12[i])
                self.b4.put(i)
            else:
                self.b5.append(self.b4.qsize())
                self.b6.append(self.b11[i])
                self.a1 = i
                self.a2 = self.b12[self.a1] + self.b11[self.a1]
                self.b7.append(self.a2)
                self.b8.append(0)
        while not self.b4.empty():
            self.a1 = self.b4.get()
    def fonk5(self):
        a3 = 0
        a4 = 0
        a5 = 0
        self.a6 = 0
        a7 = 0
        while a3 < len(self.b7):
            if a4 < len(self.b12) and self.b12[a4] < self.b7[a3]:
                self.a6 += a5 * (self.b12[a4] - a7)
                a5 += 1
                a7 = self.b12[a4]
                a4 += 1
            else:
                self.a6 += a5 * (self.b7[a3] - a7)
                a5 -= 1
                a7 = self.b7[a3]
                a3 += 1
        return self.a6 / self.b7[-1]