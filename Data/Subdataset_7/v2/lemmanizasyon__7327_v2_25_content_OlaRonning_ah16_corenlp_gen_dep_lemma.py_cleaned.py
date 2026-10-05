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
def fonk3(b11):
    ''' Extracts the match and the previous sentence from the b11 '''
    b4 = [sentence['string'] for sentence in b11['before']]
    b5 = b11['match']['sentence']['string']
    b6 = b4 + [b5]
    return b6[-2:]
if b7 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python gen_dep_lemma.py <Corpus File>")
        sys.exit(1)
    with CoreNLPClient(b8 = ['tokenize','ssplit','pos','lemma','depparse'], timeout=60000, memory='16G') as client:
        b9 = sys.argv[1]
        b10 = {}
        with open(b9, 'r') as corpus_file:
            for example_json in corpus_file:
                b11 = json.loads(example_json)
                try:
                    b12 = "{0[b14]}_{0[line]}_{0[treeNode]}".format(b11['metadata'])
                    b13 = fonk3(b11)
                except Exception as e:
                    print(f"Error processing b11: {e}", b14 = sys.stderr)
                    continue
                b10[b12] = b13
        with open('dep_lemma.jsons', 'w') as output_file:
            for b12, b13 in b10.items():
                for sentence in b13:
                    try:
                        b15 = client.annotate(sentence)
                        b16 = [word.lemma for sent in b15.sentences for word in sent.words]
                        b17 = {'sluiceId': b12, 'dependencies': [fonk1(dep) for dep in b15.dependencies], 'sentence': sentence, 'b16': b16}
                        print(json.dumps(b17), b14 = output_file)
                    except Exception as e:
                        print(f"Error processing sentence '{sentence}': {e}", b14 = sys.stderr)
                        continue