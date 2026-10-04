from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def main():
    print('::: Annotation Started :::')
    tagger = Tagger(load=True, model_dir='models/new_cg')
    print('Tagger loaded, now annotating...')
    input_dir = 'data/limborch/orig/'
    output_dir = 'data/limborch/tagged/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if not filename.endswith('.txt'):
            continue
        print(f'\t + Annotating {filename}')
        input_file_path = os.path.join(input_dir, filename)
        tokens = pandora.utils.load_unannotated_file(
            input_file_path,
            nb_instances=None,
            tokenized_input=False
        )
        annotations = tagger.annotate(tokens)
        output_file_path = os.path.join(output_dir, filename)
        write_annotations_to_file(output_file_path, annotations)
    print('::: Annotation Ended :::')
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
if __name__ == '__main__':
    main()