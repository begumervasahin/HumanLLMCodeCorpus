from __future__ import print_function
import json
import sys
from stanfordnlp.server import CoreNLPClient
from pprint import pprint
def sub_one(w):
    ''' fixes off by one error in dependency suffix index '''
    def f(w):
        return [w[0], str(int(w[1])-1)]
    rel, w1, w2 = w
    w1 = f(w1.split('-'))
    w2 = f(w2.split('-'))
    return [rel, w1, w2]
def get_article(example):
    ''' Extracts match and previous sentence from example '''
    before = [sent['string'] for sent in example['before']]
    match = example['match']['sentence']['string']
    candidates = before + [match]
    return candidates[-2:]
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python gen_dep_lemma.py <Corpus File>")
        sys.exit(1)
    with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','depparse'], timeout=60000, memory='16G') as client:
        anno_path = sys.argv[1]
        anno_data = {}
        with open(anno_path,'r') as in_:
            for example in in_:
                dict_ = json.loads(example)
                try:
                    sluice_id = "{0[file]}_{0[line]}_{0[treeNode]}".format(dict_['metadata'])
                    article = get_article(dict_)
                except Exception as e:
                    print(f"Error: {e}", file=sys.stderr)
                    continue
                anno_data[sluice_id] = article
        with open('dep_lemma.jsons','w') as out_:
            for sluice_id, article in anno_data.items():
                for sent in article:
                    try:
                        result = client.annotate(sent)
                        lemmas = [word.lemma for sent in result.sentences for word in sent.words]
                        dict_ = {'sluiceId': sluice_id, 'deps': [sub_one(dep) for dep in result.dependencies], 'string': sent, 'lemmas': lemmas}
                        print(json.dumps(dict_), file=out_)
                    except Exception as e:
                        print(f"Error: {e}", file=sys.stderr)
                        continue