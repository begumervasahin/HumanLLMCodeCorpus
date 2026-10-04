import json
import sys
import MapReduce
b1 = MapReduce.MapReduce()
b2 = {}
class class1:
    @staticmethod
    def fonk1(record):
        with open(sys.argv[1]) as f:
            for line in f:
                b3 = json.loads(line)
                b4 = sum(1 for chunk_line in b3 if set(chunk_line) >= set(record))
                b5 = tuple(record)
                b2[b5] = [b4, len(b3)]
                b1.emit_intermediate(b5, [b4, len(b3)])
    @staticmethod
    def fonk2(key, values):
        b6 = sum(value[0] for value in values)
        b1.emit([key, b6])
if b7 = = '__main__':
    b8 = open(sys.argv[2])
    b9 = b1.execute(b8, class1.mapper, class1.reducer)