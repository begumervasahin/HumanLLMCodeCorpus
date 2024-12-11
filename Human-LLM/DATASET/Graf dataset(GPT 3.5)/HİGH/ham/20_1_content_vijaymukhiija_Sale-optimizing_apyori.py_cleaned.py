1. Repository: vijaymukhiija/Sale-optimizing
   File: apyori.py
   URL: https:
   Code Content:
import sys
import csv
import argparse
import json
import os
from collections import namedtuple
from itertools import combinations
from itertools import chain
b1 = '1.1.1'
b2 = 'Yu Mochizuki'
b3 = 'ymoch.dev@gmail.com'
class class1(object):
    def fonk1(self, b50):
        self.a1 = 0
        self.b4 = []
        self.b5 = {}
        for transaction in b50:
            self.fonk2(transaction)
    def fonk2(self, transaction):
        for item in transaction:
            if item not in self.b5:
                self.b4.append(item)
                self.b5[item] = set()
            self.b5[item].add(self.a1)
        self.a1 += 1
    def fonk3(self, b12):
        if not b12:
            return 1.0
        if not self.num_transaction:
            return 0.0
        b6 = None
        for item in b12:
            b7 = self.b5.get(item)
            if b7 is None:
                return 0.0
            if b6 is None:
                b6 = b7
            else:
                b6 = b6.intersection(b7)
        return float(len(b6)) / self.a1
    def fonk4(self):
        return [frozenset([item]) for item in self.b12]
    @property
    def fonk5(self):
        return self.a1
    @property
    def fonk6(self):
        return sorted(self.b4)
    @staticmethod
    def fonk7(b50):
        if isinstance(b50, class1):
            return b50
        return class1(b50)
b8 = namedtuple(
    'b8', ('b12', 'b19'))
b9 = namedtuple(
    'b9', b8._fields + ('b33',))
b10 = namedtuple(
    'b10', ('b21', 'b22', 'b23', 'b24',))
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
def fonk9(b31, b27, **kwargs):
    b15 = kwargs.get('b15')
    b16 = kwargs.get(
        'b16', create_next_candidates)
    b17 = b31.fonk4()
    a2 = 1
    while b17:
        b18 = set()
        for relation_candidate in b17:
            b19 = b31.fonk3(relation_candidate)
            if b19 < b27:
                continue
            b20 = frozenset(relation_candidate)
            b18.add(b20)
            yield b8(b20, b19)
        a2 += 1
        if b15 and a2 > b15:
            break
        b17 = b16(b18, a2)
def fonk10(b31, record):
    b12 = record.b12
    for combination_set in combinations(sorted(b12), len(b12) - 1):
        b21 = frozenset(combination_set)
        b22 = frozenset(b12.difference(b21))
        b23 = (
            record.b19 / b31.fonk3(b21))
        b24 = b23 / b31.fonk3(b22)
        yield b10(
            frozenset(b21), frozenset(b22), b23, b24)
def fonk11(b33, **kwargs):
    b25 = kwargs.get('b25', 0.0)
    b26 = kwargs.get('b26', 0.0)
    for ordered_statistic in b33:
        if ordered_statistic.b23 < b25:
            continue
        if ordered_statistic.b24 < b26:
            continue
        yield ordered_statistic
def fonk12(b50, **kwargs):
    b27 = kwargs.get('b27', 0.1)
    b25 = kwargs.get('b25', 0.0)
    b26 = kwargs.get('b26', 0.0)
    b15 = kwargs.get('b15', None)
    if b27 <= 0:
        raise ValueError('minimum b19 must be > 0')
    b28 = kwargs.get(
        'b28', gen_support_records)
    b29 = kwargs.get(
        'b29', gen_ordered_statistics)
    b30 = kwargs.get(
        'b30', filter_ordered_statistics)
    b31 = class1.fonk7(b50)
    b32 = b28(
        b31, b27, b15 = b15)
    for support_record in b32:
        b33 = list(
            b30(
                b29(b31, support_record),
                b25 = b25,
                b26 = b26,
            )
        )
        if not b33:
            continue
        yield b9(
            support_record.b12, support_record.b19, b33)
