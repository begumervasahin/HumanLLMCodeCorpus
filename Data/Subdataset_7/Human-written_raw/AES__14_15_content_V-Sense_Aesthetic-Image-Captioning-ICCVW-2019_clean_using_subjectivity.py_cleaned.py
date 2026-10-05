'''
1. remove non-english captions
2. Truncates woooooooow to woow, and what!!!!!!!!!!!!!! to what!
3. Puncuations except ?, !, ,, . are removed
4. Tokenizes into b31 and b32
5. Computes probabilities based on corpus freq and filters captions
6. Also coments with manually selected bad words are removed by hard coding zero probabilities
'''
from __future__ import print_function
import json
import re
import io
from random import shuffle
import pdb
from nltk.tokenize import RegexpTokenizer
from string import digits, punctuation
from nltk.corpus import stopwords
from langdetect import detect
from nltk import pos_tag
from langdetect import DetectorFactory
from nltk.util import ngrams
from collections import Counter
import numpy as np
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from tqdm import tqdm
DetectorFactory.a1 = 0
import itertools
b1 = set(punctuation + digits) - set(['!','?', '.', '\'',','])
b2 = RegexpTokenizer(r'\w+\S*\w*')
b3 = set(stopwords.words('english'))
b4 = WordNetLemmatizer()
b5 = dict((ord(char), None) for char in b1)
b6 = ['challenge', 'challenges', 'congrats', 'congratulations',\
'congratulation', 'title','titles',  'ribbon', 'ribbons','score', 'scores','scored', \
 'comment', 'b43', 'commented','favorites', 'favorite', 'fav','thanks', 'thank', 'vote', 'voting',\
 'votes', 'voters', 'voter','voted', 'entry', 'entries', 'dpc', 'dpchallenge', 'award', 'awards', 'critique', 'rating', 'luck', 'theme']
b7 = {
    '\xc2\x82' : ',',
    '\xc2\x84' : ',,',
    '\xc2\x85' : '...',
    '\xc2\x88' : '^',
    '\xc2\x91' : '\x27',
    '\xc2\x92' : '\x27',
    '\xc2\x93' : '\x22',
    '\xc2\x94' : '\x22',
    '\xc2\x95' : ' ',
    '\xc2\x96' : '-',
    '\xc2\x97' : '--',
    '\xc2\x99' : ' ',
    '\xc2\xa0' : ' ',
    '\xc2\xa6' : '|',
    '\xc2\xab' : '<<',
    '\xc2\xbb' : '>>',
    '\xc2\xbc' : '1/4',
    '\xc2\xbd' : '1/2',
    '\xc2\xbe' : '3/4',
    '\xca\xbf' : '\x27',
    '\xcc\xa8' : '',
    '\xcc\xb1' : '',
    '\xc2\xb4' : '\''
}
b8 = "CLEAN_AVA_FULL_COMMENTS.json"
b9 = io.open('Logs/Non_English.txt','w', encoding = 'utf-8')
b10 = io.open('Logs/Unigrams.txt','w', encoding = 'utf-8')
b11 = io.open('Logs/Bigrams.txt','w', encoding = 'utf-8')
b12 = io.open('Logs/Normalized_Unigrams.txt','w', encoding = 'utf-8')
b13 = io.open('Logs/Normalized_Bigrams.txt','w', encoding = 'utf-8')
b14 = io.open('Logs/Sub_Discarded.txt','w', encoding = 'utf-8')
b15 = io.open('Logs/Ob_Discarded.txt','w', encoding = 'utf-8')
b16 = io.open('Logs/Accepted.txt','w', encoding = 'utf-8')
b17 = json.load(io.open(b8, encoding = 'utf-8'))
b18 = [True] * 2 + [False] * 8
shuffle(b18)
b19 = b17['images'][::4]
b20 = np.sum([len(img['sentences']) for img in b19])
b21 = {}
b22 = {}
a2 = 120
a3 = 20
def fonk1(text):
    b23 = re.compile(r"(.)\1{2,}")
    return b23.sub(r"\1\1", text)
def fonk2(comment):
    comment['clean'] = ' '.join(map(reduce_lengthening_word, comment['clean'].split()))
    return comment
