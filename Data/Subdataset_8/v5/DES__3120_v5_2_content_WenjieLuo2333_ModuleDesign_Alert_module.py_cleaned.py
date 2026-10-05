import numpy as np
class AlertSystem:
    def __init__(self):
        self.blood_oxygen_readings = []
        self.blood_pressure_readings = []
        self.pulse_rate_readings = []
        self.average_values = [[] for _ in range(3)]
        self.alert_flag = -1
    def check_threshold_exceedance(self, value, type_index):
        if type_index == 0:
            return 0 if not 0.1 <= value <= 0.3 else -1
        elif type_index == 1:
            return 1 if not 80 <= value <= 120 else -1
        else:
            return 2 if not 60 <= value <= 90 else -1
    def get_alert_status(self):
        if self.alert_flag != -1:
            return self.alert_flag
        else:
            return -1
    def process_sensor_data(self, data):
        sensor_value, sensor_type_index = data
        if len(self.average_values[sensor_type_index]) < 20:
            self.average_values[sensor_type_index].append(float(sensor_value))
        else:
            del self.average_values[sensor_type_index][0]
            self.average_values[sensor_type_index].append(float(sensor_value))
        if len(self.average_values[0]) > 2 and self.check_threshold_exceedance(np.mean(self.average_values[0]), 0) != -1:
            self.alert_flag = self.check_threshold_exceedance(np.mean(self.average_values[sensor_type_index]), 0)
        if len(self.average_values[1]) > 2 and self.check_threshold_exceedance(np.mean(self.average_values[1]), 1) != -1:
            self.alert_flag = self.check_threshold_exceedance(np.mean(self.average_values[sensor_type_index]), 1)
        if len(self.average_values[2]) > 2 and self.check_threshold_exceedance(np.mean(self.average_values[2]), 2) != -1:
            self.alert_flag = self.check_threshold_exceedance(np.mean(self.average_values[sensor_type_index]), 2)
        return self.get_alert_status()
alert_system = AlertSystem()
sensor_data = [
    (0.15, 0),
    (110, 1),
    (70, 2)
]
for data in sensor_data:
    alert_flag = alert_system.process_sensor_data(data)
    if alert_flag != -1:
        print(f"Alert Flag: {alert_flag}")
    else:
        print("No alert")