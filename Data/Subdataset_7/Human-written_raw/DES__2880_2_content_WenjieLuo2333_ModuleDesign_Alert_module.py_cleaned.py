import numpy
class class1():
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = b4 = [[] for i in range(3)]
        self.a1 = -1
    def fonk2(self, data, b5):
        if b5 = = 0:
            if not 0.1 <= data <= 0.3:
                return 0
            else:
                return -1
        elif b5 = = 1:
            if not 80 <= data <= 120:
                return 1
            else:
                return -1
        else:
            if not 60 <= data <= 90:
                return 2
            else:
                return -1
    def fonk3(self):
        if self.a1 != -1:
            return self.a1
        else:
            return -1
    def fonk4(self, data_in):
        if len(self.b4[data_in[1]]) < 20:
            self.b4[data_in[1]].append(float(data_in[0]))
        else:
            del (self.b4[data_in[1]][0])
            self.b4[data_in[1]].append(float(data_in[0]))
        if len(self.b4[0]) > 2 and self.fonk2(numpy.mean(self.b4[0]),'b1') != -1:
            self.a1 = self.fonk2(numpy.mean(self.b4[data_in[1]]),'b1')
        if len(self.b4[1]) > 2 and self.fonk2(numpy.mean(self.b4[1]),'b2') != -1:
            self.a1 = self.fonk2(numpy.mean(self.b4[data_in[1]]),'b2')
        if len(self.b4[2]) > 2 and self.fonk2(numpy.mean(self.b4[2]),'b3') != -1:
            self.a1 = self.fonk2(numpy.mean(self.b4[data_in[1]]),'b3')