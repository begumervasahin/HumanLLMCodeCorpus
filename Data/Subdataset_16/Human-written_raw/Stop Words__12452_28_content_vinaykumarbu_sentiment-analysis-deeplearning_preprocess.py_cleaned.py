import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
b1 = set(stopwords.words("english"))
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import enchant
b2 = enchant.Dict("en_US")
import nltk
b3 = set(nltk.corpus.words.words())
b4 = open("new_preprocessed.txt","a")
b5 = open('new_tweets.txt','r')
for b6 in b5:
    b6 = b6.split(',b6:')[1]
    b7 = b6.lower()
    b7 = ''.join([i for i in b7 if not i.isdigit() and i not in string.punctuation])
    b8 = ""
    for word in b7.split(' '):
        if(not word.startswith('@') and len(word)>2 and b2.check(word)):
            b8+=" "+word
    b9 = word_tokenize(b8)
    b10 = []
    for w in b9:
        if w not in b1:
            b10.append(w)
    from nltk.stem import WordNetLemmatizer
    b11 = WordNetLemmatizer()
    b12 = []
    for word in b10:
        b12.append(b11.lemmatize(word))
    b13 = nltk.tag.pos_tag(b12)
    b14 = [word for word,tag in b13 if tag != 'NNP' and tag != 'NNPS']
    b4.write(" ".join(b14))
    b4.write("\n")
b4.close()