import json
import sys
import MapReduce
b1 = MapReduce.MapReduce()
b2 = {}
class class1:
    @staticmethod
    def fonk1(record):
        with open(sys.argv[1]) as f:
            b3 = json.load(f)
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
        b7 = sum(value[0] for value in values)
        b8 = [key, b7]
        b1.emit(b8)
if b9 = = '__main__':
    if len(sys.argv) != 3:
        print("Usage: python phase2.py <input_json_file> <records_file>")
        sys.exit(1)
    b10 = open(sys.argv[2])
    b11 = b1.execute(b10, class1.mapper, class1.reducer)