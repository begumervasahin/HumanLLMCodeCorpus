from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def main():
    print('::: started :::')
    tagger = load_tagger_model('models/new_cg')
    print('Tagger loaded, now annotating...')
    input_directory = 'data/limborch/orig/'
    output_directory = 'data/limborch/tagged/'
    os.makedirs(output_directory, exist_ok=True)
    process_files_in_directory(input_directory, output_directory, tagger)
    print('::: ended :::')
def load_tagger_model(model_directory):
    return Tagger(load=True, model_dir=model_directory)
def process_files_in_directory(input_directory, output_directory, tagger):
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            process_file(input_directory, output_directory, filename, tagger)
def process_file(input_directory, output_directory, filename, tagger):
    print(f'\t + {filename}')
    unannotated_data = load_unannotated_data(os.path.join(input_directory, filename))
    annotations = tagger.annotate(unannotated_data)
    output_file_path = os.path.join(output_directory, filename)
    write_annotations_to_file(output_file_path, annotations)
def load_unannotated_data(file_path):
    return pandora.utils.load_unannotated_file(
        file_path,
        nb_instances=None,
        tokenized_input=False
    )
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
if __name__ == '__main__':
    main()