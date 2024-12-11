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
b2 = join(b1, 'data')
b3 = set(stopwords.b8('english'))
b4 = WordNetLemmatizer()
b5 = lru_cache(maxsize=50000)(b4.b5)
def fonk1(url, destination):
    while True:
        try:
            request.urlretrieve(url, destination)
            break
        except ConnectionResetError:
            continue
def fonk2(gzip_file, output_file):
    with gzip.open(gzip_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
def fonk3(abstract_text, b11):
    b6 = sent_tokenize(abstract_text)
    for b7 in b6:
        b7 = re.sub(r'\d+', '', b7)
        b8 = word_tokenize(b7)
        b9 = pos_tag(b8)
        for word, tag in b9:
            b10 = b5(word.lower(), fonk4(tag))
            if b10 not in b3 and b10.isalpha():
                b11[b10] += 1
def fonk4(treebank_tag):
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
def fonk5():
    if not exists(b2):
        mkdir(b2)
    if exists('checkpoint.pkl'):
        with open('checkpoint.pkl', 'rb') as f:
            b12, b11 = pickle.load(f)
        b12 = int(b12)
        b13 = range(b12 + 1, a1)
    else:
        b12 = 0
        b11 = Counter()
        b13 = range(1, a1)
    for i in b13:
        b14 = str(i).zfill(4)
        print(f'Downloading and processing pubmed18n{b14}.xml.gz ...')
        fonk1(
            f'ftp:
            join(b2, f'pubmed18n{b14}.xml.gz')
        )
        fonk2(
            join(b2, f'pubmed18n{b14}.xml.gz'),
            join(b2, f'pubmed18n{b14}.xml')
        )
        b15 = ET.parse(join(b2, f'pubmed18n{b14}.xml'))
        b16 = b15.getroot()
        for article in b16.findall('PubmedArticle'):
            try:
                b17 = article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').text
                if b17:
                    fonk3(b17, b11)
            except AttributeError:
                continue
        with open('checkpoint.pkl', 'wb') as f:
            pickle.dump([b14, b11], f)
        remove(join(b2, f'pubmed18n{b14}.xml.gz'))
        remove(join(b2, f'pubmed18n{b14}.xml'))
    b11 = {word: count for word, count in b11.items() if word not in b3 and word.isalpha()}
    with open('stop_words_1000.csv', 'w') as f:
        for word, count in b11.most_common(1000):
            f.write(f'{word},{count}\n')
if b18 = = "__main__":
    fonk5()