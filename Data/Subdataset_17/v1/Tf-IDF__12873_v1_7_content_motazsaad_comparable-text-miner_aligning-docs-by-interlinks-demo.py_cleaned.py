import sys
import importlib.util
def usage():
    print(f'Usage: {sys.argv[0]} <source corpus file> <target corpus file> <source language> <target language> <output path>')
if len(sys.argv) < 6:
    usage()
    sys.exit(2)
'''
This software is a demo aligning Wikipedia comparable documents using interlanguage links.
The method is described in:
https:
Motaz Saad. Mining Documents and Sentiments in Cross-lingual Context.
PhD thesis, UniversitÃ© de Lorraine, January 2015.
'''
def load_textpro_module(module_path):
    spec = importlib.util.spec_from_file_location("textpro", module_path)
    textpro = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(textpro)
    return textpro
def main(argv):
    source_corpus_file = argv[1]
    target_corpus_file = argv[2]
    source_language = argv[3]
    target_language = argv[4]
    output_path = argv[5]
    textpro = load_textpro_module('textpro.py')
    textpro.aligning_documents_by_interlanguage_links(
        source_corpus_file,
        target_corpus_file,
        source_language,
        target_language,
        output_path
    )
if __name__ == "__main__":
    main(sys.argv)