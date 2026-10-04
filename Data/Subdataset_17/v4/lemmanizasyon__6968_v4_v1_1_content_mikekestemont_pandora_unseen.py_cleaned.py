from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def main():
    print('::: started :::')
    tagger = Tagger(load=True, model_dir='models/new_cg')
    print('Tagger loaded, now annotating...')
    input_directory = 'data/limborch/orig/'
    output_directory = 'data/limborch/tagged/'
    for filename in os.listdir(input_directory):
        if not filename.endswith('.txt'):
            continue
        print('\t +', filename)
        input_file_path = os.path.join(input_directory, filename)
        tokens = pandora.utils.load_unannotated_file(input_file_path,
                                                     nb_instances=None,
                                                     tokenized_input=False)
        annotations = tagger.annotate(tokens)
        output_file_path = os.path.join(output_directory, filename)
        write_annotations_to_file(output_file_path, annotations)
    print('::: ended :::')
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
if __name__ == '__main__':
    main()