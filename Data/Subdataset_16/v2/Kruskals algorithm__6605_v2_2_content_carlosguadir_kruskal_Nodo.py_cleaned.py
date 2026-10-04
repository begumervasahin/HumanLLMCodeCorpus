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
    def fonk5(self, b1, b2):
        if not self.fonk6(b1):
            self.b4.append(class1(b1, b2))
    def fonk6(self, b1):
        return any(enlace.fonk2() == b1 for enlace in self.b4)
    def fonk7(self):
        return self.b4
    def fonk8(self):
        return len(self.b4)
    def fonk9(self):
        return self.b3
    def fonk10(self, posicion):
        if 0 <= posicion < len(self.b4):
            return self.b4[posicion].fonk3()
        return None
    def fonk11(self, posicion):
        if 0 <= posicion < len(self.b4):
            return self.b4[posicion].fonk2()
        return None
    def fonk12(self, posicion):
        if 0 <= posicion < len(self.b4):
            del self.b4[posicion]
            return True
        return False