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
        b4 = pandora.utils.load_unannotated_file(b2 + filename,
                                                            b5 = None,
                                                            b6 = False)
        b7 = b1.annotate(b4)
        b8 = b3 + filename
        fonk2(b8, b7)
    print('::: ended :::')
def fonk2(b8, b7):
    with codecs.open(b8, 'w', 'utf8') as f:
        for t, l, p in zip(b7['tokens'], b7['lemmas'], b7['pos']):
            f.write('\t'.join((t.lower(), l.lower(), p.lower())) + '\n')
if b9 = = '__main__':
    fonk1()