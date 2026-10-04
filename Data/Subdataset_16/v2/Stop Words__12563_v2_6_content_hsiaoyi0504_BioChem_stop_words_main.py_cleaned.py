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
b1 = dirname(abspath(__file__))
a1 = 928
b2 = join(b1, 'data')
b3 = 'checkpoint.pkl'
b4 = 'stop_words_1000.csv'
b5 = stopwords.b13('english')
b6 = WordNetLemmatizer()
b7 = lru_cache(maxsize=50000)(b6.b7)
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
def fonk2():
    if not exists(b2):
        mkdir(b2)
def fonk3():
    if exists(b3):
        with open(b3, 'rb') as file:
            b20, b8 = pickle.load(file)
        return int(b20), b8
    return 0, Counter()
def fonk4(b20):
    b9 = f'ftp:
    b10 = join(b2, f'pubmed18n{b20}.xml.gz')
    b11 = join(b2, f'pubmed18n{b20}.xml')
    print(f'Downloading {b10} ...')
    while True:
        try:
            request.urlretrieve(b9, b10)
            break
        except ConnectionResetError:
            continue
    print(f'Extracting {b10} ...')
    with gzip.open(b10, 'rb') as f_in, open(b11, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    return b11
def fonk5(text):
    b12 = sent_tokenize(text)
    b13 = []
    for b14 in b12:
        b14 = re.sub(r'\d+', '', b14)
        b15 = word_tokenize(b14)
        b16 = pos_tag(b15)
        for token, tag in b16:
            b13.append(b7(token.lower(), fonk1(tag)))
    return b13
def fonk6(b11, b8):
    b17 = ET.parse(b11)
    b18 = b17.getroot()
    for article in b18.findall('PubmedArticle'):
        try:
            b19 = article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').text
            if b19:
                b13 = fonk5(b19)
                b8.update(b13)
        except AttributeError:
            continue
def fonk7(b20, b8):
    with open(b3, 'wb') as file:
        pickle.dump([b20, b8], file)
def fonk8(b8):
    with open(b4, 'w') as file:
        for word, count in b8.most_common(1000):
            file.write(f'{word},{count}\n')
def fonk9():
    fonk2()
    start_num, b8 = fonk3()
    start_num += 1
    for i in range(start_num, a1 + 1):
        b20 = str(i).zfill(4)
        b11 = fonk4(b20)
        fonk6(b11, b8)
        print(f'Finished processing pubmed18n{b20}')
        fonk7(b20, b8)
        remove(xml