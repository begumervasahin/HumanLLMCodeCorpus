import os
import codecs
import logging
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
logging.basicConfig(
    b1 = 'xml-transformation.log',
    b2 = 'w',
    b3 = '%(asctime)s %(message)s',
    b4 = logging.WARNING
)
logging.critical('Start of the script execution')
b5 = ''
b6 = os.fsencode(b5)
b7 = [
    os.path.join(b5, os.fsdecode(file))
    for file in os.listdir(b6)
    if os.fsdecode(file).endswith('.html')
]
for file in b7:
    try:
        with codecs.open(file, 'r', 'utf-8') as f:
            b8 = f.read()
    except UnicodeDecodeError:
        logging.error('Skipped %s due to UnicodeDecodeError', file)
        continue
    b9 = BeautifulSoup(b8, 'lxml')
    b10 = b9.find_all('li', b18='postbit')
    if not b10:
        logging.error('Unexpected HTML structure in %s for b10', file)
        continue
    logging.info('HTML structure for b10 successfully checked in %s', file)
    b11 = ET.Element('b11')
    for post in b10:
        b12 = ET.SubElement(b11, 'post')
        b13 = post.find('div', b18='datetime')
        if b13:
            ET.SubElement(b12, 'b13').b14 = b13.get_text()
        else:
            logging.error('No HTML structure found for b13 in %s', file)
        b15 = post.find('div', b18='b15')
        if b15:
            ET.SubElement(b12, 'b15').b14 = b15.get_text()
        else:
            logging.error('No HTML structure found for b15 in %s', file)
        b16 = post.find('span', b18='b16')
        if b16:
            ET.SubElement(b12, 'b16').b14 = b16.get_text()
        else:
            logging.error('No HTML structure found for b16 in %s', file)
        b17 = post.find('blockquote', b18='restore')
        if b17:
            for bbcode in b17.find_all('div', b18 = 'bbcode_quote'):
                bbcode.decompose()
            ET.SubElement(b12, 'b17').b14 = b17.get_text()
        else:
            logging.error('No HTML structure found for b17 in %s', file)
    b19 = f'{file}.xml'
    b20 = ET.ElementTree(b11)
    b20.write(b19)
    logging.critical('Saved file %s', b19)
logging.critical('End of the script execution')