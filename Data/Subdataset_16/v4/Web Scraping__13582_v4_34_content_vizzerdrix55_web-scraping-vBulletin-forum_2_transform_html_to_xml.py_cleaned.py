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
logging.critical('Start of processing')
b5 = ''
b6 = os.fsencode(b5)
b7 = []
for file in os.listdir(b6):
    b1 = os.fsdecode(file)
    if b1.endswith(".html"):
        b7.append(os.path.join(b5, b1))
    else:
        logging.error(f'Skipped non-HTML file: {b1}')
for file in b7:
    try:
        with codecs.open(file, 'r', 'utf-8') as f:
            b8 = f.read()
    except UnicodeDecodeError:
        logging.error(f'Skipped {file} due to UnicodeDecodeError')
        continue
    b9 = BeautifulSoup(b8, 'lxml')
    b10 = b9.find_all('li', class_='postbit')
    if not b10:
        logging.error(f'Unexpected HTML structure for b10 in {file}')
        continue
    b11 = ET.Element('b11')
    for post in b10:
        b12 = ET.SubElement(b11, 'post')
        b13 = post.find('div', class_='datetime')
        if b13:
            ET.SubElement(b12, 'b13').b14 = b13.get_text()
        else:
            logging.error('No HTML structure found for b13')
        b15 = post.find('div', class_='b15')
        if b15:
            ET.SubElement(b12, 'b15').b14 = b15.get_text()
        else:
            logging.error('No HTML structure found for b15')
        b16 = post.find('span', class_='b16')
        if b16:
            ET.SubElement(b12, 'b16').b14 = b16.get_text()
        else:
            logging.error('No HTML structure found for b16')
        b17 = post.find('blockquote', class_='restore')
        if b17:
            b18 = b17.find_all('div', class_='bbcode_quote')
            for bbcode in b18:
                bbcode.decompose()
            ET.SubElement(b12, 'b17').b14 = b17.get_text()
        else:
            logging.error('No HTML structure found for b17')
    b19 = ET.ElementTree(b11)
    b20 = f'{os.path.splitext(file)[0]}.xml'
    b19.write(b20)
    logging.critical(f'Saved file {b20}')
logging.critical('End of processing')