class DealArgs:
    def __init__(self, args):
        self.start = ''
        self.stop = ''
        self.finish = ''
        self._format = False
        self._output = ''
        self._stats = False
        self._csv = False
        for arg in args:
            key_value = arg.split('=')
            key = key_value[0]
            value = key_value[1] if len(key_value) > 1 else None
            if key == '--input' and value:
                self.file = value
            elif key == '--start':
                self.start = value
            elif key == '--stop':
                self.stop = value
            elif key == '--finish':
                self.finish = value
            elif key == '--output':
                self.output = value
        if not hasattr(self, 'file'):
            raise ValueError('You must supply a file with --input')
        if '-s' in args:
            self.stats = True
        elif '-f' in args:
            self.format = True
        if '-c' in args:
            self.csv = True
    @property
    def file(self):
        return self._file
    @file.setter
    def file(self, file):
        if not file:
            raise ValueError('You must supply a file')
        self._file = file
    @property
    def output(self):
        if self.csv and self._output and not self._output.endswith('.csv'):
            return self._output + '.csv'
        if not self.csv and self._output and not self._output.endswith('.json'):
            return self._output + '.json'
        return self._output
    @output.setter
    def output(self, output):
        self._output = output
    @property
    def stats(self):
        return self._stats
    @stats.setter
    def stats(self, stats):
        self._stats = bool(stats)
        if self._stats:
            self._format = False
    @property
    def format(self):
        return self._format
    @format.setter
    def format(self, format_flag):
        self._format = bool(format_flag)
    @property
    def csv(self):
        return self._csv
    @csv.setter
    def csv(self, csv_flag):
        self._csv = bool(csv_flag)
        if self._csv:
            self._format = False
    def to_object(self):
        return {
            "file": self.file,
            "start": self.start,
            "stop": self.stop,
            "finish": self.finish,
            "format": self.format,
            "output": self.output,
            "stats": self.stats,
            "csv": self.csv,
        }
def clean_word(word):
    word = word.lower()
    word = word.replace('\n', '')
    return word.strip("~`!@
