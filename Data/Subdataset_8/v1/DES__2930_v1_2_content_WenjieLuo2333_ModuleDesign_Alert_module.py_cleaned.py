import numpy
class Alert:
    def __init__(self):
        self.bo = []
        self.bp = []
        self.pul = []
        self.average_list = [[] for _ in range(3)]
        self.alert_flag = -1
    def exceed_threshold(self, data, tp):
        if tp == 'bo':
            if not 0.1 <= data <= 0.3:
                return 0
            else:
                return -1
        elif tp == 'bp':
            if not 80 <= data <= 120:
                return 1
            else:
                return -1
        elif tp == 'pul':
            if not 60 <= data <= 90:
                return 2
            else:
                return -1
    def alert_output(self):
        if self.alert_flag != -1:
            return self.alert_flag
        else:
            return -1
    def alert_for_three_categories_input(self, data_in):
        if len(self.average_list[data_in[1]]) < 20:
            self.average_list[data_in[1]].append(float(data_in[0]))
        else:
            del self.average_list[data_in[1]][0]
            self.average_list[data_in[1]].append(float(data_in[0]))
        if len(self.average_list[0]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[0]), 'bo') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[0]), 'bo')
        elif len(self.average_list[1]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[1]), 'bp') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[1]), 'bp')
        elif len(self.average_list[2]) > 2 and self.exceed_threshold(numpy.mean(self.average_list[2]), 'pul') != -1:
            self.alert_flag = self.exceed_threshold(numpy.mean(self.average_list[2]), 'pul')
        return self.alert_flag
alert_obj = Alert()
data_input = [
    (0.15, 0),
    (110, 1),
    (70, 2)
]
for data in data_input:
    alert_flag = alert_obj.alert_for_three_categories_input(data)
    if alert_flag != -1:
        print(f"Alert Flag: {alert_flag}")
    else:
        print("No alert")