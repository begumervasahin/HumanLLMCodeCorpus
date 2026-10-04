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
    create_directory_if_not_exists(output_dir)
    for filename in get_txt_files(input_dir):
        print(f'\t + Annotating {filename}')
        input_file_path = os.path.join(input_dir, filename)
        tokens = load_unannotated_data(input_file_path)
        annotations = tagger.annotate(tokens)
        output_file_path = os.path.join(output_dir, filename)
        write_annotations_to_file(output_file_path, annotations)
    print('::: Annotation Ended :::')
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def get_txt_files(directory):
    return [filename for filename in os.listdir(directory) if filename.endswith('.txt')]
def load_unannotated_data(file_path):
    return pandora.utils.load_unannotated_file(
        file_path,
        nb_instances=None,
        tokenized_input=False
    )
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
if __name__ == '__main__':
    main()