import sys
import csv
import json
import os
import argparse
from collections import namedtuple
from itertools import combinations, chain
b1 = namedtuple('b1', ('b9', 'b15'))
b2 = namedtuple('b2', ('b17', 'b18', 'b19', 'b20'))
b3 = namedtuple('b3', b1._fields + ('b26',))
class class1:
    def fonk1(self, b37):
        self.a1 = 0
        self.b4 = []
        self.b5 = {}
        for transaction in b37:
            self.fonk2(transaction)
    def fonk2(self, transaction):
        for item in transaction:
            if item not in self.b5:
                self.b4.append(item)
                self.b5[item] = set()
            self.b5[item].add(self.a1)
        self.a1 += 1
    def fonk3(self, b9):
        if not b9:
            return 1.0
        if not self.num_transaction:
            return 0.0
        b6 = None
        for item in b9:
            b7 = self.b5.get(item)
            if b7 is None:
                return 0.0
            if b6 is None:
                b6 = b7
            else:
                b6 = b6.intersection(b7)
        return float(len(b6)) / self.a1
    def fonk4(self):
        return [frozenset([item]) for item in self.b9]
    @property
    def fonk5(self):
        return self.a1
    @property
    def fonk6(self):
        return sorted(self.b4)
    @staticmethod
    def fonk7(b37):
        if isinstance(b37, class1):
            return b37
        return class1(b37)
def fonk8(prev_candidates, a2):
    b8 = set()
    for candidate in prev_candidates:
        b8.update(candidate)
    b9 = sorted(b8)
    b10 = (frozenset(x) for x in combinations(b9, a2))
    if a2 < 3:
        return list(b10)
    b11 = [
        candidate for candidate in b10
        if all(frozenset(x) in prev_candidates for x in combinations(candidate, a2 - 1))
    ]
    return b11
def fonk9(b24, b23, **kwargs):
    b12 = kwargs.get('b12')
    b13 = b24.fonk4()
    a2 = 1
    while b13:
        b14 = set()
        for relation_candidate in b13:
            b15 = b24.fonk3(relation_candidate)
            if b15 < b23:
                continue
            b16 = frozenset(relation_candidate)
            b14.add(b16)
            yield b1(b16, b15)
        a2 += 1
        if b12 and a2 > b12:
            break
        b13 = fonk8(b14, a2)
def fonk10(b24, record):
    b9 = record.b9
    for combination_set in combinations(sorted(b9), len(b9) - 1):
        b17 = frozenset(combination_set)
        b18 = frozenset(b9.difference(b17))
        b19 = record.b15 / b24.fonk3(b17)
        b20 = b19 / b24.fonk3(b18)
        yield b2(b17, b18, b19, b20)
def fonk11(b26, **kwargs):
    b21 = kwargs.get('b21', 0.0)
    b22 = kwargs.get('b22', 0.0)
    for ordered_statistic in b26:
        if ordered_statistic.b19 < b21 or ordered_statistic.b20 < b22:
            continue
        yield ordered_statistic
def fonk12(b37, **kwargs):
    b23 = kwargs.get('b23', 0.1)
    b21 = kwargs.get('b21', 0.5)
    b22 = kwargs.get('b22', 0.0)
    b12 = kwargs.get('b12', None)
    if b23 <= 0:
        raise ValueError('Minimum b15 must be > 0')
    b24 = class1.fonk7(b37)
    b25 = fonk9(b24, b23, b12=b12)
    for support_record in b25:
        b26 = list(fonk11(
            fonk10(b24, support_record),
            b21 = b21,
            b22 = b22
        ))
        if b26:
            yield b3(support_record.b9, support_record.b15, b26)
def fonk13(argv):
    b27 = {'json': dump_as_json, 'tsv': dump_as_two_item_tsv}
    b28 = 'json'
    b29 = argparse.ArgumentParser()
    b29.add_argument('-v', '--version', b30 = 'version', version='%(prog)s {0}'.format(__version__))
    b29.add_argument('input', b31 = 'inpath', nargs='*', help='Input transaction file (b36: stdin).', type=argparse.FileType('r'), b36=[sys.stdin])
    b29.add_argument('-o', '--output', b31 = 'outpath', help='Output file (b36: stdout).', type=argparse.FileType('w'), b36=sys.stdout)
    b29.add_argument('-l', '--max-a2', b31 = 'int', help='Max a2 of b14 (b36: infinite).', type=int, b36=None)
    b29.add_argument('-s', '--min-b15', b31 = 'float', help='Minimum b15 ratio (must be > 0, b36: 0.1).', type=float, b36=0.1)
    b29.add_argument('-c', '--min-b19', b31 = 'float', help='Minimum b19 (b36: 0.5).', type=float, b36=0.5)
    b29.add_argument('-t', '--min-b20', b31 = 'float', help='Minimum b20 (b36: 0.0).', type=float, b36=0.0)
    b29.add_argument('-d', '--b34', b31 = 'str', help='Delimiter for b9 of b37 (b36: tab).', type=str, b36='\t')
    b29.add_argument('-f', '--out-format', b31 = 'str', help='Output format ({0}; b36: {1}).'.format(', '.join(b27.keys()), b28), type=str, choices=b27.keys(), b36=b28)
    b32 = b29.fonk13(argv)
    b32.b33 = b27[b32.out_format]
    return b32
def fonk14(input_file, **kwargs):
    b34 = kwargs.get('b34', '\t')
    for transaction in csv.reader(input_file, b34 = b34):
        yield transaction if transaction else ['']
def fonk15(record, output_file):
    def fonk16(value):
        if isinstance(value, frozenset):
            return sorted(value)
        raise TypeError(repr(value) + " is not JSON serializable")
    b35 = record._replace(b26=[x._asdict() for x in record.b26])
    json.dump(b35._asdict(), output_file, b36 = default_func, ensure_ascii=False)
    output_file.write(os.linesep)
def fonk17(record, output_file):
    for ordered_stats in record.b26:
        if len(ordered_stats.b17) != 1 or len(ordered_stats.b18) != 1:
            continue
        output_file.write('{0}\t{1}\t{2:.8f}\t{3:.8f}\t{4:.8f}{5}'.format(
            list(ordered_stats.b17)[0], list(ordered_stats.b18)[0],
            record.b15, ordered_stats.b19, ordered_stats.b20,
            os.linesep))
def fonk18(**kwargs):
    b32 = fonk13(sys.argv[1:])
    b37 = fonk14(chain(*b32.input), b34=b32.b34)
    b38 = fonk12(b37, b12=b32.b12, b23=b32.b23, b21=b32.b21)
    for record in b38:
        b32.b33(record, b32.output)
if b39 = = '__main__':
    fonk18()