class class1:
    def fonk1(self, b2, b1 = None, b3=0):
        self.b2 = b2
        if b1 is None:
            self.b1 = []
        else:
            self.b1 = b1
        self.b3 = b3
    def fonk2(self, companionship):
        self.b1.append(companionship)
        self.b3 += 1
    def fonk3(self):
        b4 = ''
        b4 += 'class1 Leader: ' + self.b2 + '\n'
        for comp in self.b1:
            b4 += comp.fonk11()
        return b4
class class2:
    def fonk4(self, b5, b6):
        self.b5 = b5
        self.b6 = b6
    def fonk5(self):
        return self.b5 + ' ' + self.b6 + '\n'
    def fonk6(self):
        return self.b5 + ' ' + self.b6
class class3:
    def fonk7(self, b5, b6):
        self.b5 = b5
        self.b6 = b6
        from lds_scraper import HometeachingScraper as hs
        b7 = hs.b7
        self.b8 = {b7[i][1]: 0 for i in range(1, 13)}
    def fonk8(self):
        return '\t' + self.b5 + ' ' + self.b6 + '\n'
    def fonk9(self):
        return self.b5 + ' ' + self.b6
class class4:
    def fonk10(self, b9 = None, b10=None):
        if b9 is None:
            self.b9 = []
        else:
            self.b9 = b9
        if b10 is None:
            self.b10 = []
        else:
            self.b10 = b10
    def fonk11(self):
        b4 = ''
        for comp in self.b9:
            b4 += comp.fonk11()
        for hometeachee in self.b10:
            b4 += hometeachee.fonk11()
        return b4