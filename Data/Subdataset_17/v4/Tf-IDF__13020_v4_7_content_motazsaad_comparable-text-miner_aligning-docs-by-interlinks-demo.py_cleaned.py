import sys
from multiprocessing import Process
import imp
def usage():
    print('Usage: ', sys.argv[0], '<source corpus file> <target corpus file> <source language> <target language> <output path>')
def main(argv):
    if len(argv) < 6:
        usage()
        sys.exit(2)
    source_corpus_file = argv[1]
    target_corpus_file = argv[2]
    source_language = argv[3]
    target_language = argv[4]
    output_path = argv[5]
    textpro = imp.load_source('textpro', 'textpro.py')
    textpro.aligning_documents_by_interlanguage_links(source_corpus_file, target_corpus_file, source_language, target_language, output_path)
import sys
from multiprocessing import Process
import imp
def usage():
    print('Usage: ', sys.argv[0], '<source corpus file> <target corpus file> <source language> <target language> <output path>')
def main(argv):
    if len(argv) < 6:
        usage()
        sys.exit(2)
    source_corpus_file = argv[1]
    target_corpus_file = argv[2]
    source_language = argv[3]
    target_language = argv[4]
    output_path = argv[5]
    textpro = imp.load_source('textpro', 'textpro.py')
    textpro.aligning_documents_by_interlanguage_links(source_corpus_file, target_corpus_file, source_language, target_language, output_path)
if __name__ == "__main__":
    main(sys.argv)
if __name__ == "__main__":
    main(sys.argv)q