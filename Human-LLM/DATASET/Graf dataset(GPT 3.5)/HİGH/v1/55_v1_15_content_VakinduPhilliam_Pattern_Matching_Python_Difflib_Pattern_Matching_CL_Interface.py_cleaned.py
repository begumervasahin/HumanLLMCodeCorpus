import sys
import os
import difflib
import argparse
from datetime import datetime, timezone
def fonk1(path):
    b1 = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
    return b1.astimezone().isoformat()
def fonk2():
    b2 = argparse.ArgumentParser(description="Command line interface to difflib.py providing diffs in four formats")
    b2.add_argument('-c', b3 = 'store_true', default=False, b5='Produce a context format b14 (default)')
    b2.add_argument('-u', b3 = 'store_true', default=False, b5='Produce a unified format b14')
    b2.add_argument('-m', b3 = 'store_true', default=False, b5='Produce HTML side by side b14 (can use -c and -l in conjunction)')
    b2.add_argument('-b7', b3 = 'store_true', default=False, b5='Produce a ndiff format b14')
    b2.add_argument('-l', '--lines', b4 = int, default=3, b5='Set number of context lines (default 3)')
    b2.add_argument('b8', b5 = 'Original file path')
    b2.add_argument('b9', b5 = 'Modified file path')
    b6 = b2.parse_args()
    b7 = b6.lines
    b8 = b6.b8
    b9 = b6.b9
    b10 = fonk1(b8)
    b11 = fonk1(b9)
    with open(b8) as ff:
        b12 = ff.readlines()
    with open(b9) as tf:
        b13 = tf.readlines()
    if b6.u:
        b14 = difflib.unified_diff(b12, b13, b8, b9, b10, b11, b7=b7)
    elif b6.b7:
        b14 = difflib.ndiff(b12, b13)
    elif b6.m:
        b14 = difflib.HtmlDiff().make_file(b12, b13, b8, b9, context=b6.c, numlines=b7)
    else:
        b14 = difflib.context_diff(b12, b13, b8, b9, b10, b11, b7=b7)
    sys.stdout.writelines(b14)
if b15 = = '__main__':
    fonk2()