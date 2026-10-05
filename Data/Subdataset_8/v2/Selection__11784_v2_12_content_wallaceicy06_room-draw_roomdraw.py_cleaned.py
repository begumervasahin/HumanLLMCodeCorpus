import argparse
import random
import sys
import time
MCM_CREST =
def welcome():
    print(MCM_CREST)
    print('Welcome to McMurtry College Room Draw.')
    print('This program will sort rooms for selection by highest points, '
          'resolving ties randomly.')
    input('Hit ENTER to begin...')
def compare_with_ties(a, b):
    diff = a - b
    return diff if diff else random.choice([-1, 1])
def run_roomdraw(names_file, delay=0.5, is_desc=False):
    draw_order = []
    try:
        with open(names_file, 'r') as groups_f:
            groups = [line.split() for line in groups_f.readlines()]
            groups = [(float(pts), ' '.join(name)) for pts, *name in groups]
            random.shuffle(groups)
            draw_order = sorted(groups, key=lambda g: g[0], reverse=is_desc,
                                cmp=compare_with_ties)
            for i, (pts, group) in enumerate(draw_order, start=1):
                print(f'{i}: {group} ({pts})')
                time.sleep(delay)
            return draw_order
    except IOError as e:
        print(f'Error opening file "{names_file}": {e}', file=sys.stderr)
    except ValueError as e:
        print(f'Error in file format: {e}', file=sys.stderr)
    sys.exit(-1)
def write_results(out_file, draw_order):
    try:
        with open(out_file, 'w') as out_f:
            out_f.write('Selection Order:\n')
            for i, (pts, group) in enumerate(draw_order, start=1):
                out_f.write(f'{i}: {group} ({pts})\n')
    except IOError as e:
        print(f'Error writing to file "{out_file}": {e}', file=sys.stderr)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='McMurtry College Room Draw')
    parser.add_argument('infile', help='input file containing room groups')
    parser.add_argument('outfile', help='output file for sorted room groups')
    parser.add_argument('-d', '--delay', metavar='seconds', type=float,
                        default=0.5, help='delay between selections (default: 0.5)')
    parser.add_argument('-a', '--ascending', action='store_true',
                        help='sort in ascending order (descending by default)')
    args = parser.parse_args()
    welcome()
    draw_order = run_roomdraw(args.infile, args.delay, not args.ascending)
    write_results(args.outfile, draw_order)