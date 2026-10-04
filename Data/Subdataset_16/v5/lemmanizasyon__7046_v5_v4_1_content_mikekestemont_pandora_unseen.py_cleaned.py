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
        if filename.endswith('.txt'):
            print(f'\t + Annotating {filename}')
            fonk2(b1, b2, b3, filename)
    print('::: Annotation Process Ended :::')
def fonk2(b1, b2, b3, filename):
    b4 = os.path.join(b2, filename)
    b5 = pandora.utils.load_unannotated_file(
        b4,
        b6 = None,
        b7 = False
    )
    b8 = b1.annotate(b5)
    b9 = os.path.join(b3, filename)
    fonk3(b9, b8)
def fonk3(b9, b8):
    with codecs.open(b9, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(b8['tokens'], b8['lemmas'], b8['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
if b10 = = '__main__':
    fonk1()