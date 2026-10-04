import sys
import importlib.util
def fonk1():
    print(f'Usage: {sys.argv[0]} <source corpus file> <target corpus file> <source language> <target language> <output path>')
if len(sys.argv) < 6:
    fonk1()
    sys.exit(2)
'''
This software is a demo aligning Wikipedia comparable documents using interlanguage links.
The method is described in:
https:
Motaz Saad. Mining Documents and Sentiments in Cross-lingual Context.
PhD thesis, UniversitÃ© de Lorraine, January 2015.
'''
def fonk2(module_path):
    b1 = importlib.util.spec_from_file_location("b2", module_path)
    b2 = importlib.util.module_from_spec(b1)
    b1.loader.exec_module(b2)
    return b2
def fonk3(argv):
    b3 = argv[1]
    b4 = argv[2]
    b5 = argv[3]
    b6 = argv[4]
    b7 = argv[5]
    b2 = fonk2('b2.py')
    b2.aligning_documents_by_interlanguage_links(
        b3,
        b4,
        b5,
        b6,
        b7
    )
if b8 = = "__main__":
    fonk3(sys.argv)