def fonk3(comment):
    b24 = re.compile(r'([.,/
    comment['clean'] = b24.sub(r'\1', comment['clean'])
    return comment
def fonk4(comment):
    b25 = comment['raw'].lower()
    b26 = b25.translate(b7)
    comment['clean'] = b26.translate(b5)
    return comment
def fonk5(unigram):
    global b21
    b27 = unigram[1]
    if b27 in ['NN', 'NNS']:
        try:
           b21[unigram[0]] += 1
        except KeyError as e:
            b21[unigram[0]] = 1
        return True
    else:
        return False
def fonk6(bigram):
    global b22
    if bigram[0][1] in ['NN', 'NNS', 'JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS'] \
    and bigram[1][1] in ['NN', 'NNS', 'JJ', 'JJR', 'JJS']:
        b28 = bigram[0][0] + '_' +bigram[1][0]
        try:
           b22[b28] += 1
        except KeyError as e:
            b22[b28] = 1
        return True
    else:
        return False
def fonk7(comment):
    b29 = re.findall(r"[\w']+|[.,!?;]", comment['clean'], re.UNICODE)
    b30 = pos_tag(b29)
    comment['b29'] = b30
    return comment
def fonk8(comment):
    b30 = comment['b29']
    b31 = [(i,j) for i,j in b30 if i not in (b3 | set(punctuation))]
    b32 = ngrams(b31, 2)
    b33 = filter(update_unigram_dictionary, b31)
    b34 = filter(update_bi_gram_dictionary, b32)
    comment['b31'] = b33
    comment['b32'] = b34
def fonk9(comment):
    global b18
    b35 = b18[np.random.randint(10)]
    try:
        b36 = detect(comment['raw']) == u'en'
        if b36:
            return True
        else:
            if b35:
                print (comment['raw'], b37 = b9)
            return False
    except:
        if b35:
            print (u'No language detected for : ' , comment['raw'], b37 = b9)
        return False
def fonk10(comment):
      b38 = fonk4(comment)
      b39 = fonk3(b38)
      b40 = fonk2(b39)
      b41 = fonk7(b40)
      if fonk12(b41):
          fonk8(b41)
          if len(b41['b31']) != 0 or len(b41['b32']) != 0:
              return True
          else:
              return False
      else:
          return False
def fonk11(comment):
      b38 = fonk4(comment)
      b39 = fonk3(b38)
      b40 = fonk2(b39)
      b42 = re.split("!|\\?|\\.", b40['clean'])
      b43 = []
      for split_comment in b42:
          b43.append({'clean':split_comment})
      b44 = map(tokenize, b43)
      b45 = filter(remove_dpc, b44)
      b46 = []
      for non_lame_comment in b45:
          fonk8(non_lame_comment)
          if len(non_lame_comment['b31']) != 0 or len(non_lame_comment['b32']) != 0:
              b46.append(non_lame_comment)
      return b46
def fonk12(comment):
    def fonk13(b27):
        global b4
        if b27[1] in ['NN', 'NNS', 'NNP', 'NNPS']:
            return (b4.fonk13(b27[0], wordnet.NOUN), b27[1])
        elif b27[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            return (b4.fonk13(b27[0], wordnet.VERB), b27[1])
        elif b27[1] in ['JJ', 'JJR', 'JJS']:
            return (b4.fonk13(b27[0], wordnet.ADJ), b27[1])
        elif b27[1] in [ 'RB', 'RBR', 'RBS']:
            return (b4.fonk13(b27[0], wordnet.ADV), b27[1])
        else:
            return b27
    b30 = comment['b29']
    b47 = map(lemmatize, b30)
    for token in b47:
        if token[0] in b6:
            return False
    comment['b29'] = b47
    return True
def fonk14(comment):
    global unit_count_threshold, a2, a3, b21, b22, b18
    a4 = 1.0
    a5 = 1.0
    b48 = True
    b49 = True
    b35 = b18[np.random.randint(10)]
    for unigram in comment['b31']:
        a4 *= b54[unigram[0]]
    for bigram in comment['b32']:
        a5 *= b55[bigram[0][0] +'_' +bigram[1][0]]
    if -np.log(a4 * a5)/2 <= a2:
        b49 = False
    if -np.log(a4 * a5)/2 >= a3 and len(comment['b29']) >= 5:
        b48 = False
    b50 = not (b49 or b48 )
    if not b50:
        if b48 and b35:
            print(unicode("{:0.1e}".format(a5)), \
            unicode("{:0.1e}".format(a4)), \
            unicode("{:0.1f}".format(-np.log(a4 * \
            a5)/2)) , comment['clean'], b37 = b15)
        else :
            if b35:
                print(unicode("{:0.1e}".format(a5)),\
                unicode("{:0.1e}".format(a4)), \
                unicode("{:0.1f}".format(-np.log(a4 * \
                a5)/2)), comment['clean'], b37 = b14)
    else:
        if b35:
            print(unicode("{:0.1e}".format(a5)),\
            unicode("{:0.1e}".format(a4)),\
            unicode("{:0.1f}".format(-np.log(a4 * \
                a5)/2)), comment['clean'], b37 = b16)
    return b50
for count, img in enumerate(tqdm(b19,  b51 = 0, leave=True, unit=' images')):
    b43 = img['sentences']
    b52 = filter(check_language, b43)
    b53 = filter(all_the_steps, b52)
    img['sentences'] = b53
print ('\n'.join([i + '\t'+ str(j) for i,j in Counter(b21).most_common()]), b37 = b10)
print ('\n'.join([i + '\t' + str(j) for i,j in Counter(b22).most_common()]), b37 = b11)
b54 = dict(zip(b21.keys(), np.array(b21.values())/float(np.sum(b21.values()))))
b55 = dict(zip(b22.keys(), np.array(b22.values())/float(np.sum(b22.values()))))
print ('\n'.join([i + '\t'+ unicode("{:0.1e}".format(j)) for i,j in Counter(b54).most_common()]), b37 = b12)
print ('\n'.join([i + '\t' + unicode("{:0.1e}".format(j)) for i,j in Counter(b55).most_common()]), b37 = b13)
b56 = np.sum([len(img['sentences']) for img in b19])
for count, img in enumerate(tqdm(b19,  b51 = 0, leave=True, unit=' images')):
    b43 = img['sentences']
    b52 = filter(filter_commenst_sub_dis, b43)
    img['sentences'] = b52
b19 = [img for img in b19 if len(img['sentences']) > 0]
b57 = {}
b57['dataset'] = 'AVA'
b57['images'] = b19
b58 = np.sum([len(img['sentences']) for img in b19])
print ("First : %d\nSecond : %d\nThird : %d\nPercent Removed : %0.2f"\
%(b20, b56, b58,(1 - b58/float(b20))*100))
pdb.set_trace()