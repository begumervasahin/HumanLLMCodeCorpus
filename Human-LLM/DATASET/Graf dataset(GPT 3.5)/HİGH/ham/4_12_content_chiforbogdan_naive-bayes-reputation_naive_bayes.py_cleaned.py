from feature_type import *
class class1:
    def fonk1(self, sensor_name, feature_weights, satisfaction_threshold):
        self.b1 = []
        self.b2 = sensor_name
        self.b3 = feature_weights
        self.b4 = {}
        self.b5 = satisfaction_threshold
        self.a1 = 0
        self.a2 = 0
        self.b6 = {}
        self.a3 = 0
    def fonk2(self, satisfaction):
        self.b1.append(satisfaction)
        self.b4[satisfaction.get_feature_type()] = 0
        self.b6[satisfaction.get_feature_type()] = []
    def fonk3(self, data):
        self.a1 = self.a1 + 1
        a4 = 0
        for satisfaction in self.b1:
            a4 = a4 + self.b3[satisfaction.get_feature_type()] * satisfaction.get_satisfaction(data)
        if a4 >= self.b5:
            self.a2 = self.a2 + 1
            for satisfaction in self.b1:
                if satisfaction.get_satisfaction(data) >= self.b3[satisfaction.get_feature_type()] * self.b5:
                    self.b4[satisfaction.get_feature_type()] = self.b4[satisfaction.get_feature_type()] + 1
    def fonk4(self, feature):
        if self.a1 = = 0 or self.a2 == 0:
            return (0,0)
        b7 = self.a2 / self.a1
        b8 = self.b4[feature] / self.a1
        return (b8 / b7, b7)
    def fonk5(self):
        for feature in self.b4.keys():
            self.b6[feature].append(self.fonk4(feature))
        self.a3 = self.a3 + 1
    def fonk6(self, features):
        b9 = []
        for i in range(self.a3):
            b10 = self.b6[features[0]][i][1]
            for feature in features:
                b10 = b10 * self.b6[feature][i][0]
            b9.append(b10)
        return b9