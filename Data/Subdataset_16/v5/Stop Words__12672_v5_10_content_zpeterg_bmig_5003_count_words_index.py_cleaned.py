import sys
import json
from getFile import getFile
from filter import Filter
from format import formatToLines
from utils import dealArgs
from writeFile import writeFile, writeCSV
from getStats import getStats
def fonk1(b5):
    b1 = Filter(b5)
    b2 = getFile(b5['file'], b1.filter)
    return b2
def fonk2(b5, b2):
    if b5.get('stats'):
        return getStats(b2)
    if b5.get('format'):
        return formatToLines(b2)
    return b2
def fonk3(b5, b6):
    if b5.get('output'):
        if b5.get('csv'):
            b3 = ['Name']
            if isinstance(b6, dict):
                b3.append('Count')
            writeCSV(b6, b5['output'], b3)
        else:
            b4 = json.dumps(b6, indent=4)
            writeFile(b4, b5['output'])
        print(f"\nThe requested b6 has been written to file {b5['output']}.")
    else:
        fonk4(b6)
def fonk4(b6):
    if isinstance(b6, dict):
        if len(b6) <= 1:
            print('No stats to print.')
        else:
            print('STATS:')
            for stat, value in b6.items():
                print(f'{stat}: {value}')
    else:
        if len(b6) <= 1:
            print('No b2 to print.')
        else:
            print('WORDS:')
            for word in b6:
                print(word)
def fonk5(args):
    b5 = dealArgs(args).to_object()
    b2 = fonk1(b5)
    b6 = fonk2(b5, b2)
    fonk3(b5, b6)
if b7 = = '__main__':
    fonk5(sys.argv)