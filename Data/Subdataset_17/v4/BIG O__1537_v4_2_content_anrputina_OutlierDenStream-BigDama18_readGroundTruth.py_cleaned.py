
import pandas as pd
class GroundTruth:
    def __init__(self, filename, file_type='txt'):
        self.filename = filename
        self.events = []
        self.clears = []
        if file_type == 'txt':
            self.read_file()
        elif file_type == 'csv':
            self.read_file_csv()
    def add_event(self, event):
        self.events.append(event)
    def add_clear(self, clear):
        self.clears.append(clear)
    def build_clear(self):
        for idx in range(len(self.events)):
            if self.events[idx]['type'] == 'single':
                if idx < len(self.events) - 1:
                    idx2 = idx + 1
                    while idx2 <= len(self.events) - 1 and self.events[idx2]['type'] == 'multiple':
                        idx2 += 1
                    clear_record = {
                        'name': 'clear' + str(idx),
                        'startTime': self.events[idx]['endTime'] + 1,
                        'endTime': self.events[idx2]['startTime'] - 1
                    }
                    self.clears.append(clear_record)
                if idx == len(self.events) - 1:
                    clear_record = {
                        'name': 'clear' + str(idx),
                        'startTime': self.events[idx]['endTime'] + 1,
                        'endTime': self.events[idx]['endTime'] + 1 + 300
                    }
                    self.clears.append(clear_record)
        for event in self.events:
            event['type'] = 'single'
    def read_file(self):
        df = pd.read_csv(self.filename, sep='\t', header=None)
        df.columns = ["node", "ip", "startTime", "event"]
        df['endTime'] = df['startTime'] + 300
        df['clearStart'] = df['endTime'] + 1
        df['clearEnd'] = df['startTime'].shift(-1) - 1 - 5
        df['clearEnd'].iloc[-1] = 2000000000
        for _, row in df.iterrows():
            event_record = {
                'name': row.name,
                'startTime': row['startTime'],
                'endTime': row['endTime'],
                'node': row['node'],
                'type': 'single',
                'ONLINE': False,
                'endSent': False
            }
            self.add_event(event_record)
            clear_record = {
                'name': row.name,
                'startTime': row['clearStart'],
                'endTime': row['clearEnd']
            }
            self.add_clear(clear_record)
    def read_file_csv(self):
        df = pd.read_csv(self.filename, sep=',')
        for _, row in df.iterrows():
            event_record = {
                'name': row.name,
                'startTime': row['Start'],
                'endTime': row['End'],
                'node': row['Node'],
                'type': row['Type'],
                'ONLINE': False,
                'endSent': False
            }
            self.add_event(event_record)
        self.build_clear()