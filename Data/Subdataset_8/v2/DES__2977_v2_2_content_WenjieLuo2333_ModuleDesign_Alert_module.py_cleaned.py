import numpy as np
class AlertSystem:
    def __init__(self):
        self.blood_oxygen = []
        self.blood_pressure = []
        self.pulse_rate = []
        self.average_values = [[] for _ in range(3)]
        self.alert_flag = -1
    def check_threshold_exceedance(self, value, category):
        if category == 'bo':
            if not 0.1 <= value <= 0.3:
                return 0
            else:
                return -1
        elif category == 'bp':
            if not 80 <= value <= 120:
                return 1
            else:
                return -1
        elif category == 'pul':
            if not 60 <= value <= 90:
                return 2
            else:
                return -1
    def get_alert_status(self):
        if self.alert_flag != -1:
            return self.alert_flag
        else:
            return -1
    def process_input_data(self, data):
        if len(self.average_values[data[1]]) < 20:
            self.average_values[data[1]].append(float(data[0]))
        else:
            del self.average_values[data[1]][0]
            self.average_values[data[1]].append(float(data[0]))
        if len(self.average_values[0]) > 2 and self.check_threshold_exceedance(np.mean(self.average_values[0]), 'bo') != -1:
            self.alert_flag = self.check_threshold_exceedance(np.mean(self.average_values[0]), 'bo')
        elif len(self.average_values[1]) > 2 and self.check_threshold_exceedance(np.mean(self.average_values[1]), 'bp') != -1:
            self.alert_flag = self.check_threshold_exceedance(np.mean(self.average_values[1]), 'bp')
        elif len(self.average_values[2]) > 2 and self.check_threshold_exceedance(np.mean(self.average_values[2]), 'pul') != -1:
            self.alert_flag = self.check_threshold_exceedance(np.mean(self.average_values[2]), 'pul')
        return self.alert_flag
alert_system = AlertSystem()
data_input = [
    (0.15, 0),
    (110, 1),
    (70, 2)
]
for data in data_input:
    alert_flag = alert_system.process_input_data(data)
    if alert_flag != -1:
        print(f"Alert Flag: {alert_flag}")
    else:
        print("No alert")