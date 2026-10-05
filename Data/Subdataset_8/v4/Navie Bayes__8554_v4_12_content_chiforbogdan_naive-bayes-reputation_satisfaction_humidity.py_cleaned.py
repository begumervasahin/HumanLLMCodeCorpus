from feature_header import feature_header
from feature_type import feature_type
class SatisfactionHumidity:
    def __init__(self, target_val):
        self._target_val = target_val
    def _extract_humidity(self, data):
        humidity_header = feature_header().get_header(feature_type.HUMIDITY)
        value = data.get_value().split('\n')
        for line in value:
            if line.startswith(humidity_header):
                return float(line.replace(humidity_header, ""))
        return 0
    def get_feature_type(self):
        return feature_type.HUMIDITY
    def get_satisfaction(self, data):
        humidity = self._extract_humidity(data)
        if humidity == 0:
            return 0
        diff = abs(self._target_val - humidity)
        if diff == 0:
            return 1
        elif diff < 2:
            return 0.9
        elif diff < 5:
            return 0.8
        elif diff < 7:
            return 0.7
        elif diff < 9:
            return 0.6
        elif diff < 10:
            return 0.5
        elif diff < 12:
            return 0.4
        elif diff < 15:
            return 0.3
        elif diff < 17:
            return 0.2
        elif diff < 20:
            return 0.1
        return 0