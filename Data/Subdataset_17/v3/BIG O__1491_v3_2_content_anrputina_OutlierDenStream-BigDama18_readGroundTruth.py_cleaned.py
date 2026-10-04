import pandas as pd
class GroundTruth:
    def __init__(self, filename, file_type='txt'):
        self.filename = filename
        self.events = []
        self.clears = []
        if file_type == 'txt':
            self._read_txt_file()
        elif file_type == 'csv':
            self._read_csv_file()
    def add_event(self, event):
        self.events.append(event)
    def add_clear(self, clear):
        self.clears.append(clear)
    def build_clear(self):
        for idx, event in enumerate(self.events):
            if event['type'] == 'single':
                if idx < len(self.events) - 1:
                    idx2 = idx + 1
                    while idx2 < len(self.events) and self.events[idx2]['type'] == 'multiple':
                        idx2 += 1
                    clear_record = {
                        'name': f'clear{idx}',
                        'startTime': event['endTime'] + 1,
                        'endTime': self.events[idx2]['startTime'] - 1 if idx2 < len(self.events) else float('inf')
                    }
                else:
                    clear_record = {
                        'name': f'clear{idx}',
                        'startTime': event['endTime'] + 1,
                        'endTime': event['endTime'] + 301
                    }
                self.clears.append(clear_record)
        for event in self.events:
            event['type'] = 'single'
    def _read_txt_file(self):
        df = pd.read_csv(self.filename, sep='\t', header=None)
        df.columns = ["node", "ip", "startTime", "event"]
        df['endTime'] = df['startTime'] + 300
        df['clearStart'] = df['endTime'] + 1
        df['clearEnd'] = df['startTime'].shift(-1) - 6
        df.at[len(df) - 1, 'clearEnd'] = float('inf')
        for index, row in df.iterrows():
            event_record = {
                'name': index,
                'startTime': row['startTime'],
                'endTime': row['endTime'],
                'node': row['node'],
                'type': 'single',
                'ONLINE': False,
                'endSent': False
            }
            self.add_event(event_record)
            clear_record = {
                'name': index,
                'startTime': row['clearStart'],
                'endTime': row['clearEnd']
            }
            self.add_clear(clear_record)
    def _read_csv_file(self):
        df = pd.read_csv(self.filename)
        for index, row in df.iterrows():
            event_record = {
                'name': index,
                'startTime': row['Start'],
                'endTime': row['End'],
                'node': row['Node'],
                'type': row['Type'],
                'ONLINE': False,
                'endSent': False
            }
            self.add_event(event_record)
        self.build_clear()
