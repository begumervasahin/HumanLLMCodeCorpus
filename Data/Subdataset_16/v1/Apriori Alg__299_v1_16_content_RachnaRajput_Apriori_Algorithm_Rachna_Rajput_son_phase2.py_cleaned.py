import json
import sys
import MapReduce
b1 = MapReduce.MapReduce()
b2 = {}
class class1:
    @staticmethod
    def fonk1(record):
        with open(sys.argv[1]) as f:
            b3 = []
            for line in f:
                b4 = json.loads(line)
                a1 = 0
                b5 = len(b4)
                for chunkline in b4:
                    if set(chunkline) >= set(record):
                        a1 += 1
                b3 = [a1, b5]
                b6 = tuple(record)
                b2[b6] = b3
                b1.emit_intermediate(b6, b3)
    @staticmethod
    def fonk2(key, values):
        a1 = sum(value[0] for value in values)
        b3 = [key, a1]
        b1.emit(b3)
if b7 = = '__main__':
    b8 = open(sys.argv[2])
    b9 = b1.execute(b8, class1.mapper, class1.reducer)