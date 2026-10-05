from feature_header import feature_header
from feature_type import feature_type
class class1:
    def fonk1(self, target_val):
        self.b1 = target_val
    def fonk2(self, data):
        b2 = feature_header().get_header(feature_type.HUMIDITY)
        b3 = data.get_value().split('\n')
        for line in b3:
            if line.startswith(b2):
                return float(line.replace(b2, ""))
        return 0
    def fonk3(self):
        return feature_type.HUMIDITY
    def fonk4(self, data):
        b4 = self.fonk2(data)
        if b4 = = 0:
            return 0
        b5 = abs(self.b1 - b4)
        if b5 = = 0:
            return 1
        elif b5 < 2:
            return 0.9
        elif b5 < 5:
            return 0.8
        elif b5 < 7:
            return 0.7
        elif b5 < 9:
            return 0.6
        elif b5 < 10:
            return 0.5
        elif b5 < 12:
            return 0.4
        elif b5 < 15:
            return 0.3
        elif b5 < 17:
            return 0.2
        elif b5 < 20:
            return 0.1
        return 0