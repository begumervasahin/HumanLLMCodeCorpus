from __future__ import print_function
import os
import codecs
from pandora.b7 import Tagger
import pandora.utils
def fonk1():
    print('::: Loading Tagger Model :::')
    return Tagger(b1 = True, model_dir='models/new_cg')
def fonk2(b7, b8, b9, filename):
    print('\t + Annotating', filename)
    b2 = pandora.utils.load_unannotated_file(
        os.path.join(b8, filename),
        b3 = None,
        b4 = False
    )
    b5 = b7.annotate(b2)
    b6 = os.path.join(b9, filename)
    fonk3(b6, b5)
def fonk3(b6, b5):
    with codecs.open(b6, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(b5['tokens'], b5['lemmas'], b5['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
def fonk4():
    print('::: Annotation Started :::')
    b7 = fonk1()
    print('::: Tagger loaded, now annotating :::')
    b8 = 'data/limborch/orig/'
    b9 = 'data/limborch/tagged/'
    for filename in os.listdir(b8):
        if filename.endswith('.txt'):
            fonk2(b7, b8, b9, filename)
    print('::: Annotation Ended :::')
if b10 = = '__main__':
    fonk4()