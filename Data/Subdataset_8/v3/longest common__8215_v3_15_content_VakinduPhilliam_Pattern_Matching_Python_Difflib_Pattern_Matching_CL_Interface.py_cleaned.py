import sys
import os
import difflib
import argparse
from datetime import datetime, timezone
def get_file_last_modified_time(path):
    modified_time = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
    return modified_time.astimezone().isoformat()
def generate_diff(from_lines, to_lines, from_file_path, to_file_path, from_date, to_date, num_context_lines, diff_type):
    if diff_type == 'unified':
        return difflib.unified_diff(from_lines, to_lines, from_file_path, to_file_path, from_date, to_date, n=num_context_lines)
    elif diff_type == 'ndiff':
        return difflib.ndiff(from_lines, to_lines)
    elif diff_type == 'html':
        return difflib.HtmlDiff().make_file(from_lines, to_lines, from_file_path, to_file_path, context=options.c, numlines=num_context_lines)
    else:
        return difflib.context_diff(from_lines, to_lines, from_file_path, to_file_path, from_date, to_date, n=num_context_lines)
def main():
    parser = argparse.ArgumentParser(description="Command line tool for generating file diffs in various formats")
    parser.add_argument('-c', action='store_true', default=False, help='Produce a context format diff (default)')
    parser.add_argument('-u', action='store_true', default=False, help='Produce a unified format diff')
    parser.add_argument('-m', action='store_true', default=False, help='Produce HTML side by side diff (can use -c and -l in conjunction)')
    parser.add_argument('-n', action='store_true', default=False, help='Produce a ndiff format diff')
    parser.add_argument('-l', '--lines', type=int, default=3, help='Set number of context lines (default 3)')
    parser.add_argument('fromfile', help='Original file path')
    parser.add_argument('tofile', help='Modified file path')
    options = parser.parse_args()
    num_context_lines = options.lines
    from_file_path = options.fromfile
    to_file_path = options.tofile
    from_file_modified_time = get_file_last_modified_time(from_file_path)
    to_file_modified_time = get_file_last_modified_time(to_file_path)
    with open(from_file_path) as from_file, open(to_file_path) as to_file:
        from_lines = from_file.readlines()
        to_lines = to_file.readlines()
    if options.u:
        diff_type = 'unified'
    elif options.n:
        diff_type = 'ndiff'
    elif options.m:
        diff_type = 'html'
    else:
        diff_type = 'context'
    generated_diff = generate_diff(from_lines, to_lines, from_file_path, to_file_path, from_file_modified_time, to_file_modified_time, num_context_lines, diff_type)
    sys.stdout.writelines(generated_diff)
if __name__ == '__main__':
    main()