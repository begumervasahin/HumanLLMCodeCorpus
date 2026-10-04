from feature_header import *
from feature_type import *
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
            return 1.0
        return max(0, 1 - 0.1 * (b5
