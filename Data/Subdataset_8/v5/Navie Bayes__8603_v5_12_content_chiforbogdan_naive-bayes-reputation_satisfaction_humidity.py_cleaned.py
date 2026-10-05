from feature_header import feature_header
from feature_type import feature_type
class SatisfactionHumidity:
    def __init__(self, target_val):
        self.target_val = target_val
    def extract_humidity(self, data):
        humidity_header = feature_header().get_header(feature_type.HUMIDITY)
        lines = data.get_value().split('\n')
        for line in lines:
            if line.startswith(humidity_header):
                return float(line.replace(humidity_header, ""))
        return 0
    def get_feature_type(self):
        return feature_type.HUMIDITY
    def get_satisfaction(self, data):
        humidity = self.extract_humidity(data)
        if humidity == 0:
            return 0
        diff = abs(self.target_val - humidity)
        satisfaction = {
            0: 1, 2: 0.9, 5: 0.8, 7: 0.7, 9: 0.6, 10: 0.5, 12: 0.4, 15: 0.3, 17: 0.2, 20: 0.1
        }
        for threshold, value in satisfaction.items():
            if diff < threshold:
                return value
        return 0