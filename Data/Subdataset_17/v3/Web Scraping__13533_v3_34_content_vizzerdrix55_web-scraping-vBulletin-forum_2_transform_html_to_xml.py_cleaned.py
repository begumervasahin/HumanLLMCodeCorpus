import os
import codecs
import logging
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
logging.basicConfig(
    filename='xml-transformation.log',
    filemode='w',
    format='%(asctime)s %(message)s',
    level=logging.WARNING
)
logging.critical('Start of the script execution')
directory_path = ''
def get_html_file_paths(directory):
    filepaths = [
        os.path.join(directory, os.fsdecode(file))
        for file in os.listdir(os.fsencode(directory))
        if os.fsdecode(file).endswith('.html')
    ]
    return filepaths
def read_html_file(filepath):
    try:
        with codecs.open(filepath, 'r', 'utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        logging.error('Skipped %s due to UnicodeDecodeError', filepath)
        return None
def parse_html_to_xml(page_content, filepath):
    soup = BeautifulSoup(page_content, 'lxml')
    postlist = soup.find_all('li', class_='postbit')
    if not postlist:
        logging.error('Unexpected HTML structure in %s for postlist', filepath)
        return None
    logging.info('HTML structure for postlist successfully checked in %s', filepath)
    root = ET.Element('root')
    for post in postlist:
        post_node = ET.SubElement(root, 'post')
        date = post.find('div', class_='datetime')
        if date:
            ET.SubElement(post_node, 'date').text = date.get_text()
        else:
            logging.error('No HTML structure found for date in %s', filepath)
        title = post.find('div', class_='title')
        if title:
            ET.SubElement(post_node, 'title').text = title.get_text()
        else:
            logging.error('No HTML structure found for title in %s', filepath)
        username = post.find('span', class_='username')
        if username:
            ET.SubElement(post_node, 'username').text = username.get_text()
        else:
            logging.error('No HTML structure found for username in %s', filepath)
        content = post.find('blockquote', class_='restore')
        if content:
            for bbcode in content.find_all('div', class_='bbcode_quote'):
                bbcode.decompose()
            ET.SubElement(post_node, 'content').text = content.get_text()
        else:
            logging.error('No HTML structure found for content in %s', filepath)
    return root
def save_xml_tree(root, filepath):
    if root is not None:
        output_file = f'{filepath}.xml'
        tree = ET.ElementTree(root)
        tree.write(output_file)
        logging.critical('Saved file %s', output_file)
def main(directory_path):
    filepaths = get_html_file_paths(directory_path)
    for filepath in filepaths:
        page_content = read_html_file(filepath)
        if page_content:
            xml_root = parse_html_to_xml(page_content, filepath)
            save_xml_tree(xml_root, filepath)
    logging.critical('End of the script execution')
if __name__ == '__main__':
    main(directory_path)