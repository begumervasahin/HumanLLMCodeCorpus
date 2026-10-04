class class1:
    def fonk1(self,b1,b3,b2):
        self.b1 = b1
        self.fonk3(self.b1)
        self.b2 = b3.index(b2)
        self.b3 = b3
    def fonk2(self,step):
        for i in range(len(self.b1)):
            for j in range(len(self.b1)):
                if(self.b1[i][step] != -1 and self.b1[step][j] != -1):
                    if(self.b1[i][j] == -1):
                        self.b1[i][j] = self.b1[step][j]+self.b1[i][step]
                    else:
                        self.b1[i][j] = min(self.b1[i][j],
                            self.b1[step][j]+self.b1[i][step])
    def fonk3(self,b1):
        for i in range(len(b1)):
            b1[i][i] = 0
    def fonk4(self):
        for step in range(len(self.b1)):
            self.fonk2(step)
    def fonk5(self):
        self.fonk4()
        for n in range(len(self.b3)):
            print("   \u279c {0}: {1}".format(self.b3[n], (self.b1[self.b2][n])).replace("-1",u'inf' ))