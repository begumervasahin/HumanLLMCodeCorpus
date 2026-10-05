import queue
class class1:
    '''
    Simulates a single server queue system.
    The number of servers is 1, and the number of buffers is ignored (considered infinite).
    Service speed is assumed to be 1 to equalize the distribution of service time and packet length.
    '''
    def fonk1(self, b2, b3, b1 = 10000):
        '''
        Initializes the simulation with average arrival rate (b2) and average service time (b3).
        '''
        self.b2 = b2
        self.b3 = b3
        self.b4 = float(self.b2) / self.b3
        self.b1 = b1
        self.b5 = queue.Queue()
        self.b6 = []
        self.a1 = 0
        self.a2 = 0
        self.b7 = []
        self.b8 = []
        self.b9 = []
    def fonk2(self):
        '''
        Sets up the simulation object with necessary parameters.
        '''
        self.b10 = self.b2 * self.b1
        self.b11 = [1 / self.b2 for _ in range(self.b10)]
        self.b12 = [1 / self.b3 for _ in range(self.b10)]
        self.b13 = [sum(self.b11[:i + 1]) for i in range(self.b10)]
    def fonk3(self):
        '''
        Resets parameters that change with each simulation run.
        '''
        self.b8 = []
        self.b7 = []
        self.b9 = []
        self.b6 = []
        self.a2 = 0
        self.a1 = 0
        while not self.b5.empty():
            self.b5.get()
    def fonk4(self):
        '''
        Implements the FIFO (First In, First Out) strategy for serving customers.
        '''
        self.fonk3()
        for i in range(len(self.b13)):
            while self.a1 > 0 and self.b8[self.a1] < self.b13[i] and \
                not self.b5.empty():
                self.a1 = self.b5.get()
            if self.a2 > self.b13[i]:
                self.b9.append(self.a2 - self.b13[i])
                self.a2 += self.b12[i]
                self.b6.append(self.b5.qsize() + 1)
                self.b8.append(self.a2)
                self.b7.append(self.a2 - self.b13[i])
                self.b5.put(i)
            else:
                self.b6.append(self.b5.qsize())
                self.b7.append(self.b12[i])
                self.a1 = i
                self.a2 = self.b13[self.a1] + self.b12[self.a1]
                self.b8.append(self.a2)
                self.b9.append(0)
        while not self.b5.empty():
            self.a1 = self.b5.get()
    def fonk5(self):
        '''
        Calculates the time-average number in the system using the integral of a5 over time intervals.
        '''
        a3 = 0
        a4 = 0
        a5 = 0
        self.a6 = 0
        a7 = 0
        while a3 < self.b10:
            if a4 < self.b10 and self.b13[a4] < self.b8[a3]:
                self.a6 += (a5 * (self.b13[a4] - a7))
                a5 += 1
                a7 = self.b13[a4]
                a4 += 1
            else:
                self.a6 += (a5 * (self.b8[a3] - a7))
                a5 -= 1
                a7 = self.b8[a3]
                a3 += 1
        return self.a6 / self.b8[-1]