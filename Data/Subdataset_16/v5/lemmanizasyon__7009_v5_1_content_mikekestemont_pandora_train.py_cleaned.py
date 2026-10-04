from __future__ import print_function
import sys
import pandora.utils
from pandora.b11 import Tagger
def fonk1(data_dir, b8):
    return pandora.utils.load_annotated_dir(
        data_dir,
        b1 = 'tab',
        b2 = '.tsv',
        b3 = b8['b3'],
        b4 = b8['b4'],
        b5 = b8['b5'],
        b6 = None
    )
def fonk2():
    print('::: started :::')
    b7 = sys.argv[1]
    b8 = pandora.utils.get_param_dict(b7)
    b8['config_path'] = b7
    b9 = fonk1('data/medieval_latin/train', b8)
    b10 = fonk1('data/medieval_latin/test', b8)
    b11 = Tagger(**b8)
    b11.setup_to_train(b9 = b9, b10=b10)
    b12 = int(b8['nb_epochs'])
    for epoch in range(b12):
        b11.epoch()
        b11.save()
    b11.save()
    print('::: ended :::')
if b13 = = '__main__':
    fonk2()