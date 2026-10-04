class FeatureHeader:
    def get_header(self, feature_type):
        if feature_type == FeatureType.HUMIDITY:
            return "Humidity: "
class FeatureType:
    HUMIDITY = "humidity"
class SatisfactionHumidity:
    def __init__(self, target_val):
        self.__target_val = target_val
    def __extract_humidity(self, data):
        humidity_header = FeatureHeader().get_header(FeatureType.HUMIDITY)
        value = data.get_value().split('\n')
        for line in value:
            if line.startswith(humidity_header):
                return float(line.replace(humidity_header, ""))
        return 0
    def get_feature_type(self):
        return FeatureType.HUMIDITY
    def get_satisfaction(self, data):
        humidity = self.__extract_humidity(data)
        if humidity == 0:
            return 0
        diff = abs(self.__target_val - humidity)
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
class Data:
    def __init__(self, value):
        self.__value = value
    def get_value(self):
        return self.__value
target_val = 50
data = Data("Temperature: 23\nHumidity: 48\nPressure: 1013")
satisfaction_humidity = SatisfactionHumidity(target_val)
satisfaction = satisfaction_humidity.get_satisfaction(data)
print("Satisfaction:", satisfaction)