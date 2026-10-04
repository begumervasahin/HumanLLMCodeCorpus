class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
class class2:
    def fonk4(self, b3):
        self.b3 = b3
        self.b4 = []
    def fonk5(self):
        return self.b4
    def fonk6(self):
        return len(self.b4)
    def fonk7(self):
        return self.b3
    def fonk8(self, enlazar, b2):
        if not self.b4:
            self.b4.append(class1(enlazar, b2))
        else:
            b5 = self.fonk9(enlazar)
            if b5 = = -1:
                self.b4.append(class1(enlazar, b2))
    def fonk9(self, enlazar):
        for i, enlace in enumerate(self.b4):
            if enlace.fonk2() == enlazar:
                return i
        return -1
    def fonk10(self, b5):
        if 0 <= b5 < len(self.b4):
            return self.b4[b5].fonk3()
        return None
    def fonk11(self, b5):
        if 0 <= b5 < len(self.b4):
            return self.b4[b5].fonk2()
        return None
    def fonk12(self, b5):
        if 0 <= b5 < len(self.b4):
            del self.b4[b5]
            return True
        return False