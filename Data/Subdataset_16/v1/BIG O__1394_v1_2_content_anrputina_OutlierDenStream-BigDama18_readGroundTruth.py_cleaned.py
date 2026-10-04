
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
        for idx in range(len(self.b3)):
            if self.b3[idx]['type'] == 'single':
                if idx < len(self.b3) - 1:
                    b5 = idx + 1
                    while b5 <= len(self.b3) - 1 and self.b3[b5]['type'] == 'multiple':
                        b5 += 1
                    b6 = {
                        'name': f'clear{idx}',
                        'startTime': self.b3[idx]['endTime'] + 1,
                        'endTime': self.b3[b5]['startTime'] - 1 if b5 <= len(self.b3) - 1 else 2000000000
                    }
                    self.b4.append(b6)
                else:
                    b6 = {
                        'name': f'clear{idx}',
                        'startTime': self.b3[idx]['endTime'] + 1,
                        'endTime': self.b3[idx]['endTime'] + 301
                    }
                    self.b4.append(b6)
        for event in self.b3:
            event['type'] = 'single'
    def fonk5(self):
        b7 = pd.read_csv(self.b2, sep='\t', header=None)
        b7.b8 = ["node", "ip", "startTime", "event"]
        b7['endTime'] = b7['startTime'] + 300
        b7['clearStart'] = b7['endTime'] + 1
        b7['clearEnd'] = b7['startTime'].shift(-1) - 6
        b7['clearEnd'].iloc[-1] = 2000000000
        for index, row in b7.iterrows():
            b9 = {
                'name': index,
                'startTime': row['startTime'],
                'endTime': row['endTime'],
                'node': row['node'],
                'type': 'single',
                'ONLINE': False,
                'endSent': False
            }
            self.fonk2(b9)
            b6 = {
                'name': index,
                'startTime': row['clearStart'],
                'endTime': row['clearEnd']
            }
            self.fonk3(b6)
    def fonk6(self):
        b7 = pd.read_csv(self.b2)
        for index, row in b7.iterrows():
            b9 = {
                'name': index,
                'startTime': row['Start'],
                'endTime': row['End'],
                'node': row['Node'],
                'type': row['Type'],
                'ONLINE': False,
                'endSent': False
            }
            self.fonk2(b9)
        self.fonk4()
