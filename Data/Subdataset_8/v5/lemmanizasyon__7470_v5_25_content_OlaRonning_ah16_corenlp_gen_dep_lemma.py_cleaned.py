from __future__ import print_function
import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
import sys
import itertools
from pprint import pprint
from collections import OrderedDict
class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(), TransportTcpIp(addr=("127.0.0.1", 8080)))
    def parse(self, text):
        return json.loads(self.server.parse(text))
def chain(*args):
    if len(args) == 1:
        l = itertools.chain.from_iterable(*args)
    else:
        l = itertools.chain(*args)
    return list(l)
def adjust_dependency_index(w):
    def adjust(w):
        return chain([w, [str(int(w[-1]) - 1)]])
    rel, w1, w2 = w
    w1 = adjust(w1.split('-'))
    w2 = adjust(w2.split('-'))
    return [rel, w1, w2]
def extract_sentences(example):
    before = [sent['string'] for sent in example['before']]
    match = example['match']['sentence']['string']
    candidates = before + [match]
    return candidates[-2:]
if __name__ == '__main__':
    nlp = StanfordNLP()
    anno_path = sys.argv[1]
    anno_data = {}
    with open(anno_path, 'r') as in_file:
        for example in in_file:
            dict_ = json.loads(example)
            try:
                sluice_id = "{0[file]}_{0[line]}_{0[treeNode]}".format(dict_['metadata'])
                article = extract_sentences(dict_)
            except:
                continue
            anno_data[sluice_id] = article
    with open('dep_lemma.jsons', 'w') as out_file:
        for sluice_id, article in anno_data.items():
            for sent in article:
                try:
                    result = nlp.parse(sent)
                except:
                    print('Error in parsing', file=sys.stderr)
                    print(sluice_id, file=sys.stderr)
                    continue
                if len(result['sentences']) != 1:
                    print('Multiple sentences', file=sys.stderr)
                    print(sluice_id, file=sys.stderr)
                    continue
                lemmas = [word[-1]['Lemma'] for word in result['sentences'][-1]['words']]
                try:
                    dict_ = {
                        'sluiceId': sluice_id,
                        'deps': list(map(adjust_dependency_index, result['sentences'][-1]['dependencies'])),
                        'string': sent,
                        'lemmas': lemmas
                    }
                except:
                    print('Error in dictionary construction', file=sys.stderr)
                    print(sluice_id, file=sys.stderr)
                    continue
                print(json.dumps(dict_), file=out_file)