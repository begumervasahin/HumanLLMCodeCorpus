16. Repository: RachnaRajput/Apriori_Algorithm
   File: class1.py
   URL: https:
   Code Content:
import json
import sys
import MapReduce
b1 = MapReduce.MapReduce()
b2 = {}
class class1:
    def fonk1(record):
        b3 = open(sys.argv[1])
        b4 = []
        for line in b3:
            b5 = json.loads(line)
            a1 = 0
            a2 = 0
            b6 = len(b5)
            for chunkline in b5:
                if set(chunkline) >= set(record):
                    a2 = a2 + 1
            b4.append(a2)
            b4.append(b6)
            b7 = tuple(record)
            a1 = a1 + 1
            b2[b7] = b4
        b1.emit_intermediate(b7,b4)
    def fonk2(key, value):
        a3 = 0
        a2 = 0
        b4 = []
        a4 = 0
        while(a4 < len(value[0])):
            a2 = a2 + value[0][a4]
            a4 = a4 + 2
        b8 = []
        b4.append(key)
        b4.append(a2)
        b1.emit(b4)
    if b9 = = '__main__':
        b10 = open(sys.argv[2])
        b11 = b1.execute(b10, mapper,reducer)
   README Content:
