from __future__ import print_function
import json
import re
import io
from random import shuffle
from nltk.tokenize import RegexpTokenizer
from string import digits, punctuation
from nltk.corpus import stopwords
from langdetect import detect, DetectorFactory
from nltk import pos_tag, ngrams
from collections import Counter
import numpy as np
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from tqdm import tqdm
DetectorFactory.a1 = 0
b1 = set(punctuation + digits) - set(['!', '?', '.', '\'', ','])
b2 = RegexpTokenizer(r'\w+\S*\w*')
b3 = set(stopwords.words('english'))
b4 = WordNetLemmatizer()
b5 = dict((ord(char), None) for char in b1)
b6 = ['challenge', 'challenges', 'congrats', 'congratulations', 'congratulation', 'title', 'titles',
                  'ribbon', 'ribbons', 'score', 'scores', 'scored', 'comment', 'b24', 'commented', 'favorites',
                  'favorite', 'fav', 'thanks', 'thank', 'vote', 'voting', 'votes', 'voters', 'voter', 'voted', 'entry',
                  'entries', 'dpc', 'dpchallenge', 'award', 'awards', 'critique', 'rating', 'luck', 'theme']
b7 = {...}
b8 = "CLEAN_AVA_FULL_COMMENTS.json"
b9 = io.open('Logs/Non_English.txt', 'w', encoding='utf-8')
b10 = io.open('Logs/Unigrams.txt', 'w', encoding='utf-8')
b11 = io.open('Logs/Bigrams.txt', 'w', encoding='utf-8')
b12 = io.open('Logs/Normalized_Unigrams.txt', 'w', encoding='utf-8')
b13 = io.open('Logs/Normalized_Bigrams.txt', 'w', encoding='utf-8')
b14 = io.open('Logs/Sub_Discarded.txt', 'w', encoding='utf-8')
b15 = io.open('Logs/Ob_Discarded.txt', 'w', encoding='utf-8')
b16 = io.open('Logs/Accepted.txt', 'w', encoding='utf-8')
b17 = json.load(io.open(b8, encoding='utf-8'))
b18 = [True] * 2 + [False] * 8
shuffle(b18)
b19 = b17['images'][::4]
b20 = np.sum([len(img['sentences']) for img in b19])
b21 = {}
b22 = {}
a2 = 120
a3 = 20
for count, img in enumerate(tqdm(b19, b23 = 0, leave=True, unit='images')):
    b24 = img['sentences']
    b25 = filter(check_language, b24)
    b26 = filter(all_the_steps, b25)
    img['sentences'] = list(b26)
