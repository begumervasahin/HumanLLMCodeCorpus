
import sys
import csv
import argparse
import json
import os
from collections import namedtuple
from itertools import combinations, chain
b1 = '1.1.1'
b2 = 'Yu Mochizuki'
b3 = 'ymoch.dev@gmail.com'
b4 = namedtuple('b4', ('b12', 'b18'))
b5 = namedtuple('b5', b4._fields + ('b29',))
b6 = namedtuple('b6', ('b20', 'b21', 'b22', 'b23'))
class class1:
    def fonk1(self, b43):
        self.a1 = 0
        self.b7 = []
        self.b8 = {}
        for transaction in b43:
            self.fonk2(transaction)
    def fonk2(self, transaction):
        for item in transaction:
            if item not in self.b8:
                self.b7.append(item)
                self.b8[item] = set()
            self.b8[item].add(self.a1)
        self.a1 += 1
    def fonk3(self, b12):
        if not b12:
            return 1.0
        if not self.num_transaction:
            return 0.0
        b9 = None
        for item in b12:
            b10 = self.b8.get(item)
            if b10 is None:
                return 0.0
            if b9 is None:
                b9 = b10
            else:
                b9 = b9.intersection(b10)
        return float(len(b9)) / self.a1
    def fonk4(self):
        return [frozenset([item]) for item in self.b12]
    @property
    def fonk5(self):
        return self.a1
    @property
    def fonk6(self):
        return sorted(self.b7)
    @staticmethod
    def fonk7(b43):
        if isinstance(b43, class1):
            return b43
        return class1(b43)
def fonk8(prev_candidates, a2):
    b11 = set()
    for candidate in prev_candidates:
        for item in candidate:
            b11.add(item)
    b12 = sorted(b11)
    b13 = (frozenset(x) for x in combinations(b12, a2))
    if a2 < 3:
        return list(b13)
    b14 = [
        candidate for candidate in b13
        if all(
            True if frozenset(x) in prev_candidates else False
            for x in combinations(candidate, a2 - 1))
    ]
    return b14
def fonk9(b27, b26, **kwargs):
    b15 = kwargs.get('b15')
    b16 = b27.fonk4()
    a2 = 1
    while b16:
        b17 = set()
        for relation_candidate in b16:
            b18 = b27.fonk3(relation_candidate)
            if b18 < b26:
                continue
            b19 = frozenset(relation_candidate)
            b17.add(b19)
            yield b4(b19, b18)
        a2 += 1
        if b15 and a2 > b15:
            break
        b16 = fonk8(b17, a2)
def fonk10(b27, record):
    b12 = record.b12
    for combination_set in combinations(sorted(b12), len(b12) - 1):
        b20 = frozenset(combination_set)
        b21 = frozenset(b12.difference(b20))
        b22 = (
            record.b18 / b27.fonk3(b20))
        b23 = b22 / b27.fonk3(b21)
        yield b6(
            frozenset(b20), frozenset(b21), b22, b23)
def fonk11(b29, **kwargs):
    b24 = kwargs.get('b24', 0.0)
    b25 = kwargs.get('b25', 0.0)
    for ordered_statistic in b29:
        if ordered_statistic.b22 < b24:
            continue
        if ordered_statistic.b23 < b25:
            continue
        yield ordered_statistic
def fonk12(b43, **kwargs):
    b26 = kwargs.get('b26', 0.1)
    b24 = kwargs.get('b24', 0.0)
    b25 = kwargs.get('b25', 0.0)
    b15 = kwargs.get('b15', None)
    if b26 <= 0:
        raise ValueError('Minimum b18 must be > 0')
    b27 = class1.fonk7(b43)
    b28 = fonk9(
        b27, b26, b15 = b15)
    for support_record in b28:
        b29 = list(
            fonk11(
                fonk10(b27, support_record),
                b24 = b24,
                b25 = b25,
            )
        )
        if not b29:
            continue
        yield b5(
            support_record.b12, support_record.b18, b29)
def fonk13(argv):
    b30 = {'json': dump_as_json, 'tsv': dump_as_two_item_tsv}
    b31 = 'json'
    b32 = argparse.ArgumentParser()
    b32.add_argument(
        '-v', '--b34', b33 = 'b34',
        b34 = '%(prog)s {0}'.format(b1))
    b32.add_argument(
        'input', b35 = 'inpath', nargs='*',
        b36 = 'Input transaction file (b42: stdin).',
        b37 = argparse.FileType('r'), b42=[sys.stdin])
    b32.add_argument(
        '-o', '--output', b35 = 'outpath',
        b36 = 'Output file (b42: stdout).',
        b37 = argparse.FileType('w'), b42=sys.stdout)
    b32.add_argument(
        '-l', '--max-a2', b35 = 'int',
        b36 = 'Max a2 of b17 (b42: infinite).',
        b37 = int, b42=None)
    b32.add_argument(
        '-s', '--min-b18', b35 = 'float',
        b36 = 'Minimum b18 ratio (must be > 0, b42: 0.1).',
        b37 = float, b42=0.1)
    b32.add_argument(
        '-c', '--min-b22', b35 = 'float',
        b36 = 'Minimum b22 (b42: 0.5).',
        b37 = float, b42=0.5)
    b32.add_argument(
        '-t', '--min-b23', b35 = 'float',
        b36 = 'Minimum b23 (b42: 0.0).',
        b37 = float, b42=0.0)
    b32.add_argument(
        '-d', '--b40', b35 = 'str',
        b36 = 'Delimiter for b12 of b43 (b42: tab).',
        b37 = str, b42='\t')
    b32.add_argument(
        '-f', '--out-format', b35 = 'str',
        b36 = 'Output format ({0}; b42: {1}).'.format(
            ', '.join(b30.keys()), b31),
        b37 = str, choices=b30.keys(), b42=b31)
    b38 = b32.fonk13(argv)
    b38.b39 = b30[b38.out_format]
    return b38
def fonk14(input_file, **kwargs):
    b40 = kwargs.get('b40', '\t')
    for transaction in csv.reader(input_file, b40 = b40):
        yield transaction if transaction else ['']
def fonk15(record, output_file):
    def fonk16(value):
        if isinstance(value, frozenset):
            return sorted(value)
        raise TypeError(repr(value) + " is not JSON serializable")
    b41 = record._replace(
        b29 = [x._asdict() for x in record.b29])
    json.dump(
        b41._asdict(), output_file,
        b42 = default_func, ensure_ascii=False)
    output_file.write(os.linesep)
def fonk17(record, output_file):
    for ordered_stats in record.b29:
        if len(ordered_stats.b20) != 1:
            continue
        if len(ordered_stats.b21) != 1:
            continue
        output_file.write('{0}\t{1}\t{2:.8f}\t{3:.8f}\t{4:.8f}{5}'.format(
            list(ordered_stats.b20)[0], list(ordered_stats.b21)[0],
            record.b18, ordered_stats.b22, ordered_stats.b23,
            os.linesep))
def fonk18():
    b38 = fonk13(sys.argv[1:])
    b43 = fonk14(
        chain(*b38.input), b40 = b38.b40)
    b44 = fonk12(
        b43,
        b15 = b38.b15,
        b26 = b38.b26,
        b24 = b38.b24)
    for record in b44:
        b38.b39(record, b38.output)
if b45 = = '__main__':
    fonk18()