from __future__ import print_function
import sys
import pandora.utils
from pandora.b11 import Tagger
import os
import codecs
def fonk1():
    print('::: started :::')
    b1 = sys.argv[1]
    b2 = pandora.utils.get_param_dict(b1)
    b2['config_path'] = b1
    b3 = pandora.utils.load_annotated_dir(
        'data/medieval_latin/train',
        b4 = 'tab',
        b5 = '.tsv',
        b6 = b2['b6'],
        b7 = b2['b7'],
        b8 = b2['b8'],
        b9 = None
    )
    b10 = pandora.utils.load_annotated_dir(
        'data/medieval_latin/test',
        b4 = 'tab',
        b5 = '.tsv',
        b6 = b2['b6'],
        b7 = b2['b7'],
        b8 = b2['b8'],
        b9 = None
    )
    b11 = Tagger(**b2)
    b11.setup_to_train(b3 = b3, b10=b10)
    b12 = int(b2['nb_epochs'])
    for epoch in range(b12):
        b11.epoch()
        b11.save()
    b11.save()
    print('::: ended :::')
if b13 = = '__main__':
    fonk1()