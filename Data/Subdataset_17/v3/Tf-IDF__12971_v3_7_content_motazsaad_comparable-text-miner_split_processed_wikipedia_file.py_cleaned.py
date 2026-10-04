import sys
import os
import logging
from os.path import basename
logging.basicConfig(format='%(levelname)s : %(asctime)s : %(message)s', level=logging.INFO)
def usage():
    print('Usage:', sys.argv[0], '<corpus file> <number of parts> <output path>')
def load_textpro_module():
    import imp
    return imp.load_source('textpro', 'textpro.py')
def ensure_trailing_slash(path):
    return path if path.endswith('/') else path + '/'
def split_and_write_documents(corpus_file, num_parts, output_path, tp):
    docs = tp.split_wikipedia_docs_into_array(corpus_file)
    logging.info('Corpus is loaded')
    parts = tp.split_list(docs, num_parts)
    f_name = basename(corpus_file).split()[0]
    for i, part in enumerate(parts):
        output_file = os.path.join(output_path, f'part-{i}-{f_name}')
        with open(output_file, 'w', encoding='utf-8') as out:
            for doc in part:
                out.write(doc + '\n')
        logging.info('Part %d is done', i)
def main(argv):
    if len(argv) < 4:
        usage()
        sys.exit(2)
    tp = load_textpro_module()
    corpus_file = argv[1]
    num_parts = int(argv[2])
    output_path = ensure_trailing_slash(argv[3])
    tp.check_dir(output_path)
    split_and_write_documents(corpus_file, num_parts, output_path, tp)
if __name__ == "__main__":
    main(sys.argv)