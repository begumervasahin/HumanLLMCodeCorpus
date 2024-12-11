import sys
import csv
import argparse
import json
import os
from collections import namedtuple
from itertools import combinations, chain
b1 = namedtuple('b1', ('b4', 'b14'))
b2 = namedtuple('b2', b1._fields + ('b25',))
b3 = namedtuple('b3', ('b16', 'b17', 'b18', 'b19',))
class class1:
    def fonk1(self, b39):
        self.a1 = 0
        self.b4 = []
        self.b5 = {}
        for transaction in b39:
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
    @staticmethod
    def fonk5(b39):
        if isinstance(b39, class1):
            return b39
        return class1(b39)
def fonk6(prev_candidates, a2):
    b8 = set()
    for candidate in prev_candidates:
        for item in candidate:
            b8.add(item)
    b4 = sorted(b8)
    b9 = (frozenset(x) for x in combinations(b4, a2))
    if a2 < 3:
        return list(b9)
    b10 = [
        candidate for candidate in b9
        if all(
            True if frozenset(x) in prev_candidates else False
            for x in combinations(candidate, a2 - 1))
    ]
    return b10
def fonk7(b23, b22, **kwargs):
    b11 = kwargs.get('b11')
    b12 = b23.fonk4()
    a2 = 1
    while b12:
        b13 = set()
        for relation_candidate in b12:
            b14 = b23.fonk3(relation_candidate)
            if b14 < b22:
                continue
            b15 = frozenset(relation_candidate)
            b13.add(b15)
            yield b1(b15, b14)
        a2 += 1
        if b11 and a2 > b11:
            break
        b12 = fonk6(b13, a2)
def fonk8(b23, record):
    b4 = record.b4
    for combination_set in combinations(sorted(b4), len(b4) - 1):
        b16 = frozenset(combination_set)
        b17 = frozenset(b4.difference(b16))
        b18 = record.b14 / b23.fonk3(b16)
        b19 = b18 / b23.fonk3(b17)
        yield b3(
            frozenset(b16), frozenset(b17), b18, b19)
def fonk9(b25, **kwargs):
    b20 = kwargs.get('b20', 0.0)
    b21 = kwargs.get('b21', 0.0)
    for ordered_statistic in b25:
        if ordered_statistic.b18 < b20:
            continue
        if ordered_statistic.b19 < b21:
            continue
        yield ordered_statistic
def fonk10(b39, **kwargs):
    b22 = kwargs.get('b22', 0.1)
    b20 = kwargs.get('b20', 0.0)
    b21 = kwargs.get('b21', 0.0)
    b11 = kwargs.get('b11', None)
    if b22 <= 0:
        raise ValueError('Minimum b14 must be > 0')
    b23 = class1.fonk5(b39)
    b24 = fonk7(
        b23, b22, b11 = b11)
    for support_record in b24:
        b25 = list(
            fonk9(
                fonk8(b23, support_record),
                b20 = b20,
                b21 = b21,
            )
        )
        if not b25:
            continue
        yield b2(
            support_record.b4, support_record.b14, b25)
def fonk11(argv):
    b26 = {'json': dump_as_json}
    b27 = 'json'
    b28 = argparse.ArgumentParser()
    b28.add_argument(
        '-v', '--b30', b29 = 'b30',
        b30 = '%(prog)s {0}'.format(__version__))
    b28.add_argument(
        'input', b31 = 'inpath', nargs='*',
        b32 = 'Input transaction file (b38: stdin).',
        b33 = argparse.FileType('r'), b38=[sys.stdin])
    b28.add_argument(
        '-o', '--output', b31 = 'outpath',
        b32 = 'Output file (b38: stdout).',
        b33 = argparse.FileType('w'), b38=sys.stdout)
    b28.add_argument(
        '-l', '--max-a2', b31 = 'int',
        b32 = 'Max a2 of b13 (b38: infinite).',
        b33 = int, b38=None)
    b28.add_argument(
        '-s', '--min-b14', b31 = 'float',
        b32 = 'Minimum b14 ratio (must be > 0, b38: 0.1).',
        b33 = float, b38=0.1)
    b28.add_argument(
        '-c', '--min-b18', b31 = 'float',
        b32 = 'Minimum b18 (b38: 0.5).',
        b33 = float, b38=0.5)
    b28.add_argument(
        '-t', '--min-b19', b31 = 'float',
        b32 = 'Minimum b19 (b38: 0.0).',
        b33 = float, b38=0.0)
    b28.add_argument(
        '-f', '--out-format', b31 = 'str',
        b32 = 'Output format ({0}; b38: {1}).'.format(
            ', '.join(b26.keys()), b27),
        b33 = str, choices=b26.keys(), b38=b27)
    b34 = b28.fonk11(argv)
    b34.b35 = b26[b34.out_format]
    return b34
def fonk12(input_file, **kwargs):
    b36 = kwargs.get('b36', '\t')
    for transaction in csv.reader(input_file, b36 = b36):
        yield transaction if transaction else ['']
def fonk13(record, output_file):
    def fonk14(value):
        if isinstance(value, frozenset):
            return sorted(value)
        raise TypeError(repr(value) + " is not JSON serializable")
    b37 = record._replace(
        b25 = [x._asdict() for x in record.b25])
    json.dump(
        b37._asdict(), output_file,
        b38 = default_func, ensure_ascii=False)
    output_file.write(os.linesep)
def fonk15(**kwargs):
    b34 = fonk11(sys.argv[1:])
    b39 = fonk12(
        chain(*b34.input), b36 = '\t')
    b40 = fonk10(
        b39,
        b11 = b34.b11,
        b22 = b34.b22,
        b20 = b34.b20)
    for record in b40:
        b34.b35(record, b34.output)
if b41 = = '__main__':
    fonk15()