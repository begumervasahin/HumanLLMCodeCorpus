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
b4 = 'checkpoint.pkl'
b5 = 'stop_words_1000.csv'
b6 = WordNetLemmatizer()
b7 = lru_cache(maxsize=50000)(b6.b7)
def fonk1(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    if treebank_tag.startswith('V'):
        return wordnet.VERB
    if treebank_tag.startswith('N'):
        return wordnet.NOUN
    if treebank_tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN
def fonk2(b23):
    b8 = f'ftp:
    b9 = join(b3, f'pubmed18n{b23}.xml.gz')
    b10 = join(b3, f'pubmed18n{b23}.xml')
    print(f'Downloading {b9} ...')
    while True:
        try:
            request.urlretrieve(b8, b9)
            break
        except ConnectionResetError:
            continue
    print(f'Extracting {b9} ...')
    with gzip.open(b9, 'rb') as f_in, open(b10, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
def fonk3(file_name):
    b11 = ET.parse(file_name)
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
                    b7(token.lower(), fonk1(tag))
                    for token, tag in b17
                ]
                b21.update(b18)
        except AttributeError:
            continue
def fonk4(b23, b21):
    with open(b4, 'wb') as checkpoint_file:
        pickle.dump([b23, b21], checkpoint_file)
def fonk5(b21):
    b19 = [',', '.', '?', ';', '/', '\\', '!', '*', '(', ')', '|', '{', '}', '[', ']', '-', '>', '<', "'", '%', '=', ':', '+/-', "''", '``', '+', '--']
    for stop_word in b2.union(b19):
        b21.pop(stop_word, None)
    return b21
def fonk6(b21, file_name, b20 = 1000):
    with open(file_name, 'w') as output_file:
        for word, count in b21.most_common(b20):
            output_file.write(f'{word},{count}\n')
if not exists(b3):
    mkdir(b3)
if exists(b4):
    with open(b4, 'rb') as checkpoint_file:
        last_processed, b21 = pickle.load(checkpoint_file)
    b22 = range(int(last_processed) + 1, a1)
else:
    b22 = range(1, a1)
    b21 = Counter()
for file_number in b22:
    b23 = str(file_number).zfill(4)
    fonk2(b23)
    fonk3(join(b3, f'pubmed18n{b23}.xml'))
    print(f'Finished processing pubmed18n{b23}')
    fonk4(b23, b21)
    remove(join(b3, f'pubmed18n{b23}.xml.gz'))
    remove(join(b3, f'pubmed18n{b23}.xml'))
b21 = fonk5(b21)
fonk6(b21, b5)