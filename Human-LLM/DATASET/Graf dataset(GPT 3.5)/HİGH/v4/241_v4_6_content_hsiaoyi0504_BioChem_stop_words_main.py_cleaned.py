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
b2 = stopwords.words('english')
b3 = WordNetLemmatizer()
b4 = lru_cache(maxsize=50000)(b3.b4)
b5 = join(b1, 'data')
if not exists(b5):
    mkdir(b5)
if exists('checkpoint.pkl'):
    with open('checkpoint.pkl', 'rb') as f:
        b8, b6 = pickle.load(f)
    b7 = range(int(b8) + 1, a1)
else:
    b7 = range(1, a1)
    b6 = Counter()
for i in b7:
    b8 = str(i).zfill(4)
    print(f'Downloading pubmed18n{b8}.xml.gz ...')
    while True:
        try:
            request.urlretrieve(
                f'ftp:
                join(b5, f'pubmed18n{b8}.xml.gz'))
            break
        except ConnectionResetError:
            continue
    print(f'Extracting pubmed18n{b8}.xml.gz ...')
    b9 = join(b5, f'pubmed18n{b8}.xml.gz')
    b10 = join(b5, f'pubmed18n{b8}.xml')
    with gzip.open(b9, 'rb') as f_in, open(b10, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    b11 = ET.parse(b10)
    b12 = b11.getroot()
    for article in b12.findall('PubmedArticle'):
        try:
            b13 = article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').b16
            try:
                b14 = sent_tokenize(b13)
            except TypeError:
                continue
            for s in b14:
                b15 = re.sub(r'\d+', '', s)
                b16 = word_tokenize(b15)
                b17 = pos_tag(b16)
                b18 = []
                for t, tag in b17:
                    b18.append(b4(t.lower(), get_wordnet_pos(tag)))
                b6.update(b18)
        except AttributeError:
            continue
    print(f'Finished processing the pubmed18n{b8}')
    with open('checkpoint.pkl', 'wb') as f:
        pickle.dump([b8, b6], f)
    remove(b9)
    remove(b10)
for s in b2 + [',', '.', '?', ';', '/', '\\', '!', '*', '(', ')', '|', '{', '}', '[', ']', '-', '>', '<', "'", '%', '=', ':', '+/-', "''", '``', '+', '--']:
    if s in b6:
        del b6[s]
with open('stop_words_1000.csv', 'w') as f:
    for w, count in b6.most_common(1000):
        f.write(w + ',' + str(count) + '\n')