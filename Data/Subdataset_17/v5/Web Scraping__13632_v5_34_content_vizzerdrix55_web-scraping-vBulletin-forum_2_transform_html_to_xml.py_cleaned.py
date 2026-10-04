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
logging.critical('Start of processing')
def collect_html_files(directory_path):
    directory = os.fsencode(directory_path)
    filepaths = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".html"):
            filepaths.append(os.path.join(directory_path, filename))
        else:
            logging.error(f'Skipped non-HTML file: {filename}')
    return filepaths
def parse_html_file(file):
    try:
        with codecs.open(file, 'r', 'utf-8') as f:
            page = f.read()
        return BeautifulSoup(page, 'lxml')
    except UnicodeDecodeError:
        logging.error(f'Skipped {file} due to UnicodeDecodeError')
        return None
def extract_post_data(post):
    data = {}
    date = post.find('div', class_='datetime')
    data['date'] = date.get_text() if date else None
    title = post.find('div', class_='title')
    data['title'] = title.get_text() if title else None
    username = post.find('span', class_='username')
    data['username'] = username.get_text() if username else None
    content = post.find('blockquote', class_='restore')
    if content:
        for bbcode in content.find_all('div', class_='bbcode_quote'):
            bbcode.decompose()
        data['content'] = content.get_text()
    else:
        data['content'] = None
    return data
def create_xml_from_posts(posts):
    root = ET.Element('root')
    for post_data in posts:
        post_node = ET.SubElement(root, 'post')
        for key, value in post_data.items():
            if value:
                ET.SubElement(post_node, key).text = value
            else:
                logging.error(f'No HTML structure found for {key}')
    return ET.ElementTree(root)
def save_xml(tree, filename):
    tree.write(filename)
    logging.critical(f'Saved file {filename}')
def process_html_files(directory_path):
    filepaths = collect_html