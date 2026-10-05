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
DATA_PATH = join(PROJECT_ROOT, 'data')
STOPWORDS = set(stopwords.words('english'))
wordnet_lemmatizer = WordNetLemmatizer()
lemmatize = lru_cache(maxsize=50000)(wordnet_lemmatizer.lemmatize)
def download_file(url, destination):
    while True:
        try:
            request.urlretrieve(url, destination)
            break
        except ConnectionResetError:
            continue
def extract_gzip(gzip_file, output_file):
    with gzip.open(gzip_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
def process_abstract(abstract_text, word_counts):
    sentences = sent_tokenize(abstract_text)
    for sentence in sentences:
        sentence = re.sub(r'\d+', '', sentence)
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        for word, tag in tagged_words:
            lemma = lemmatize(word.lower(), get_wordnet_pos(tag))
            if lemma not in STOPWORDS and lemma.isalpha():
                word_counts[lemma] += 1
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
def main():
    if not exists(DATA_PATH):
        mkdir(DATA_PATH)
    if exists('checkpoint.pkl'):
        with open('checkpoint.pkl', 'rb') as f:
            start_index, word_counts = pickle.load(f)
        start_index = int(start_index)
        file_range = range(start_index + 1, NUM_FILES)
    else:
        start_index = 0
        word_counts = Counter()
        file_range = range(1, NUM_FILES)
    for i in file_range:
        file_index = str(i).zfill(4)
        print(f'Downloading and processing pubmed18n{file_index}.xml.gz ...')
        download_file(
            f'ftp:
            join(DATA_PATH, f'pubmed18n{file_index}.xml.gz')
        )
        extract_gzip(
            join(DATA_PATH, f'pubmed18n{file_index}.xml.gz'),
            join(DATA_PATH, f'pubmed18n{file_index}.xml')
        )
        tree = ET.parse(join(DATA_PATH, f'pubmed18n{file_index}.xml'))
        root = tree.getroot()
        for article in root.findall('PubmedArticle'):
            try:
                abstract = article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').text
                if abstract:
                    process_abstract(abstract, word_counts)
            except AttributeError:
                continue
        with open('checkpoint.pkl', 'wb') as f:
            pickle.dump([file_index, word_counts], f)
        remove(join(DATA_PATH, f'pubmed18n{file_index}.xml.gz'))
        remove(join(DATA_PATH, f'pubmed18n{file_index}.xml'))
    word_counts = {word: count for word, count in word_counts.items() if word not in STOPWORDS and word.isalpha()}
    with open('stop_words_1000.csv', 'w') as f:
        for word, count in word_counts.most_common(1000):
            f.write(f'{word},{count}\n')
if __name__ == "__main__":
    main()