import sys
import os
from os.path import basename
import logging
logging.basicConfig(format='%(levelname)s : %(asctime)s : %(message)s', level=logging.INFO)
X_SEPARATOR = '\nXXXXXXX\n'
def usage():
    print(f'Usage: {sys.argv[0]} <corpus file> <number of parts> <output path>')
def load_textpro_module():
    import imp
    return imp.load_source('textpro', 'textpro.py')
def ensure_output_path(output_path):
    return output_path if output_path.endswith('/') else output_path + '/'
def write_parts_to_files(parts, output_path, base_name):
    for i, part in enumerate(parts):
        output_filename = os.path.join(output_path, f'part-{i}-{base_name}')
        with open(output_filename, 'w', encoding='utf-8') as out_file:
            for doc in part:
                out_file.write(f'{doc}\n')
        logging.info(f'Part {i} is done')
def main(argv):
    if len(argv) < 4:
        usage()
        sys.exit(2)
    tp = load_textpro_module()
    corpus_file = argv[1]
    num_parts = int(argv[2])
    output_path = ensure_output_path(argv[3])
    tp.check_dir(output_path)
    docs = tp.split_wikipedia_docs_into_array(corpus_file)
    logging.info('Corpus is loaded')
    parts = tp.split_list(docs, num_parts)
    base_name = basename(corpus_file).split()[0]
    write_parts_to_files(parts, output_path, base_name)
if __name__ == "__main__":
    main(sys.argv)