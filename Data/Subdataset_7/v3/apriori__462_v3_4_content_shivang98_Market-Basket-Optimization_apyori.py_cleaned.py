import sys
import csv
import json
import os
import argparse
from collections import namedtuple
from itertools import combinations, chain
b1 = namedtuple('b1', ('b4', 'b14'))
b2 = namedtuple('b2', ('b16', 'b17', 'b18', 'b19'))
b3 = namedtuple('b3', b1._fields + ('b24',))
class class1:
    def fonk1(self, b36):
        self.a1 = 0
        self.b4 = []
        self.b5 = {}
        for transaction in b36:
            self.fonk2(transaction)
    def fonk2(self, transaction):
        for item in transaction:
            if item not in self.b5:
                self.b4.append(item)
                self.b5[item] = set()
            self.b5[item].add(self.a1)
        self.a1 += 1
    def fonk3(self, b4):
        if not b4:
            return 1.0
        if not self.a1:
            return 0.0
        b6 = None
        for item in b4:
            b7 = self.b5.get(item)
            if b7 is None:
                return 0.0
            if b6 is None:
                b6 = b7
            else:
                b6 = b6.intersection(b7)
        return float(len(b6)) / self.a1
    def fonk4(self):
        return [frozenset([item]) for item in self.b4]
def fonk5(prev_candidates, a2):
    b8 = set()
    for candidate in prev_candidates:
        b8.update(candidate)
    b4 = sorted(b8)
    b9 = (frozenset(x) for x in combinations(b4, a2))
    if a2 < 3:
        return list(b9)
    b10 = [
        candidate for candidate in b9
        if all(frozenset(x) in prev_candidates for x in combinations(candidate, a2 - 1))
    ]
    return b10
def fonk6(b22, b21, b11 = None):
    b12 = b22.fonk4()
    a2 = 1
    while b12:
        b13 = set()
        for relation_candidate in b12:
            b14 = b22.fonk3(relation_candidate)
            if b14 < b21:
                continue
            b15 = frozenset(relation_candidate)
            b13.add(b15)
            yield b1(b15, b14)
        a2 += 1
        if b11 and a2 > b11:
            break
        b12 = fonk5(b13, a2)
def fonk7(b22, record):
    b4 = record.b4
    for combination_set in combinations(sorted(b4), len(b4) - 1):
        b16 = frozenset(combination_set)
        b17 = frozenset(b4.difference(b16))
        b18 = record.b14 / b22.fonk3(b16)
        b19 = b18 / b22.fonk3(b17)
        yield b2(b16, b17, b18, b19)
def fonk8(b24, b20 = 0.0, b25=0.0):
    for ordered_statistic in b24:
        if ordered_statistic.b18 < b20 or ordered_statistic.b19 < b25:
            continue
        yield ordered_statistic
def fonk9(b36, b21 = 0.1, b20=0.5, b25=0.0, b11=None):
    if b21 <= 0:
        raise ValueError('Minimum b14 must be > 0')
    b22 = class1(b36)
    b23 = fonk6(b22, b21, b11=b11)
    for support_record in b23:
        b24 = list(fonk8(
            fonk7(b22, support_record),
            b20 = b20,
            b25 = b25
        ))
        if b24:
            yield b3(support_record.b4, support_record.b14, b24)
def fonk10(argv):
    b26 = {'json': dump_as_json, 'tsv': dump_as_two_item_tsv}
    b27 = 'json'
    b28 = argparse.ArgumentParser()
    b28.add_argument('-v', '--version', b29 = 'version', version='%(prog)s {0}'.format(__version__))
    b28.add_argument('input', b30 = 'inpath', nargs='*', help='Input transaction file (b35: stdin).', type=argparse.FileType('r'), b35=[sys.stdin])
    b28.add_argument('-o', '--output', b30 = 'outpath', help='Output file (b35: stdout).', type=argparse.FileType('w'), b35=sys.stdout)
    b28.add_argument('-l', '--max-a2', b30 = 'int', help='Max a2 of b13 (b35: infinite).', type=int, b35=None)
    b28.add_argument('-s', '--min-b14', b30 = 'float', help='Minimum b14 ratio (must be > 0, b35: 0.1).', type=float, b35=0.1)
    b28.add_argument('-c', '--min-b18', b30 = 'float', help='Minimum b18 (b35: 0.5).', type=float, b35=0.5)
    b28.add_argument('-t', '--min-b19', b30 = 'float', help='Minimum b19 (b35: 0.0).', type=float, b35=0.0)
    b28.add_argument('-d', '--b33', b30 = 'str', help='Delimiter for b4 of b36 (b35: tab).', type=str, b35='\t')
    b28.add_argument('-f', '--out-format', b30 = 'str', help='Output format ({0}; b35: {1}).'.format(', '.join(b26.keys()), b27), type=str, choices=b26.keys(), b35=b27)
    b31 = b28.fonk10(argv)
    b31.b32 = b26[b31.out_format]
    return b31
def fonk11(input_file, b33 = '\t'):
    for transaction in csv.reader(input_file, b33 = b33):
        yield transaction if transaction else ['']
def fonk12(record, output_file):
    def fonk13(value):
        if isinstance(value, frozenset):
            return sorted(value)
        raise TypeError(repr(value) + " is not JSON serializable")
    b34 = record._replace(b24=[x._asdict() for x in record.b24])
    json.dump(b34._asdict(), output_file, b35 = default_func, ensure_ascii=False)
    output_file.write(os.linesep)
def fonk14(record, output_file):
    for ordered_stats in record.b24:
        if len(ordered_stats.b16) != 1 or len(ordered_stats.b17) != 1:
            continue
        output_file.write('{0}\t{1}\t{2:.8f}\t{3:.8f}\t{4:.8f}{5}'.format(
            list(ordered_stats.b16)[0], list(ordered_stats.b17)[0],
            record.b14, ordered_stats.b18, ordered_stats.b19,
            os.linesep))
def fonk15():
    b31 = fonk10(sys.argv[1:])
    b36 = fonk11(chain(*b31.input), b33=b31.b33)
    b37 = fonk9(b36, b21=b31.b21, b20=b31.b20, b25=b31.b25, b11=b31.b11)
    for record in b37:
        b31.b32(record, b31.output)
if b38 = = '__main__':
    fonk15()