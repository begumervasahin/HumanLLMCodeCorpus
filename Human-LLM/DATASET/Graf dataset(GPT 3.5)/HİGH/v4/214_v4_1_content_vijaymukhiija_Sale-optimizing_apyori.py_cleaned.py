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
    def fonk1(self, b39):
        self.a1 = 0
        self.b7 = []
        self.b8 = {}
        for transaction in b39:
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
        if not self.a1:
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
        return [frozenset([item]) for item in self.b7]
    @staticmethod
    def fonk5(b39):
        if isinstance(b39, class1):
            return b39
        return class1(b39)
def fonk6(prev_candidates, a2):
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
def fonk7(b27, b26, **kwargs):
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
        b16 = fonk6(b17, a2)
def fonk8(b27, record):
    b12 = record.b12
    for combination_set in combinations(sorted(b12), len(b12) - 1):
        b20 = frozenset(combination_set)
        b21 = frozenset(b12.difference(b20))
        b22 = record.b18 / b27.fonk3(b20)
        b23 = b22 / b27.fonk3(b21)
        yield b6(frozenset(b20), frozenset(b21), b22, b23)
def fonk9(b29, **kwargs):
    b24 = kwargs.get('b24', 0.0)
    b25 = kwargs.get('b25', 0.0)
    for ordered_statistic in b29:
        if ordered_statistic.b22 < b24 or ordered_statistic.b23 < b25:
            continue
        yield ordered_statistic
def fonk10(b39, **kwargs):
    b26 = kwargs.get('b26', 0.1)
    b24 = kwargs.get('b24', 0.0)
    b25 = kwargs.get('b25', 0.0)
    b15 = kwargs.get('b15', None)
    if b26 <= 0:
        raise ValueError('Minimum b18 must be > 0')
    b27 = class1.fonk5(b39)
    b28 = fonk7(b27, b26, b15=b15)
    for support_record in b28:
        b29 = list(fonk9(fonk8(b27, support_record), b24=b24, b25=b25))
        if not b29:
            continue
        yield b5(support_record.b12, support_record.b18, b29)
def fonk11(argv):
    b30 = {'json': dump_as_json}
    b31 = argparse.ArgumentParser()
    b31.add_argument('-v', '--version', b32 = 'version', version='%(prog)s {0}'.format(b1))
    b31.add_argument('input', b33 = 'inpath', nargs='*', help='Input transaction file (b38: stdin)', type=argparse.FileType('r'), b38=[sys.stdin])
    b31.add_argument('-o', '--output', b33 = 'outpath', help='Output file (b38: stdout)', type=argparse.FileType('w'), b38=sys.stdout)
    b31.add_argument('-l', '--max-a2', b33 = 'int', help='Max a2 of b17 (b38: infinite)', type=int, b38=None)
    b31.add_argument('-s', '--min-b18', b33 = 'float', help='Minimum b18 ratio (must be > 0, b38: 0.1)', type=float, b38=0.1)
    b31.add_argument('-c', '--min-b22', b33 = 'float', help='Minimum b22 (b38: 0.5)', type=float, b38=0.5)
    b31.add_argument('-t', '--min-b23', b33 = 'float', help='Minimum b23 (b38: 0.0)', type=float, b38=0.0)
    b31.add_argument('-f', '--out-format', b33 = 'str', help='Output format (json; b38: json)', type=str, choices=b30.keys(), b38='json')
    b34 = b31.fonk11(argv)
    b34.b35 = b30[b34.out_format]
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
    b37 = record._replace(b29=[x._asdict() for x in record.b29])
    json.dump(b37._asdict(), output_file, b38 = default_func, ensure_ascii=False)
    output_file.write(os.linesep)
def fonk15(**kwargs):
    b34 = fonk11(sys.argv[1:])
    b39 = fonk12(chain(*b34.input), b36='\t')
    b40 = fonk10(b39, b15=b34.b15, b26=b34.b26, b24=b34.b24)
    for record in b40:
        b34.b35(record, b34.output)
if b41 = = '__main__':
    fonk15()