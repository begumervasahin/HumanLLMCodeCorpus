import pandas as pd
class class1:
    def fonk1(self, b2, b1 = 'txt'):
        self.b2 = b2
        self.b3 = []
        self.b4 = []
        if b1 = = 'txt':
            self.fonk5()
        elif b1 = = 'csv':
            self.fonk6()
    def fonk2(self, event):
        self.b3.append(event)
    def fonk3(self, clear):
        self.b4.append(clear)
    def fonk4(self):
        for b7 in range(len(self.b3)):
            if self.b3[b7]['type'] == 'single':
                if b7 < len(self.b3) - 1:
                    b5 = b7 + 1
                    if b5 <= len(self.b3) - 1:
                        while self.b3[b5]['type'] == 'multiple' and b5 < len(self.b3) - 1:
                            b5 += 1
                    b6 = {
                        'name': 'clear' + str(b7),
                        'startTime': self.b3[b7]['endTime'] + 1,
                        'endTime': self.b3[b5]['startTime'] - 1
                    }
                    self.b4.append(b6)
                if b7 = = len(self.b3) - 1:
                    b6 = {
                        'name': 'clear' + str(b7),
                        'startTime': self.b3[b7]['endTime'] + 1,
                        'endTime': self.b3[b7]['endTime'] + 1 + 300
                    }
                    self.b4.append(b6)
        for event in self.b3:
            event['type'] = 'single'
    def fonk5(self):
        b8 = pd.read_csv(self.b2, sep='\t', header=None)
        b8.b9 = ["node", "ip", "startTime", "event"]
        b8['endTime'] = b8['startTime'] + 300
        b8['clearStart'] = b8['endTime'] + 1
        b8['clearEnd'] = b8['startTime'].shift(-1) - 1 - 5
        b8.at[b8.index[-1], 'clearEnd'] = 2000000000
        for row in b8.iterrows():
            b10 = {
                'name': row[0],
                'startTime': row[1]['startTime'],
                'endTime': row[1]['endTime'],
                'node': row[1]['node'],
                'type': 'single',
                'ONLINE': False,
                'endSent': False
            }
            self.fonk2(b10)
            b6 = {
                'name': row[0],
                'startTime': row[1]['clearStart'],
                'endTime': row[1]['clearEnd']
            }
            self.fonk3(b6)
    def fonk6(self):
        self.b8 = pd.read_csv(self.b2, sep=',')
        for row in self.b8.iterrows():
            b10 = {
                'name': row[0],
                'startTime': row[1]['Start'],
                'endTime': row[1]['End'],
                'node': row[1]['Node'],
                'type': row[1]['Type'],
                'ONLINE': False,
                'endSent': False
            }
            self.fonk2(b10)
        self.fonk4()
b2 = 'example.txt'
b11 = class1(b2, b1='txt')
print(b11.b3)
print(b11.b4)