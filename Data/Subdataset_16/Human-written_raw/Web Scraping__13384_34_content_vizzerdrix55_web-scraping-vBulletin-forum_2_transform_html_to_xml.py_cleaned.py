import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import codecs
import logging
logging.basicConfig(b1 = 'xml-transformation.log',
                    b2 = 'w',
                    b3 = '%(asctime)s %(message)s',
                    b4 = logging.WARNING)
logging.critical('start')
b5 = ''
b6 = os.fsencode(b5)
b7 = []
for file in os.listdir(b6):
    b1 = os.fsdecode(file)
    if b1.endswith(".html"):
        b7.append(os.path.join(b5, b1))
    else:
        logging.error('skipped file that ends not with .html: %s' % file)
for file in b7:
    try:
        with codecs.open(file, 'r', 'utf-8') as f:
            b8 = f.read()
    except:
        logging.error('skipped %s because of UnicodeDecodeError' % file)
    else:
        b9 = BeautifulSoup(b8, 'lxml')
        b10 = b9.find_all('li', ['postbit'])
        if b10:
            logging.info('HTML structure for b10 successfully checked')
        else:
            logging.error('other HTML structure than expected',
                          'for b10')
        b11 = ET.Element('b11')
        for post in b10:
            b12 = ET.SubElement(b11, 'post')
            b13 = post.find('div',['datetime'])
            if b13:
                ET.SubElement(b12, 'b13').b14 = b13.get_text()
            else:
                logging.error('no HTML structure found for b13')
            b15 = post.find('div',['b15'])
            if b15:
                ET.SubElement(b12, 'b15').b14 = b15.get_text()
            else:
                logging.error('no HTML structure found for b15')
            b16 = post.find('span',['b16'])
            if b16:
                ET.SubElement(b12, 'b16').b14 = b16.get_text()
            else:
                logging.error('no HTML structure found for b16')
            b17 = post.find('blockquote',['restore'])
            if b17:
                b18 = b17.find_all('div', ['bbcode_quote'])
                for bbcode in b18:
                    bbcode.decompose()
                ET.SubElement(b12, 'b17').b14 = b17.get_text()
            else:
                logging.error('no HTML structure found for b17')
    b19 = ET.ElementTree(b11)
    b19.write('%s.xml' % file,)
    logging.critical('saved file %s.xml' % file)
logging.critical('end')