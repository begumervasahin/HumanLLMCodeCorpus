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
b1 = dirname(abspath(__file__))
a1 = 928
b2 = set(stopwords.words('english'))
b3 = join(b1, 'data')
b4 = WordNetLemmatizer()
b5 = lru_cache(maxsize=50000)(b4.b5)
def fonk1(treebank_tag):
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
if not exists(b3):
    mkdir(b3)
if exists('checkpoint.pkl'):
    with open('checkpoint.pkl', 'rb') as checkpoint_file:
        last_processed, b6 = pickle.load(checkpoint_file)
    b7 = range(int(last_processed) + 1, a1)
else:
    b7 = range(1, a1)
    b6 = Counter()
for file_number in b7:
    b8 = str(file_number).zfill(4)
    print(f'Downloading pubmed18n{b8}.xml.gz ...')
    while True:
        try:
            request.urlretrieve(
                f'ftp:
                join(b3, f'pubmed18n{b8}.xml.gz')
            )
            break
        except ConnectionResetError:
            continue
    print(f'Extracting pubmed18n{b8}.xml.gz ...')
    b9 = join(b3, f'pubmed18n{b8}.xml.gz')
    b10 = join(b3, f'pubmed18n{b8}.xml')
    with gzip.open(b9, 'rb') as f_in, open(b10, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    b11 = ET.parse(b10)
    b12 = b11.getroot()
    for article in b12.findall('PubmedArticle'):
        try:
            b13 = article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').text
            if b13 is None:
                continue
            b14 = sent_tokenize(b13)
            for sentence in b14:
                b15 = re.sub(r'\d+', '', sentence)
                b16 = word_tokenize(b15)
                b17 = pos_tag(b16)
                b18 = [
                    b5(token.lower(), fonk1(tag))
                    for token, tag in b17
                ]
                b6.update(b18)
        except AttributeError:
            continue
    print(f'Finished processing pubmed18n{b8}')
    with open('checkpoint.pkl', 'wb') as checkpoint_file:
        pickle.dump([b8, b6], checkpoint_file)
    remove(b9)
    remove(b10)
b19 = [',', '.', '?', ';', '/', '\\', '!', '*', '(', ')', '|', '{', '}', '[', ']', '-', '>', '<', "'", '%', '=', ':', '+/-', "''", '``', '+', '--']
for stop_word in b2.union(b19):
    b6.pop(stop_word, None)
with open('stop_words_1000.csv', 'w') as output_file:
    for word, count in b6.most_common(1000):
        output_file.write(f'{word},{count}\n')