import json
import sys
import MapReduce
class class1:
    def fonk1(self):
        self.b1 = MapReduce.MapReduce()
        self.b2 = {}
    def fonk2(self, record):
        with open(sys.argv[1]) as f:
            for line in f:
                b3 = json.loads(line)
                b4 = sum(1 for chunk_line in b3 if set(chunk_line) >= set(record))
                b5 = tuple(record)
                self.b2[b5] = [b4, len(b3)]
                self.b1.emit_intermediate(b5, [b4, len(b3)])
    def fonk3(self, key, values):
        b6 = sum(value[0] for value in values)
        self.b1.emit([key, b6])
    def fonk4(self, input_data_path):
        with open(input_data_path) as input_data:
            self.b1.fonk4(input_data, self.mapper, self.reducer)
def fonk5():
    if len(sys.argv) != 3:
        print("Usage: python script.py <b7> <b8>")
        sys.exit(1)
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    b9 = class1()
    b9.fonk4(b8)
if b10 = = '__main__':
    fonk5()