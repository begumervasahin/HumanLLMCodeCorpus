import gzip
import shutil
import re
from collections import Counter
import xml.etree.ElementTree as ET
from os import mkdir, remove
from os.path import dirname, abspath, exists, join
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from functools import lru_cache
from six.moves.urllib import request
import pickle
PROJECT_ROOT = dirname(abspath(__file__))
NUM_FILES = 928
STOP_WORDS = set(stopwords.words('english'))
DATA_PATH = join(PROJECT_ROOT, 'data')
CHECKPOINT_FILE = 'checkpoint.pkl'
WORD_COUNTS_FILE = 'stop_words_1000.csv'
lemmatizer = WordNetLemmatizer()
lemmatize = lru_cache(maxsize=50000)(lemmatizer.lemmatize)
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    if treebank_tag.startswith('V'):
        return wordnet.VERB
    if treebank_tag.startswith('N'):
        return wordnet.NOUN
    if treebank_tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN
def download_and_extract_file(file_id):
    url = f'ftp:
    file_name_in = join(DATA_PATH, f'pubmed18n{file_id}.xml.gz')
    file_name_out = join(DATA_PATH, f'pubmed18n{file_id}.xml')
    print(f'Downloading {file_name_in} ...')
    while True:
        try:
            request.urlretrieve(url, file_name_in)
            break
        except ConnectionResetError:
            continue
    print(f'Extracting {file_name_in} ...')
    with gzip.open(file_name_in, 'rb') as f_in, open(file_name_out, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
def parse_and_count_words(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    for article in root.findall('PubmedArticle'):
        try:
            abstract_text = article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').text
            if abstract_text is None:
                continue
            sentences = sent_tokenize(abstract_text)
            for sentence in sentences:
                clean_text = re.sub(r'\d+', '', sentence)
                tokens = word_tokenize(clean_text)
                tagged_tokens = pos_tag(tokens)
                lemmatized_words = [
                    lemmatize(token.lower(), get_wordnet_pos(tag))
                    for token, tag in tagged_tokens
                ]
                word_counts.update(lemmatized_words)
        except AttributeError:
            continue
def save_checkpoint(file_id, word_counts):
    with open(CHECKPOINT_FILE, 'wb') as checkpoint_file:
        pickle.dump([file_id, word_counts], checkpoint_file)
def remove_stop_words(word_counts):
    punctuation_and_special_chars = [',', '.', '?', ';', '/', '\\', '!', '*', '(', ')', '|', '{', '}', '[', ']', '-', '>', '<', "'", '%', '=', ':', '+/-', "''", '``', '+', '--']
    for stop_word in STOP_WORDS.union(punctuation_and_special_chars):
        word_counts.pop(stop_word, None)
    return word_counts
def save_word_counts(word_counts, file_name, top_n=1000):
    with open(file_name, 'w') as output_file:
        for word, count in word_counts.most_common(top_n):
            output_file.write(f'{word},{count}\n')
if not exists(DATA_PATH):
    mkdir(DATA_PATH)
if exists(CHECKPOINT_FILE):
    with open(CHECKPOINT_FILE, 'rb') as checkpoint_file:
        last_processed, word_counts = pickle.load(checkpoint_file)
    file_range = range(int(last_processed) + 1, NUM_FILES)
else:
    file_range = range(1, NUM_FILES)
    word_counts = Counter()
for file_number in file_range:
    file_id = str(file_number).zfill(4)
    download_and_extract_file(file_id)
    parse_and_count_words(join(DATA_PATH, f'pubmed18n{file_id}.xml'))
    print(f'Finished processing pubmed18n{file_id}')
    save_checkpoint(file_id, word_counts)
    remove(join(DATA_PATH, f'pubmed18n{file_id}.xml.gz'))
    remove(join(DATA_PATH, f'pubmed18n{file_id}.xml'))
word_counts = remove_stop_words(word_counts)
save_word_counts(word_counts, WORD_COUNTS_FILE)