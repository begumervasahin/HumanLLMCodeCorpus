from __future__ import print_function
import os
import codecs
from pandora.tagger import Tagger
import pandora.utils
def load_tagger_model(model_directory='models/new_cg'):
    print('::: Loading Tagger Model :::')
    return Tagger(load=True, model_dir=model_directory)
def annotate_file(tagger, input_directory, output_directory, filename):
    print(f'\t + Annotating {filename}')
    unseen_tokens = pandora.utils.load_unannotated_file(
        os.path.join(input_directory, filename),
        nb_instances=None,
        tokenized_input=False
    )
    annotations = tagger.annotate(unseen_tokens)
    output_file_path = os.path.join(output_directory, filename)
    write_annotations_to_file(output_file_path, annotations)
def write_annotations_to_file(output_file_path, annotations):
    with codecs.open(output_file_path, 'w', 'utf8') as output_file:
        for token, lemma, pos in zip(annotations['tokens'], annotations['lemmas'], annotations['pos']):
            output_file.write('\t'.join((token.lower(), lemma.lower(), pos.lower())) + '\n')
def main():
    print('::: Annotation Started :::')
    tagger = load_tagger_model()
    print('::: Tagger loaded, now annotating :::')
    input_directory = 'data/limborch/orig/'
    output_directory = 'data/limborch/tagged/'
    os.makedirs(output_directory, exist_ok=True)
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            annotate_file(tagger, input_directory, output_directory, filename)
    print('::: Annotation Ended :::')
if __name__ == '__main__':
    main()