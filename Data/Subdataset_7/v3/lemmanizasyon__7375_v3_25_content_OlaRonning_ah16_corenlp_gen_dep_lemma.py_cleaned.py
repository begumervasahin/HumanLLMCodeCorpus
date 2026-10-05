from __future__ import print_function
import json
import sys
from stanfordnlp.server import CoreNLPClient
def fonk1(dependency):
    ''' Fixes off-by-one error in dependency suffix index '''
    def fonk2(index):
        return [index[0], str(int(index[1]) - 1)]
    relation, index1, b1 = dependency
    b2 = fonk2(index1.split('-'))
    b3 = fonk2(b1.split('-'))
    return [relation, b2, b3]
def fonk3(b12):
    ''' Extracts the match and the previous sentence from the b12 '''
    b4 = [sentence['string'] for sentence in b12['before']]
    b5 = b12['match']['sentence']['string']
    b6 = b4 + [b5]
    return b6[-2:]
if b7 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python gen_dep_lemma.py <Corpus File>", b8 = sys.stderr)
        sys.exit(1)
    with CoreNLPClient(b9 = ['tokenize','ssplit','pos','lemma','depparse'], timeout=60000, memory='16G') as client:
        b10 = sys.argv[1]
        b11 = {}
        with open(b10, 'r') as corpus_file:
            for example_json in corpus_file:
                b12 = json.loads(example_json)
                try:
                    b13 = "{0[b8]}_{0[line]}_{0[treeNode]}".format(b12['metadata'])
                    b14 = fonk3(b12)
                except Exception as e:
                    print(f"Error processing b12: {e}", b8 = sys.stderr)
                    continue
                b11[b13] = b14
        b15 = 'dep_lemma.jsons'
        with open(b15, 'w') as output_file:
            for b13, b14 in b11.items():
                for sentence in b14:
                    try:
                        b16 = client.annotate(sentence)
                        b17 = [word.lemma for sent in b16.sentences for word in sent.words]
                        b18 = {'sluiceId': b13, 'dependencies': [fonk1(dep) for dep in b16.dependencies], 'sentence': sentence, 'b17': b17}
                        print(json.dumps(b18), b8 = output_file)
                    except Exception as e:
                        print(f"Error processing sentence '{sentence}': {e}", b8 = sys.stderr)
                        continue