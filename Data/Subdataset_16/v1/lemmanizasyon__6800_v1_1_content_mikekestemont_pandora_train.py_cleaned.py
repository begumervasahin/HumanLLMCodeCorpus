from __future__ import print_function
import sys
import pandora.utils
from pandora.b10 import Tagger
import os, codecs
def fonk1(cf_path):
    print('::: started :::')
    b1 = pandora.utils.get_param_dict(cf_path)
    b1['config_path'] = cf_path
    b2 = pandora.utils.load_annotated_dir(
        'data/medieval_latin/train',
        b3 = 'tab',
        b4 = '.tsv',
        b5 = b1['b5'],
        b6 = b1['b6'],
        b7 = b1['b7'],
        b8 = None
    )
    b9 = pandora.utils.load_annotated_dir(
        'data/medieval_latin/test',
        b3 = 'tab',
        b4 = '.tsv',
        b5 = b1['b5'],
        b6 = b1['b6'],
        b7 = b1['b7'],
        b8 = None
    )
    b10 = Tagger(**b1)
    b10.setup_to_train(b2 = b2, b9=b9)
    for i in range(int(b1['nb_epochs'])):
        b10.epoch()
        b10.save()
    b10.save()
    print('::: ended :::')
if b11 = = '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_path>")
    else:
        fonk1(sys.argv[1])