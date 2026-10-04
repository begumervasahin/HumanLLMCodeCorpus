class class1:
    def fonk1(self, b1):
        if b1 = = class2.b2:
            return "Humidity: "
class class2:
    b2 = "b6"
class class3:
    def fonk2(self, a1):
        self.b3 = a1
    def fonk3(self, b9):
        b4 = class1().fonk1(class2.b2)
        b5 = b9.fonk7().split('\n')
        for line in b5:
            if line.startswith(b4):
                return float(line.replace(b4, ""))
        return 0
    def fonk4(self):
        return class2.b2
    def fonk5(self, b9):
        b6 = self.fonk3(b9)
        if b6 = = 0:
            return 0
        b7 = abs(self.b3 - b6)
        if b7 = = 0:
            return 1
        elif b7 < 2:
            return 0.9
        elif b7 < 5:
            return 0.8
        elif b7 < 7:
            return 0.7
        elif b7 < 9:
            return 0.6
        elif b7 < 10:
            return 0.5
        elif b7 < 12:
            return 0.4
        elif b7 < 15:
            return 0.3
        elif b7 < 17:
            return 0.2
        elif b7 < 20:
            return 0.1
        return 0
class class4:
    def fonk6(self, b5):
        self.b8 = b5
    def fonk7(self):
        return self.b8
a1 = 50
b9 = class4("Temperature: 23\nHumidity: 48\nPressure: 1013")
b10 = class3(a1)
b11 = b10.fonk5(b9)
print("Satisfaction:", b11)