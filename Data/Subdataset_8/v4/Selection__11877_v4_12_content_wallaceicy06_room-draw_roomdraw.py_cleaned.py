import argparse
import random
import time
import sys
MCM_CREST =
def welcome():
    print(MCM_CREST)
    print('Welcome to McMurtry College Room Draw.')
    print('This program will sort rooms for selection by highest points, resolving ties randomly.')
    print('Hit ENTER to begin...')
    input('')
def compare_with_ties(a, b):
    diff = (a > b) - (a < b)
    return diff if diff else random.choice([-1, 1])
def run_roomdraw(names_file, delay=0.5, is_desc=False):
    draw_order = []
    try:
        with open(names_file, 'r') as groups_f:
            groups = [(float(line.split()[0]), ' '.join(line.split()[1:]).strip()) for line in groups_f.readlines()]
            random.shuffle(groups)
            draw_order = sorted(groups, key=lambda g: g[0], cmp=compare_with_ties, reverse=is_desc)
            for i, (pts, group) in enumerate(draw_order):
                print(str(i + 1) + ': ' + group + ' (' + str(pts) + ')')
                time.sleep(delay)
            return draw_order
    except IOError:
        print('There was an error opening the specified file \'' + names_file + '\' for read.')
        sys.exit(-1)
    except ValueError:
        print('There was an error in the format of the groups file.')
        sys.exit(-1)
def write_results(out_file, draw_order):
    try:
        with open(out_file, 'w') as out_f:
            out_f.write('Selection Order:\n')
            for i, (pts, group) in enumerate(draw_order):
                out_f.write(str(i + 1) + ': ' + group + ' (' + str(pts) + ')\n')
    except IOError:
        print('There was an error opening the specified file \'' + out_file + '\' for write.')
        sys.exit(-1)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='McMurtry College Room Draw')
    parser.add_argument('infile', help='file containing the list of room groups to randomly sort')
    parser.add_argument('outfile', help='file to output the results to')
    parser.add_argument('-d', '--delay', metavar='seconds', required=False, type=float, default=0.5,
                        help='delay between selections in decimal seconds (0.5 by default)')
    parser.add_argument('-a', '--ascending', required=False, action='store_true', default=False,
                        help='sort in ascending order (descending by default)')
    args = parser.parse_args()
    welcome()
    draw_order = run_roomdraw(args.infile, args.delay, not args.ascending)
    write_results(args.outfile, draw_order)