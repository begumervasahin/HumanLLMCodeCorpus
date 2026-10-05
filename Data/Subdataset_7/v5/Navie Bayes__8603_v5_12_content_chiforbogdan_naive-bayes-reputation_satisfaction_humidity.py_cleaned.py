from feature_header import feature_header
from feature_type import feature_type
class class1:
    def fonk1(self, b1):
        self.b1 = b1
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
        b6 = {
            0: 1, 2: 0.9, 5: 0.8, 7: 0.7, 9: 0.6, 10: 0.5, 12: 0.4, 15: 0.3, 17: 0.2, 20: 0.1
        }
        for threshold, value in b6.items():
            if b5 < threshold:
                return value
        return 0