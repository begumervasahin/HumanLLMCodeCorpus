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
                a1 = 0
                b4 = len(b3)
                for chunkline in b3:
                    if set(chunkline) >= set(record):
                        a1 += 1
                b5 = [a1, b4]
                b6 = tuple(record)
                b2[b6] = b5
                b1.emit_intermediate(b6, b5)
    @staticmethod
    def fonk2(key, values):
        a1 = sum(value[0] for value in values)
        b7 = [key, a1]
        b1.emit(b7)
if b8 = = '__main__':
    b9 = open(sys.argv[2])
    b10 = b1.execute(b9, class1.mapper, class1.reducer)