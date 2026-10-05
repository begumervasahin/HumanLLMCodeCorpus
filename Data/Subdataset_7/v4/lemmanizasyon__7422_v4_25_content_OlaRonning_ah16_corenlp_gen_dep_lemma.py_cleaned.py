from __future__ import print_function
import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
import sys
import itertools
from pprint import pprint
from collections import OrderedDict
class class1:
    def fonk1(self):
        self.b1 = ServerProxy(JsonRpc20(), TransportTcpIp(addr=("127.0.0.1", 8080)))
    def fonk2(self, text):
        return json.loads(self.b1.fonk2(text))
def fonk3(*args):
    if len(args) == 1:
        b2 = itertools.chain.from_iterable(*args)
    else:
        b2 = itertools.fonk3(*args)
    return list(b2)
def fonk4(w):
    def fonk5(w):
        return fonk3([w, [str(int(w[-1]) - 1)]])
    rel, b4, b3 = w
    b4 = fonk5(b4.split('-'))
    b3 = fonk5(b3.split('-'))
    return [rel, b4, b3]
def fonk6(example):
    b5 = [sent['string'] for sent in example['b5']]
    b6 = example['b6']['sentence']['string']
    b7 = b5 + [b6]
    return b7[-2:]
if b8 = = '__main__':
    b9 = class1()
    b10 = sys.argv[1]
    b11 = {}
    with open(b10, 'r') as in_:
        for example in in_:
            b12 = json.loads(example)
            try:
                b13 = "{0[b16]}_{0[line]}_{0[treeNode]}".format(b12['metadata'])
                b14 = fonk6(b12)
            except:
                continue
            b11[b13] = b14
    with open('dep_lemma.jsons', 'w') as out_:
        for b13, b14 in b11.items():
            for sent in b14:
                try:
                    b15 = b9.fonk2(sent)
                except:
                    print('error in parsing', b16 = sys.stderr)
                    print(b13, b16 = sys.stderr)
                    continue
                if len(b15['sentences']) != 1:
                    print('multiple sentences', b16 = sys.stderr)
                    print(b13, b16 = sys.stderr)
                    continue
                b17 = [word[-1]['Lemma'] for word in b15['sentences'][-1]['words']]
                try:
                    b12 = {'sluiceId': b13, 'deps': list(map(sub_one, b15['sentences'][-1]['dependencies'])), 'string': sent, 'b17': b17}
                except:
                    print('error in dict', b16 = sys.stderr)
                    print(b13, b16 = sys.stderr)
                    continue
                print(json.dumps(b12), b16 = out_)