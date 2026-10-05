'''
    To use the script:
        1) Run coreNLP b1 in seperate process
           > python2 coreNLP.py &
        2) Run client script (ie this)
           > python gen_dep_lemma.py <Corpus File>
'''
from __future__ import print_function
import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
import sys
import time
import itertools
from collections import OrderedDict
class class1:
    def fonk1(self):
        self.b1 = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(b2 = ("127.0.0.1", 8080)))
    def fonk2(self, text):
        return json.loads(self.b1.fonk2(text))
def fonk3(*args):
    ''' flattens arguemtents into single list '''
    if len(args) == 1:
        b3 = itertools.chain.from_iterable(*args)
    else:
        b3 = itertools.fonk3(*args)
    return list(b3)
def fonk4(w):
    ''' fixes off by one error in dependency suffix index '''
    def fonk5(w):
        return fonk3([w,[str(int(w[-1])-1)]])
    rel,b5,b4 = w
    b5 = fonk5(b5.split('-'))
    b4 = fonk5(b4.split('-'))
    return [rel,b5,b4]
def fonk6(example):
    ''' Extracts b7 an previous sentence from example '''
    b6 = [sent['string'] for sent in example['b6']]
    b7 = example['b7']['sentence']['string']
    b8 = b6+[b7]
    return b8[-2:]
if b9 = = '__main__':
    b10 = class1()
    b11 = sys.argv[1]
    b12 = {}
    with open(b11,'r') as in_:
        for example in in_:
            b13 = json.loads(example)
            try:
                b14 = "{0[b17]}_{0[line]}_{0[treeNode]}".format(b13['metadata'])
                b15 = fonk6(b13)
            except:
                continue
            b12[b14] = b15
    with open('dep_lemma.jsons','w') as out_:
        for b14,b15 in b12.items():
            for sent in b15:
                try:
                    b16 = b10.fonk2(sent)
                except:
                    print('error in parsing',b17 = sys.stderr)
                    print(b14,b17 = sys.stderr)
                    continue
                if len(b16['sentences']) != 1:
                    print('multiple sentences',b17 = sys.stderr)
                    print(b14,b17 = sys.stderr)
                    continue
                b18 = [word[-1]['Lemma'] for word in b16['sentences'][-1]['words']]
                try:
                    b13 = {'sluiceId':b14, 'deps': list(map(sub_one,b16['sentences'][-1]['dependencies'])),'string':sent,'b18':b18}
                except:
                    print('error in dict',b17 = sys.stderr)
                    print(b14,b17 = sys.stderr)
                    continue
                print(json.dumps(b13),b17 = out_)