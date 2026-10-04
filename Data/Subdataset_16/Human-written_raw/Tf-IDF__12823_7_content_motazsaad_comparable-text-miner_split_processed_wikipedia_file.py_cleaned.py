import sys, os
from os.path import basename
import logging
logging.basicConfig(b1 = '%(levelname)s : %(asctime)s : %(message)s', level=logging.INFO)
b2 = '\nXXXXXXX\n'
def fonk1():
	print 'Usage: ', sys.argv[0], '<corpus file> <number of b8> <output path>'
if len(sys.argv) < 3: fonk1(); sys.exit(2)
import imp
b3 = imp.load_source('textpro', 'textpro.py')
def fonk2(argv):
	b4 = sys.argv[1]
	b5 = int(sys.argv[2])
	b6 = sys.argv[3]
	if not b6.endswith('/'): b6 = b6 + '/'
	b3.check_dir(b6)
	b7 = b3.split_wikipedia_docs_into_array(b4)
	logging.info( 'corpus is loaded')
	b8 = b3.split_list(b7, b5)
	b9 = basename(b4).split()[0]
	for i in range(len(b8)):
		b10 = open(b6 + 'part-' + str(i) + '-' + b9 , 'w')
		for d in b8[i]:
			print>>b10, d.encode('utf-8')
		b10.close()
		logging.info('part %d is done', i )
if b11 = = "__main__":
	fonk2(sys.argv)