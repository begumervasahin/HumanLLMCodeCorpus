from b7 import FeatureType
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = []
        self.b5 = {}
        self.a1 = 0
        self.a2 = 0
        self.b6 = {}
        self.a3 = 0
    def fonk2(self, satisfaction):
        b7 = satisfaction.get_feature_type()
        self.b4.append(satisfaction)
        self.b5[b7] = 0
        self.b6[b7] = []
    def fonk3(self, data):
        self.a1 += 1
        b8 = sum(self.b2[s.get_feature_type()] * s.get_satisfaction(data) for s in self.b4)
        if b8 >= self.b3:
            self.a2 += 1
            for satisfaction in self.b4:
                b3 = self.b2[satisfaction.get_feature_type()] * self.b3
                if satisfaction.get_satisfaction(data) >= b3:
                    self.b5[satisfaction.get_feature_type()] += 1
    def fonk4(self, feature):
        if self.a1 = = 0 or self.a2 == 0:
            return (0, 0)
        b9 = self.a2 / self.a1
        b10 = self.b5[feature] / self.a1
        return (b10 / b9, b9)
    def fonk5(self):
        for feature in self.b5.keys():
            self.b6[feature].append(self.fonk4(feature))
        self.a3 += 1
    def fonk6(self, features):
        b6 = []
        for i in range(self.a3):
            a4 = 1
            for feature in features:
                feature_reputation, b9 = self.b6[feature][i]
                a4 *= feature_reputation * b9
            b6.append(a4)
        return b6