from b7 import *
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
    def fonk3(self, data):
        self.a1 += 1
        b8 = self.fonk4(data)
        if b8 >= self.b5:
            self.a2 += 1
            self.fonk5(data)
    def fonk4(self, data):
        b8 = 0
        for satisfaction in self.b1:
            b7 = satisfaction.get_feature_type()
            b9 = satisfaction.get_satisfaction(data)
            b8 += self.b3[b7] * b9
        return b8
    def fonk5(self, data):
        for satisfaction in self.b1:
            b7 = satisfaction.get_feature_type()
            if satisfaction.get_satisfaction(data) >= self.b3[b7] * self.b5:
                self.b4[b7] += 1
    def fonk6(self, feature):
        if self.a1 = = 0 or self.a2 == 0:
            return (0, 0)
        b10 = self.a2 / self.a1
        b11 = self.b4[feature] / self.a1
        return (b11 / b10, b10)
    def fonk7(self):
        for feature in self.b4.keys():
            self.b6[feature].append(self.fonk6(feature))
        self.a3 += 1
    def fonk8(self, features):
        b6 = []
        for i in range(self.a3):
            b12 = self.b6[features[0]][i][1]
            for feature in features:
                b12 *= self.b6[feature][i][0]
            b6.append(b12)
        return b6