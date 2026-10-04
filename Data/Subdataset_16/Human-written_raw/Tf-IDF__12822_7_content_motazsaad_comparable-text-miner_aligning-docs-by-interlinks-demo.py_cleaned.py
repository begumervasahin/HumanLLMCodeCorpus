import sys
from multiprocessing import Process
def fonk1():
	print 'Usage: ', sys.argv[0], '<source corpus file> <target corpus file> <source language> <target language> <output path>'
if len(sys.argv) < 6: fonk1(); sys.exit(2)
'''
This software is a demo aligning wikipeida comparable documents using interlanguage links. The method is described in
https:
Motaz Saad. Mining Documents and Sentiments in Cross-lingual Context. PhD thesis, UniversitÃ© de Lorraine, January 2015.
'''
import imp
b1 = imp.load_source('textpro', 'textpro.py')
def fonk2(argv):
	b2 = sys.argv[1]
	b3 = sys.argv[2]
	b4 = sys.argv[3]
	b5 = sys.argv[4]
	b6 = sys.argv[5]
	b1.aligning_documents_by_interlanguage_links(b2, b3, b4, b5, b6)
if b7 = = "__main__":
	fonk2(sys.argv)