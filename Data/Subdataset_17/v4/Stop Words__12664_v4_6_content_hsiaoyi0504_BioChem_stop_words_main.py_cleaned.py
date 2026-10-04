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
wordnet_lemmatizer = WordNetLemmatizer()
lemmatize = lru_cache(maxsize=50000)(wordnet_lemmatizer.lemmatize)
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
if not exists(DATA_PATH):
    mkdir(DATA_PATH)
if exists('checkpoint.pkl'):
    with open('checkpoint.pkl', 'rb') as checkpoint_file:
        last_processed, word_counts = pickle.load(checkpoint_file)
    file_range = range(int(last_processed) + 1, NUM_FILES)
else:
    file_range = range(1, NUM_FILES)
    word_counts = Counter()
for file_number in file_range:
    file_id = str(file_number).zfill(4)
    print(f'Downloading pubmed18n{file_id}.xml.gz ...')
    while True:
        try:
            request.urlretrieve(
                f'ftp:
                join(DATA_PATH, f'pubmed18n{file_id}.xml.gz')
            )
            break
        except ConnectionResetError:
            continue
    print(f'Extracting pubmed18n{file_id}.xml.gz ...')
    file_name_in = join(DATA_PATH, f'pubmed18n{file_id}.xml.gz')
    file_name_out = join(DATA_PATH, f'pubmed18n{file_id}.xml')
    with gzip.open(file_name_in, 'rb') as f_in, open(file_name_out, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    tree = ET.parse(file_name_out)
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
    print(f'Finished processing pubmed18n{file_id}')
    with open('checkpoint.pkl', 'wb') as checkpoint_file:
        pickle.dump([file_id, word_counts], checkpoint_file)
    remove(file_name_in)
    remove(file_name_out)
punctuation_and_special_chars = [',', '.', '?', ';', '/', '\\', '!', '*', '(', ')', '|', '{', '}', '[', ']', '-', '>', '<', "'", '%', '=', ':', '+/-', "''", '``', '+', '--']
for stop_word in STOP_WORDS.union(punctuation_and_special_chars):
    word_counts.pop(stop_word, None)
with open('stop_words_1000.csv', 'w') as output_file:
    for word, count in word_counts.most_common(1000):
        output_file.write(f'{word},{count}\n')