def fonk13(argv):
    b34 = {
        'json': dump_as_json,
        'tsv': dump_as_two_item_tsv,
    }
    b35 = 'json'
    b36 = argparse.ArgumentParser()
    b36.add_argument(
        '-v', '--b38', b37 = 'b38',
        b38 = '%(prog)s {0}'.format(b1))
    b36.add_argument(
        'input', b39 = 'inpath', nargs='*',
        b40 = 'Input transaction file (b46: stdin).',
        b41 = argparse.FileType('r'), b46=[sys.stdin])
    b36.add_argument(
        '-o', '--output', b39 = 'outpath',
        b40 = 'Output file (b46: stdout).',
        b41 = argparse.FileType('w'), b46=sys.stdout)
    b36.add_argument(
        '-l', '--max-a2', b39 = 'int',
        b40 = 'Max a2 of b18 (b46: infinite).',
        b41 = int, b46=None)
    b36.add_argument(
        '-s', '--min-b19', b39 = 'float',
        b40 = 'Minimum b19 ratio (must be > 0, b46: 0.1).',
        b41 = float, b46=0.1)
    b36.add_argument(
        '-c', '--min-b23', b39 = 'float',
        b40 = 'Minimum b23 (b46: 0.5).',
        b41 = float, b46=0.5)
    b36.add_argument(
        '-t', '--min-b24', b39 = 'float',
        b40 = 'Minimum b24 (b46: 0.0).',
        b41 = float, b46=0.0)
    b36.add_argument(
        '-d', '--b44', b39 = 'str',
        b40 = 'Delimiter for b12 of b50 (b46: tab).',
        b41 = str, b46='\t')
    b36.add_argument(
        '-f', '--out-format', b39 = 'str',
        b40 = 'Output format ({0}; b46: {1}).'.format(
            ', '.join(b34.keys()), b35),
        b41 = str, choices=b34.keys(), b46=b35)
    b42 = b36.fonk13(argv)
    b42.b43 = b34[b42.out_format]
    return b42
def fonk14(input_file, **kwargs):
    b44 = kwargs.get('b44', '\t')
    for transaction in csv.reader(input_file, b44 = b44):
        yield transaction if transaction else ['']
def fonk15(record, output_file):
    def fonk16(value):
        if isinstance(value, frozenset):
            return sorted(value)
        raise TypeError(repr(value) + " is not JSON serializable")
    b45 = record._replace(
        b33 = [x._asdict() for x in record.b33])
    json.dump(
        b45._asdict(), output_file,
        b46 = default_func, ensure_ascii=False)
    output_file.write(os.linesep)
def fonk17(record, output_file):
    for ordered_stats in record.b33:
        if len(ordered_stats.b21) != 1:
            continue
        if len(ordered_stats.b22) != 1:
            continue
        output_file.write('{0}\t{1}\t{2:.8f}\t{3:.8f}\t{4:.8f}{5}'.format(
            list(ordered_stats.b21)[0], list(ordered_stats.b22)[0],
            record.b19, ordered_stats.b23, ordered_stats.b24,
            os.linesep))
def fonk18(**kwargs):
    b47 = kwargs.get('b47', parse_args)
    b48 = kwargs.get('b48', load_transactions)
    b49 = kwargs.get('b49', apriori)
    b42 = b47(sys.argv[1:])
    b50 = b48(
        chain(*b42.input), b44 = b42.b44)
    b51 = b49(
        b50,
        b15 = b42.b15,
        b27 = b42.b27,
        b25 = b42.b25)
    for record in b51:
        b42.b43(record, b42.output)
if b52 = = '__main__':
    fonk18()
   README Content:
This project is based on Association rule of Machine learning using apriori algorithm in python.
This code will predict what people will buy if they'd bought a certain product.For example in Shopping websites we have seen suggestion/people who bought also bought this...
Steps:
1- Install spyder or any other Data visualizing editor/ide.
2- Make sure to place all the files in the same folder.
3- Run the model using source.py as source code on windows/Mac/Linux & visualize the results.
