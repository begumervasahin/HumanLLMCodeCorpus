16. Repository: RachnaRajput/Apriori_Algorithm
   File: Rachna_Rajput_son_phase2.py
   URL: https:
   Code Content:
import json
import sys
import MapReduce
mr = MapReduce.MapReduce()
dict = {}
class Rachna_Rajput_son_phase2:
    def mapper(record):
        f = open(sys.argv[1])
        mylist = []
        for line in f:
            chunkdata = json.loads(line)
            k = 0
            count = 0
            length = len(chunkdata)
            for chunkline in chunkdata:
                if set(chunkline) >= set(record):
                    count = count + 1
            mylist.append(count)
            mylist.append(length)
            recordtuple = tuple(record)
            k = k + 1
            dict[recordtuple] = mylist
        mr.emit_intermediate(recordtuple,mylist)
    def reducer(key, value):
        x = 0
        count = 0
        mylist = []
        i = 0
        while(i < len(value[0])):
            count = count + value[0][i]
            i = i + 2
        somelist = []
        mylist.append(key)
        mylist.append(count)
        mr.emit(mylist)
    if __name__ == '__main__':
        inputdata = open(sys.argv[2])
        output = mr.execute(inputdata, mapper,reducer)
   README Content:
