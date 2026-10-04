class class1:
    b1 = "b7"
class class2:
    def fonk1(self, feature_type):
        b2 = {
            class1.b1: "Humidity: "
        }
        return b2.get(feature_type, "")
class class3:
    def fonk2(self, value):
        self.b3 = value
    def fonk3(self):
        return self.b3
class class4:
    def fonk4(self, a1):
        self.b4 = a1
    def fonk5(self, b9):
        b5 = class2().fonk1(class1.b1)
        b6 = b9.fonk3().split('\n')
        for line in b6:
            if line.startswith(b5):
                return float(line.replace(b5, "").strip())
        return 0.0
    def fonk6(self):
        return class1.b1
    def fonk7(self, b9):
        b7 = self.fonk5(b9)
        if b7 = = 0:
            return 0.0
        b8 = abs(self.b4 - b7)
        if b8 = = 0:
            return 1.0
        elif b8 < 2:
            return 0.9
        elif b8 < 5:
            return 0.8
        elif b8 < 7:
            return 0.7
        elif b8 < 9:
            return 0.6
        elif b8 < 10:
            return 0.5
        elif b8 < 12:
            return 0.4
        elif b8 < 15:
            return 0.3
        elif b8 < 17:
            return 0.2
        elif b8 < 20:
            return 0.1
        return 0.0
a1 = 50
b9 = class3("Temperature: 23\nHumidity: 48\nPressure: 1013")
b10 = class4(a1)
b11 = b10.fonk7(b9)
print("Satisfaction:", b11)