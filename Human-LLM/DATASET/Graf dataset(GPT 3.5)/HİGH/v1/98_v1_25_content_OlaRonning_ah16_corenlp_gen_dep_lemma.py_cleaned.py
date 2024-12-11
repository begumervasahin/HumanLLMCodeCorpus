from __future__ import print_function
import json
import sys
from stanfordnlp.server import CoreNLPClient
from pprint import pprint
def fonk1(w):
    ''' fixes off by one error in dependency suffix index '''
    def fonk2(w):
        return [w[0], str(int(w[1])-1)]
    rel, b2, b1 = w
    b2 = fonk2(b2.split('-'))
    b1 = fonk2(b1.split('-'))
    return [rel, b2, b1]
def fonk3(example):
    ''' Extracts b4 and previous sentence from example '''
    b3 = [sent['string'] for sent in example['b3']]
    b4 = example['b4']['sentence']['string']
    b5 = b3 + [b4]
    return b5[-2:]
if b6 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python gen_dep_lemma.py <Corpus File>")
        sys.exit(1)
    with CoreNLPClient(b7 = ['tokenize','ssplit','pos','lemma','depparse'], timeout=60000, memory='16G') as client:
        b8 = sys.argv[1]
        b9 = {}
        with open(b8,'r') as in_:
            for example in in_:
                b10 = json.loads(example)
                try:
                    b11 = "{0[b13]}_{0[line]}_{0[treeNode]}".format(b10['metadata'])
                    b12 = fonk3(b10)
                except Exception as e:
                    print(f"Error: {e}", b13 = sys.stderr)
                    continue
                b9[b11] = b12
        with open('dep_lemma.jsons','w') as out_:
            for b11, b12 in b9.items():
                for sent in b12:
                    try:
                        b14 = client.annotate(sent)
                        b15 = [word.lemma for sent in b14.sentences for word in sent.words]
                        b10 = {'sluiceId': b11, 'deps': [fonk1(dep) for dep in b14.dependencies], 'string': sent, 'b15': b15}
                        print(json.dumps(b10), b13 = out_)
                    except Exception as e:
                        print(f"Error: {e}", b13 = sys.stderr)
                        continue