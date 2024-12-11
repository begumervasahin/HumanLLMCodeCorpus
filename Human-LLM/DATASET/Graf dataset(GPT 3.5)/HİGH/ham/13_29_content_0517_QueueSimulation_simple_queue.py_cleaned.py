import queue
class class1:
    '''
    Simulating the single server queue
        The number of server is 1.
        The number of b5 is ignored, which is infinity.
        Take the service speed as 1 so that the distribution of service time equals to the distribution of
            packet length.
    Initializing the simulation program with at least b2(Î») and b3(Î¼).
        b2(Î») is the average arrival rate in unit time.
        b3(Î¼) is the average service time.
    '''
    def fonk1(self, b2, b3, b1 = 10000):
        self.b2 = b2
        self.b3 = b3
        self.b4 = float(self.b2)/self.b3
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
        Set up the simulation object.
        b10 is the total number of points calculated or generated with regarding distribution using the
            average arriving rate and the total simulating time.
        b11 is the calculated or generated with regarding distribution using the average arriving
            rate and the total number of points.
        b12 is the calculated or generated with regarding distribution using the average serving
            rate and the total number of points.
        b13 is the actual arriving time of each point.
        '''
        self.b10 = self.b2*self.b1
        self.b11 = [1/self.b2 for i in range(self.b10)]
        self.b12 = [1/self.b3 for i in range(self.b10)]
        self.b13 = []
        for i in range(self.b10):
            self.b13.append(sum(self.b11[:i+1]))
    def fonk3(self):
        '''
        Reset those parameters that change with each time of simulation.
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
        a2 is the time when the server can finish all the work in the system.
        If an point arrives at the time after next_free t, it means that it won't see any remaining b9,
            only itself.
        If it arrives before the a2, it means it would see some remaining b9, which is
            a2 - b13.
        The unfinished work is the remaining work plus what it brings.
        '''
        self.fonk3()
        for i in range(len(self.b13)):
            while self.a1 > 0 and self.b8[self.a1] < self.b13[i] and \
                not self.b5.empty():
                self.a1 = self.b5.get()
            if self.a2 > self.b13[i]:
                self.b9.append(self.a2 - self.b13[i])
                self.a2 += self.b12[i]
                self.b6.append(self.b5.qsize()+1)
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
        Take the arrival and departure as event on the time series. When an new point arrives, the state of the system
        a5 transists to a5+1 , which last until the next event. When point departs, the state change to a5-1 and last until
        the next event. By intergral the a5 over each time interval, the result is the integral of a5 over the whole time.
        Divide it by the time, the result is then the time average number in the system.
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
        return self.a6/self.b8[-1]