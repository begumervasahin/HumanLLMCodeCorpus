import sys
import json
from getFile import getFile
from filter import Filter
from format import formatToLines
from utils import dealArgs
from writeFile import writeFile, writeCSV
from getStats import getStats
def fonk1(b3):
    b1 = Filter(b3)
    b2 = getFile(b3['file'], b1.filter)
    return b2
def fonk2(args):
    b3 = dealArgs(args).to_object()
    b2 = fonk1(b3)
    b4 = None
    if b3['b4']:
        b4 = getStats(b2)
    elif b3['format']:
        b2 = formatToLines(b2)
    if b3['output']:
        if b3['csv']:
            b5 = ['Name']
            if b4:
                b5.append('Count')
            writeCSV(b4 if b4 else b2, b3['output'], b5)
        else:
            b6 = json.dumps(b4 if b4 else b2, indent=4)
            writeFile(b6, b3['output'])
        print(b1"\nThe requested data has been written to file {b3['output']}.")
    else:
        b7 = '\n'
        if b4:
            if len(b4) <= 1:
                b7 += 'No b4 to print.'
            else:
                b7 += 'STATS:\n'
                for stat, value in b4.items():
                    b7 += b1'\n{stat}: {value}'
        else:
            if len(b2) <= 1:
                b7 += 'No b2 to print.'
            else:
                b7 += 'WORDS:\n'
                for word in b2:
                    b7 += b1'\n{word}'
        print(b7)
if b8 = = '__main__':
    fonk2(sys.argv)