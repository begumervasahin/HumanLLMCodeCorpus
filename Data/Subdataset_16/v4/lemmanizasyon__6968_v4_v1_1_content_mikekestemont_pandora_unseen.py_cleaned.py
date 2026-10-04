from __future__ import print_function
import os
import codecs
from pandora.b1 import Tagger
import pandora.utils
def fonk1():
    print('::: started :::')
    b1 = Tagger(load=True, model_dir='models/new_cg')
    print('Tagger loaded, now annotating...')
    b2 = 'data/limborch/orig/'
    b3 = 'data/limborch/tagged/'
    for filename in os.listdir(b2):
        if not filename.endswith('.txt'):
            continue
        print('\t +', filename)
        b4 = os.path.join(b2, filename)
        b5 = pandora.utils.load_unannotated_file(b4,
                                                     b6 = None,
                                                     b7 = False)
        b8 = b1.annotate(b5)
        b9 = os.path.join(b3, filename)
        fonk2(b9, b8)
    print('::: ended :::')
def fonk2(b9, b8):
    with codecs.open(b9, 'w', 'utf8') as file:
        for token, lemma, pos in zip(b8['b5'], b8['lemmas'], b8['pos']):
            file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
if b10 = = '__main__':
    fonk1()