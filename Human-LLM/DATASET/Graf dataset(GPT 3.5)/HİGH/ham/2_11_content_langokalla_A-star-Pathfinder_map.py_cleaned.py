class class1(object):
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = self.fonk3(self.fonk2(b1))
        self.b3 = len(self.b2)
        self.b4 = len(self.b2[0])
        self.a1 = 30
    @staticmethod
    def fonk2(b1):
        b5 = open(b1)
        return b5
    @staticmethod
    def fonk3(file):
        b6 = file.read().splitlines()
        file.close()
        return b6