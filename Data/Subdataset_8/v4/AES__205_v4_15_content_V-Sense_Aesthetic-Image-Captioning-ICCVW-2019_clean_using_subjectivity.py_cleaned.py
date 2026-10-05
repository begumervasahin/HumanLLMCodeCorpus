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
DetectorFactory.seed = 0
exclude = set(punctuation + digits) - set(['!', '?', '.', '\'', ','])
tokenizer = RegexpTokenizer(r'\w+\S*\w*')
stop = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
remove_char_map = dict((ord(char), None) for char in exclude)
lame_word_list = ['challenge', 'challenges', 'congrats', 'congratulations', 'congratulation', 'title', 'titles',
                  'ribbon', 'ribbons', 'score', 'scores', 'scored', 'comment', 'comments', 'commented', 'favorites',
                  'favorite', 'fav', 'thanks', 'thank', 'vote', 'voting', 'votes', 'voters', 'voter', 'voted', 'entry',
                  'entries', 'dpc', 'dpchallenge', 'award', 'awards', 'critique', 'rating', 'luck', 'theme']
replace_char_map = {...}
input_json = "CLEAN_AVA_FULL_COMMENTS.json"
non_eng_f = io.open('Logs/Non_English.txt', 'w', encoding='utf-8')
unigram_f = io.open('Logs/Unigrams.txt', 'w', encoding='utf-8')
bigram_f = io.open('Logs/Bigrams.txt', 'w', encoding='utf-8')
norm_unigram_f = io.open('Logs/Normalized_Unigrams.txt', 'w', encoding='utf-8')
norm_bigram_f = io.open('Logs/Normalized_Bigrams.txt', 'w', encoding='utf-8')
sub_discarded_f = io.open('Logs/Sub_Discarded.txt', 'w', encoding='utf-8')
ob_discarded_f = io.open('Logs/Ob_Discarded.txt', 'w', encoding='utf-8')
accepted_f = io.open('Logs/Accepted.txt', 'w', encoding='utf-8')
data = json.load(io.open(input_json, encoding='utf-8'))
print_flag_array = [True] * 2 + [False] * 8
shuffle(print_flag_array)
imgs = data['images'][::4]
original_count = np.sum([len(img['sentences']) for img in imgs])
unigram_dictionary = {}
bigram_dictionary = {}
subjectivity_threshold = 120
objectivity_threshold = 20
for count, img in enumerate(tqdm(imgs, position=0, leave=True, unit='images')):
    comments = img['sentences']
    new_comments = filter(check_language, comments)
    reduced_tokenized_comments = filter(all_the_steps, new_comments)
    img['sentences'] = list(reduced_tokenized_comments)
