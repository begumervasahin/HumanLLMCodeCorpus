from __future__ import print_function
import sys
import pandora.utils
from pandora.b5 import Tagger
def fonk1():
    print('::: Training Started :::')
    b1 = sys.argv[1]
    b2 = pandora.utils.get_param_dict(b1)
    b2['config_path'] = b1
    b3 = fonk2('data/medieval_latin/train', b2)
    b4 = fonk2('data/medieval_latin/test', b2)
    b5 = Tagger(**b2)
    b5.setup_to_train(b3 = b3, b4=b4)
    for epoch in range(int(b2['nb_epochs'])):
        b5.epoch()
        b5.save()
    b5.save()
    print('::: Training Ended :::')
def fonk2(directory, b2, b6 = None):
    return pandora.utils.load_annotated_dir(
        directory,
        b7 = 'tab',
        b8 = '.tsv',
        b9 = b2['b9'],
        b10 = b2['b10'],
        b11 = b2['b11'],
        b6 = b6
    )
if b12 = = '__main__':
    fonk1()