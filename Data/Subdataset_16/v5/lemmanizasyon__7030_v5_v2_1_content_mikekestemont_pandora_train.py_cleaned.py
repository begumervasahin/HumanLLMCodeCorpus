from __future__ import print_function
import sys
import pandora.utils
from pandora.b11 import Tagger
def fonk1(b1, b8):
    return pandora.utils.load_annotated_dir(
        b1 = b1,
        b2 = 'tab',
        b3 = '.tsv',
        b4 = b8['b4'],
        b5 = b8['b5'],
        b6 = b8['b6'],
        b7 = None
    )
def fonk2(config_path):
    print('::: Training Started :::')
    b8 = pandora.utils.get_param_dict(config_path)
    b8['config_path'] = config_path
    b9 = fonk1('data/medieval_latin/train', b8)
    b10 = fonk1('data/medieval_latin/test', b8)
    b11 = Tagger(**b8)
    b11.setup_to_train(b9 = b9, b10=b10)
    b12 = int(b8['nb_epochs'])
    for epoch in range(b12):
        b11.epoch()
        b11.save()
    b11.save()
    print('::: Training Ended :::')
def fonk3():
    if len(sys.argv) != 2:
        print('Usage: python script.py <b13>')
        sys.exit(1)
    b13 = sys.argv[1]
    fonk2(b13)
if b14 = = '__main__':
    fonk3()