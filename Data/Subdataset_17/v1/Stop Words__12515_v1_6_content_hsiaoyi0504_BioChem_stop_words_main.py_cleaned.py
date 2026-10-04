import gzip
import shutil
import re
import pickle
import xml.etree.ElementTree as ET
from collections import Counter
from os import mkdir, remove
from os.path import dirname, abspath, exists, join
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from functools import lru_cache
from six.moves.urllib import request
PROJECT_ROOT = dirname(abspath(__file__))
NUM_FILES = 928
DATA_PATH = join(PROJECT_ROOT, 'data')
CHECKPOINT_FILE = 'checkpoint.pkl'
STOP_WORDS_FILE = 'stop_words_1000.csv'
STOP_WORDS = stopwords.words('english')
LEMMATIZER = WordNetLemmatizer()
lemmatize = lru_cache(maxsize=50000)(LEMMATIZER.lemmatize)
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
def ensure_data_path_exists():
    if not exists(DATA_PATH):
        mkdir(DATA_PATH)
def load_checkpoint():
    if exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'rb') as file:
            num, word_counts = pickle.load(file)
        return int(num), word_counts
    return 0, Counter()
def download_and_extract_file(num):
    url = f'ftp:
    gz_path = join(DATA_PATH, f'pubmed18n{num}.xml.gz')
    xml_path = join(DATA_PATH, f'pubmed18n{num}.xml')
    print(f'Downloading {gz_path} ...')
    while True:
        try:
            request.urlretrieve(url, gz_path)
            break
        except ConnectionResetError:
            continue
    print(f'Extracting {gz_path} ...')
    with gzip.open(gz_path, 'rb') as f_in, open(xml_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    return xml_path
def process_abstract_text(text):
    sentences = sent_tokenize(text)
    words = []
    for sentence in sentences:
        sentence = re.sub(r'\d+', '', sentence)
        tokens = word_tokenize(sentence)
        tagged_tokens = pos_tag(tokens)
        for token, tag in tagged_tokens:
            words.append(lemmatize(token.lower(), get_wordnet_pos(tag)))
    return words
def process_pubmed_file(xml_path, word_counts):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for article in root.findall('PubmedArticle'):
        try:
            abstract = article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').text
            if abstract:
                words = process_abstract_text(abstract)
                word_counts.update(words)
        except AttributeError:
            continue
def save_checkpoint(num, word_counts):
    with open(CHECKPOINT_FILE, 'wb') as file:
        pickle.dump([num, word_counts], file)
def save_word_counts(word_counts):
    with open(STOP_WORDS_FILE, 'w') as file:
        for word, count in word_counts.most_common(1000):
            file.write(f'{word},{count}\n')
def main():
    ensure_data_path_exists()
    start_num, word_counts = load_checkpoint()
    start_num += 1
    for i in range(start_num, NUM_FILES + 1):
        num = str(i).zfill(4)
        xml_path = download_and_extract_file(num)
        process_pubmed_file(xml_path, word_counts)
        print(f'Finished processing pubmed18n{num}')
        save_checkpoint(num, word_counts)
        remove(xml_path)
        remove(join(DATA_PATH, f'pubmed18n{num}.xml.gz'))
    for stop_word in STOP_WORDS + [',', '.', '?', ';', '/', '\\', '!', '*', '(', ')', '|', '{', '}', '[', ']', '-', '>', '<', "'", '%', '=', ':', '+/-', "''", '``', '+', '--']:
        if stop_word in word_counts:
            del word_counts[stop_word]
    save_word_counts(word_counts)
if __name__ == '__main__':
    main()