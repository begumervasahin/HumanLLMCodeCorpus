from __future__ import print_function
import os
import codecs
from pandora.b1 import Tagger
import pandora.utils
def fonk1():
    print('::: Annotation Process Started :::')
    b1 = Tagger(load=True, model_dir='models/new_cg')
    print('Tagger loaded. Now, annotating...')
    b2 = 'data/limborch/orig/'
    b3 = 'data/limborch/tagged/'
    for filename in os.listdir(b2):
        if not filename.endswith('.txt'):
            continue
        print('\t + Annotating', filename)
        b4 = pandora.utils.load_unannotated_file(
            os.path.join(b2, filename),
            b5 = None,
            b6 = False
        )
        b7 = b1.annotate(b4)
        b8 = os.path.join(b3, filename)
        fonk2(b8, b7)
    print('::: Annotation Process Ended :::')
def fonk2(b8, b7):
    with codecs.open(b8, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(b7['tokens'], b7['lemmas'], b7['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
if b9 = = '__main__':
    fonk1()