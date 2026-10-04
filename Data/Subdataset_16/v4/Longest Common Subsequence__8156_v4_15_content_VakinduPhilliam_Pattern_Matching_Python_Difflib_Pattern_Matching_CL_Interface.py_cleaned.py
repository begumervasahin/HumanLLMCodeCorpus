import sys
import os
import difflib
import argparse
from datetime import datetime, timezone
def fonk1(path):
    b1 = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
    return b1.astimezone().isoformat()
def fonk2():
    b2 = argparse.ArgumentParser(description="Provide diffs in various formats.")
    b2.add_argument('-c', b3 = 'store_true', default=False,
                        b4 = 'Produce a context format b13 (default)')
    b2.add_argument('-u', b3 = 'store_true', default=False,
                        b4 = 'Produce a unified format b13')
    b2.add_argument('-m', b3 = 'store_true', default=False,
                        b4 = 'Produce HTML side-by-side b13 '
                             '(can use -c and -l in conjunction)')
    b2.add_argument('-n', b3 = 'store_true', default=False,
                        b4 = 'Produce an ndiff format b13')
    b2.add_argument('-l', '--lines', b5 = int, default=3,
                        b4 = 'Set number of context lines (default 3)')
    b2.add_argument('b7', b4 = 'The original file')
    b2.add_argument('b8', b4 = 'The modified file')
    b6 = b2.parse_args()
    b7 = b6.b7
    b8 = b6.b8
    b9 = fonk1(b7)
    b10 = fonk1(b8)
    with open(b7) as ff:
        b11 = ff.readlines()
    with open(b8) as tf:
        b12 = tf.readlines()
    if b6.u:
        b13 = difflib.unified_diff(b11, b12, b7, b8, b9, b10, n=b6.lines)
    elif b6.n:
        b13 = difflib.ndiff(b11, b12)
    elif b6.m:
        b13 = difflib.HtmlDiff().make_file(b11, b12, b7, b8, context=b6.c, numlines=b6.lines)
    else:
        b13 = difflib.context_diff(b11, b12, b7, b8, b9, b10, n=b6.lines)
    if b6.m:
        sys.stdout.write(b13)
    else:
        sys.stdout.writelines(b13)
if b14 = = '__main__':
    fonk2()