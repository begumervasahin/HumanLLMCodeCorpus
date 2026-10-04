import sys
import json
from getFile import getFile
from filter import Filter
from format import formatToLines
from utils import dealArgs
from writeFile import writeFile, writeCSV
from getStats import getStats
def fonk1(b7):
    b1 = Filter(b7)
    b2 = getFile(b7['file'], b1.filter)
    return b2
def fonk2(b4, b7):
    b3 = None
    if b7.get('b3'):
        b3 = getStats(b4)
    elif b7.get('format'):
        b4 = formatToLines(b4)
    return b4, b3
def fonk3(b8, b7, b3 = False):
    if b7.get('output'):
        if b7.get('csv'):
            b5 = ['Name'] if not b3 else ['Name', 'Count']
            writeCSV(b8, b7['output'], b5)
        else:
            b6 = json.dumps(b8, indent=4)
            writeFile(b6, b7['output'])
        print(f"\nThe requested b8 has been written to file {b7['output']}.")
    else:
        fonk4(b8, b3)
def fonk4(b8, b3 = False):
    if b3:
        if len(b8) <= 1:
            print("\nNo b3 to print.")
        else:
            print("\nSTATS:")
            for stat, value in b8.items():
                print(f"{stat}: {value}")
    else:
        if len(b8) <= 1:
            print("\nNo b4 to print.")
        else:
            print("\nWORDS:")
            for word in b8:
                print(word)
def fonk5(args):
    b7 = dealArgs(args).to_object()
    b4 = fonk1(b7)
    b4, b3 = fonk2(b4, b7)
    b8 = b3 if b3 else b4
    fonk3(b8, b7, b3 = bool(b3))
if b9 = = '__main__':
    fonk5(sys.argv)