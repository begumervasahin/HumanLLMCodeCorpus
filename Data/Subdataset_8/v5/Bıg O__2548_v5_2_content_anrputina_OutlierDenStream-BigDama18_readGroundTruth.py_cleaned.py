import pandas as pd
class GroundTruth:
    def __init__(self, filename, file_type='txt'):
        self.filename = filename
        self.events = []
        self.clears = []
        if file_type == 'txt':
            self.read_txt_file()
        elif file_type == 'csv':
            self.read_csv_file()
    def add_event(self, event):
        self.events.append(event)
    def add_clear(self, clear):
        self.clears.append(clear)
    def build_clear(self):
        for idx, event in enumerate(self.events):
            if event['type'] == 'single':
                idx2 = idx + 1
                while idx2 < len(self.events) and self.events[idx2]['type'] == 'multiple':
                    idx2 += 1
                clear_record = {
                    'name': f'clear{idx}',
                    'startTime': event['endTime'] + 1,
                    'endTime': self.events[idx2]['startTime'] - 1 if idx2 < len(self.events) else event['endTime'] + 301
                }
                self.clears.append(clear_record)
        for event in self.events:
            event['type'] = 'single'
    def read_txt_file(self):
        df = pd.read_csv(self.filename, sep='\t', header=None)
        df.columns = ["node", "ip", "startTime", "event"]
        df['endTime'] = df['startTime'] + 300
        df['clearStart'] = df['endTime'] + 1
        df['clearEnd'] = df['startTime'].shift(-1) - 1 - 5
        df.at[df.index[-1], 'clearEnd'] = 2000000000
        for idx, row in df.iterrows():
            event_record = {
                'name': idx,
                'startTime': row['startTime'],
                'endTime': row['endTime'],
                'node': row['node'],
                'type': 'single',
                'ONLINE': False,
                'endSent': False
            }
            self.add_event(event_record)
            clear_record = {
                'name': idx,
                'startTime': row['clearStart'],
                'endTime': row['clearEnd']
            }
            self.add_clear(clear_record)
    def read_csv_file(self):
        self.df = pd.read_csv(self.filename, sep=',')
        for idx, row in self.df.iterrows():
            event_record = {
                'name': idx,
                'startTime': row['Start'],
                'endTime': row['End'],
                'node': row['Node'],
                'type': row['Type'],
                'ONLINE': False,
                'endSent': False
            }
            self.add_event(event_record)
        self.build_clear()