from b7 import FeatureSatisfaction
class class1:
    def fonk1(self, b2, b3, b5):
        self.b1 = []
        self.b2 = b2
        self.b3 = b3
        self.b4 = {}
        self.b5 = b5
        self.a1 = 0
        self.a2 = 0
        self.b6 = {}
        self.a3 = 0
    def fonk2(self, satisfaction):
        self.b1.append(satisfaction)
        b7 = satisfaction.get_feature_type()
        self.b4[b7] = 0
        self.b6[b7] = []
    def fonk3(self, b16):
        self.a1 += 1
        b8 = sum(
            self.b3[satisfaction.get_feature_type()] * satisfaction.get_satisfaction(b16)
            for satisfaction in self.b1
        )
        if b8 >= self.b5:
            self.a2 += 1
            for satisfaction in self.b1:
                b7 = satisfaction.get_feature_type()
                if satisfaction.get_satisfaction(b16) >= self.b3[b7] * self.b5:
                    self.b4[b7] += 1
    def fonk4(self, feature):
        if self.a1 = = 0 or self.a2 == 0:
            return (0, 0)
        b9 = self.a2 / self.a1
        b10 = self.b4[feature] / self.a1
        return (b10 / b9, b9)
    def fonk5(self):
        for feature in self.b4:
            self.b6[feature].append(self.fonk4(feature))
        self.a3 += 1
    def fonk6(self, b17):
        b6 = []
        for step in range(self.a3):
            b11 = self.b6[b17[0]][step][1]
            for feature in b17:
                b11 *= self.b6[feature][step][0]
            b6.append(b11)
        return b6
if b12 = = "__main__":
    b3 = {'feature1': 0.3, 'feature2': 0.7}
    b5 = 0.5
    b13 = class1(b2="Sensor1", b3=b3, b5=b5)
    b14 = FeatureSatisfaction('feature1')
    b15 = FeatureSatisfaction('feature2')
    b13.fonk2(b14)
    b13.fonk2(b15)
    b16 = {}
    b13.fonk3(b16)
    b13.fonk5()
    b17 = ['feature1', 'feature2']
    b6 = b13.fonk6(b17)
    print(b6)