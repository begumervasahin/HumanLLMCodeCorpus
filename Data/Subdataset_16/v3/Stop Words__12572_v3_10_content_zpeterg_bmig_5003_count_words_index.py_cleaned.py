import sys
import json
from getFile import getFile
from filter import Filter
from format import formatToLines
from utils import dealArgs
from writeFile import writeFile, writeCSV
from getStats import getStats
def fonk1(b4):
    b1 = Filter(b4)
    return getFile(b4['file'], b1.filter)
def fonk2(b5, b4):
    if b4.get('stats'):
        return getStats(b5), True
    elif b4.get('format'):
        return formatToLines(b5), False
    return b5, False
def fonk3(data, b4, b6):
    if b4.get('output'):
        if b4.get('csv'):
            b2 = ['Name'] if not b6 else ['Name', 'Count']
            writeCSV(data, b4['output'], b2)
        else:
            b3 = json.dumps(data, indent=4)
            writeFile(b3, b4['output'])
        print(f"\nThe requested data has been written to file {b4['output']}.")
    else:
        fonk4(data, b6)
def fonk4(data, b6):
    if b6:
        if not data:
            print("\nNo stats to print.")
        else:
            print("\nSTATS:")
            for stat, value in data.items():
                print(f"{stat}: {value}")
    else:
        if not data:
            print("\nNo b5 to print.")
        else:
            print("\nWORDS:")
            for word in data:
                print(word)
def fonk5(args):
    b4 = dealArgs(args).to_object()
    b5 = fonk1(b4)
    processed_data, b6 = fonk2(b5, b4)
    fonk3(processed_data, b4, b6)
if b7 = = '__main__':
    fonk5(sys.argv)