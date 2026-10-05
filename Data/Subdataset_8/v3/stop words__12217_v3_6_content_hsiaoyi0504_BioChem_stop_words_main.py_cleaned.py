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
WORDNET_LEMMATIZER = WordNetLemmatizer()
LEM_CACHE_SIZE = 50000
lemmatize = lru_cache(maxsize=LEM_CACHE_SIZE)(WORDNET_LEMMATIZER.lemmatize)
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
DATA_PATH = join(PROJECT_ROOT, 'data')
if not exists(DATA_PATH):
    mkdir(DATA_PATH)
if exists('checkpoint.pkl'):
    with open('checkpoint.pkl', 'rb') as f:
        num, word_counts = pickle.load(f)
    iter_range = range(int(num) + 1, NUM_FILES)
else:
    iter_range = range(1, NUM_FILES)
    word_counts = Counter()
for i in iter_range:
    num = str(i).zfill(4)
    print(f'Downloading pubmed18n{num}.xml.gz ...')
    while True:
        try:
            request.urlretrieve(
                f'ftp:
                join(DATA_PATH, f'pubmed18n{num}.xml.gz'))
            break
        except ConnectionResetError:
            continue
    print(f'Extracting pubmed18n{num}.xml.gz ...')
    file_name_in = join(DATA_PATH, f'pubmed18n{num}.xml.gz')
    file_name_out = join(DATA_PATH, f'pubmed18n{num}.xml')
    with gzip.open(file_name_in, 'rb') as f_in, open(file_name_out, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    tree = ET.parse(file_name_out)
    root = tree.getroot()
    for article in root.findall('PubmedArticle'):
        try:
            abstract = article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').text
            try:
                sentences = sent_tokenize(abstract)
            except TypeError:
                continue
            for s in sentences:
                temp = re.sub(r'\d+', '', s)
                text = word_tokenize(temp)
                tagged_text = pos_tag(text)
                temp_words = []
                for t, tag in tagged_text:
                    temp_words.append(lemmatize(t.lower(), get_wordnet_pos(tag)))
                word_counts.update(temp_words)
        except AttributeError:
            continue
    print(f'Finished processing the pubmed18n{num}')
    with open('checkpoint.pkl', 'wb') as f:
        pickle.dump([num, word_counts], f)
    remove(file_name_in)
    remove(file_name_out)
for s in STOP_WORDS.union({',', '.', '?', ';', '/', '\\', '!', '*', '(', ')', '|', '{', '}', '[', ']', '-', '>', '<', "'", '%', '=', ':', '+/-', "''", '``', '+', '--'}):
    if s in word_counts:
        del word_counts[s]
with open('stop_words_1000.csv', 'w') as f:
    for w, count in word_counts.most_common(1000):
        f.write(f'{w},{count}\n')