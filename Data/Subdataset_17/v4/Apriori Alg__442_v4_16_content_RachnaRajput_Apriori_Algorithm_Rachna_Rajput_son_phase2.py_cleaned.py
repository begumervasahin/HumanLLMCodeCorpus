import json
import sys
import MapReduce
mr = MapReduce.MapReduce()
results_dict = {}
class RachnaRajputPhase2:
    @staticmethod
    def mapper(record):
        with open(sys.argv[1]) as f:
            for line in f:
                chunk_data = json.loads(line)
                count = sum(1 for chunk_line in chunk_data if set(chunk_line) >= set(record))
                record_tuple = tuple(record)
                results_dict[record_tuple] = [count, len(chunk_data)]
                mr.emit_intermediate(record_tuple, [count, len(chunk_data)])
    @staticmethod
    def reducer(key, values):
        total_count = sum(value[0] for value in values)
        mr.emit([key, total_count])
if __name__ == '__main__':
    input_data = open(sys.argv[2])
    output = mr.execute(input_data, RachnaRajputPhase2.mapper, RachnaRajputPhase2.reducer)