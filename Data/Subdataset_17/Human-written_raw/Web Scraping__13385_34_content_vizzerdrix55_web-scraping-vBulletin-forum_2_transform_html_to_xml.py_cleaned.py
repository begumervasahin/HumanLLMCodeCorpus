import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import codecs
import logging
logging.basicConfig(filename='xml-transformation.log',
                    filemode='w',
                    format='%(asctime)s %(message)s',
                    level=logging.WARNING)
logging.critical('start')
directory_in_str = ''
directory = os.fsencode(directory_in_str)
filepaths =[]
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".html"):
        filepaths.append(os.path.join(directory_in_str, filename))
    else:
        logging.error('skipped file that ends not with .html: %s' % file)
for file in filepaths:
    try:
        with codecs.open(file, 'r', 'utf-8') as f:
            page = f.read()
    except:
        logging.error('skipped %s because of UnicodeDecodeError' % file)
    else:
        soup = BeautifulSoup(page, 'lxml')
        postlist = soup.find_all('li', ['postbit'])
        if postlist:
            logging.info('HTML structure for postlist successfully checked')
        else:
            logging.error('other HTML structure than expected',
                          'for postlist')
        root = ET.Element('root')
        for post in postlist:
            post_node = ET.SubElement(root, 'post')
            date = post.find('div',['datetime'])
            if date:
                ET.SubElement(post_node, 'date').text = date.get_text()
            else:
                logging.error('no HTML structure found for date')
            title = post.find('div',['title'])
            if title:
                ET.SubElement(post_node, 'title').text = title.get_text()
            else:
                logging.error('no HTML structure found for title')
            username = post.find('span',['username'])
            if username:
                ET.SubElement(post_node, 'username').text                = username.get_text()
            else:
                logging.error('no HTML structure found for username')
            content = post.find('blockquote',['restore'])
            if content:
                bbcodes = content.find_all('div', ['bbcode_quote'])
                for bbcode in bbcodes:
                    bbcode.decompose()
                ET.SubElement(post_node, 'content').text                = content.get_text()
            else:
                logging.error('no HTML structure found for content')
    tree = ET.ElementTree(root)
    tree.write('%s.xml' % file,)
    logging.critical('saved file %s.xml' % file)
logging.critical('end')