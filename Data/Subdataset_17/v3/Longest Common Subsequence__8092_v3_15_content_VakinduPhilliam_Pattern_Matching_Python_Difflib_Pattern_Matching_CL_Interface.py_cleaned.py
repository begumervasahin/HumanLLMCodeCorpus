import sys
import os
import difflib
import argparse
from datetime import datetime, timezone
def get_file_mtime(path):
    mtime = os.stat(path).st_mtime
    return datetime.fromtimestamp(mtime, timezone.utc).astimezone().isoformat()
def read_file_lines(filepath):
    with open(filepath) as file:
        return file.readlines()
def generate_diff(fromfile, tofile, fromlines, tolines, fromdate, todate, options):
    context_lines = options.lines
    if options.u:
        return difflib.unified_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=context_lines)
    elif options.n:
        return difflib.ndiff(fromlines, tolines)
    elif options.m:
        return difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile, context=options.c, numlines=context_lines)
    else:
        return difflib.context_diff(fromlines, tolines, fromfile, tofile, fromdate, todate, n=context_lines)
def main():
    parser = argparse.ArgumentParser(description="Command line tool for generating diffs in various formats using difflib.")
    parser.add_argument('-c', action='store_true', default=False, help='Produce a context format diff (default)')
    parser.add_argument('-u', action='store_true', default=False, help='Produce a unified format diff')
    parser.add_argument('-m', action='store_true', default=False, help='Produce HTML side by side diff (can use -c and -l in conjunction)')
    parser.add_argument('-n', action='store_true', default=False, help='Produce an ndiff format diff')
    parser.add_argument('-l', '--lines', type=int, default=3, help='Set number of context lines (default 3)')
    parser.add_argument('fromfile', help='First file to compare')
    parser.add_argument('tofile', help='Second file to compare')
    options = parser.parse_args()
    fromdate = get_file_mtime(options.fromfile)
    todate = get_file_mtime(options.tofile)
    fromlines = read_file_lines(options.fromfile)
    tolines = read_file_lines(options.tofile)
    diff = generate_diff(options.fromfile, options.tofile, fromlines, tolines, fromdate, todate, options)
    if options.m:
        sys.stdout.write(diff)
    else:
        sys.stdout.writelines(diff)
if __name__ == '__main__':
    main()