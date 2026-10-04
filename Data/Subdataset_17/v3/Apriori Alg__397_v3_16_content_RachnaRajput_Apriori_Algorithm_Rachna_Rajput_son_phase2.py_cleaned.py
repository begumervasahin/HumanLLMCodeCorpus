import json
import sys
import MapReduce
mr = MapReduce.MapReduce()
intermediate_dict = {}
class Phase2:
    @staticmethod
    def mapper(record):
        with open(sys.argv[1]) as f:
            chunkdata = json.load(f)
            count = 0
            length = len(chunkdata)
            for chunkline in chunkdata:
                if set(chunkline) >= set(record):
                    count += 1
            mylist = [count, length]
            recordtuple = tuple(record)
            intermediate_dict[recordtuple] = mylist
            mr.emit_intermediate(recordtuple, mylist)
    @staticmethod
    def reducer(key, values):
        total_count = sum(value[0] for value in values)
        result = [key, total_count]
        mr.emit(result)
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python phase2.py <input_json_file> <records_file>")
        sys.exit(1)
    inputdata = open(sys.argv[2])
    output = mr.execute(inputdata, Phase2.mapper, Phase2.reducer)