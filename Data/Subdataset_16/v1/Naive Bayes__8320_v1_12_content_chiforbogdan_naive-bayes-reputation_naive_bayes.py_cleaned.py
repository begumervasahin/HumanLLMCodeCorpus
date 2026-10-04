from b7 import *
class class1:
    def fonk1(self, sensor_name, b13, a5):
        self.b1 = []
        self.b2 = sensor_name
        self.b3 = b13
        self.b4 = {}
        self.b5 = a5
        self.a1 = 0
        self.a2 = 0
        self.b6 = {}
        self.a3 = 0
    def fonk2(self, satisfaction):
        self.b1.append(satisfaction)
        self.b4[satisfaction.get_feature_type()] = 0
        self.b6[satisfaction.get_feature_type()] = []
    def fonk3(self, b17):
        self.a1 += 1
        a4 = 0
        for satisfaction in self.b1:
            b7 = satisfaction.get_feature_type()
            a4 += self.b3[b7] * satisfaction.get_satisfaction(b17)
        if a4 >= self.b5:
            self.a2 += 1
            for satisfaction in self.b1:
                b7 = satisfaction.get_feature_type()
                if satisfaction.get_satisfaction(b17) >= self.b3[b7] * self.b5:
                    self.b4[b7] += 1
    def fonk4(self, feature):
        if self.a1 = = 0 or self.a2 == 0:
            return (0, 0)
        b8 = self.a2 / self.a1
        b9 = self.b4[feature] / self.a1
        return (b9 / b8, b8)
    def fonk5(self):
        for feature in self.b4.keys():
            self.b6[feature].append(self.fonk4(feature))
        self.a3 += 1
    def fonk6(self, b18):
        b10 = []
        for i in range(self.a3):
            b11 = self.b6[b18[0]][i][1]
            for feature in b18:
                b11 *= self.b6[feature][i][0]
            b10.append(b11)
        return b10
if b12 = = "__main__":
    b13 = {'feature1': 0.3, 'feature2': 0.7}
    a5 = 0.5
    b14 = class1(sensor_name="Sensor1", b13=b13, a5=a5)
    b15 = FeatureSatisfaction('feature1')
    b16 = FeatureSatisfaction('feature2')
    b14.fonk2(b15)
    b14.fonk2(b16)
    b17 = {}
    b14.fonk3(b17)
    b14.fonk5()
    b18 = ['feature1', 'feature2']
    b10 = b14.fonk6(b18)
    print(b10)