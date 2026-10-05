import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import string
b1 = open('nlp python answer finals.txt','r',errors = 'ignore')
b2 = open('modules pythons.txt','r',errors = 'ignore')
b3 = "./chatbot_weights.ckpt"
b4 = b1.read()
b5 = b2.read()
b4 = b4.lower()
b5 = b5.lower()
nltk.download('punkt')
nltk.download('wordnet')
b6 = nltk.sent_tokenize(b4)
b7 = nltk.word_tokenize(b4)
b8 = nltk.sent_tokenize(b5)
b9 = nltk.word_tokenize(b5)
b6[:2]
b8[:2]
b7[:5]
b9[:5]
b10 = nltk.stem.WordNetLemmatizer()
def fonk1(tokens):
    return [b10.lemmatize(token) for token in tokens]
b11 = dict((ord(punct), None) for punct in string.punctuation)
def fonk2(text):
    return fonk1(nltk.word_tokenize(text.lower().translate(b11)))
b12 = ["My name is PyBot.","My name is PyBot you can called me pi.","Im PyBot :) ","My name is PyBot. and my nickname is pi and i am happy to solve your queries :) "]
b13 = ("hello", "hi","hiii","hii","hiiii","hiiii", "greetings", "sup", "what's up","hey",)
b14 = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
b15 = ("what is python ?","what is python","what is python?","what is python.")
b16 = "Python is a high-level, interpreted, interactive and object-oriented scripting programming language python is designed to be highly readable It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages."
b17 = ("what is module","what is module.","what is module ","what is module ?","what is module?","what is module in python","what is module in python.","what is module in python?","what is module in python ?")
b18 = ["Consider a module to be the same as a code library.","A file containing a set of functions you want to include in your application.","A module can define functions, classes and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use."]
def fonk3(sentence):
    for word in sentence.split():
        if word.lower() in b13:
            return random.choice(b14)
def fonk4(sentence):
    for word in b15:
        if sentence.lower() == word:
            return b16
def fonk5(sentence):
    for word in b17:
        if sentence.lower() == word:
            return random.choice(b18)
def fonk6(sentence):
    return random.choice(b12)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def fonk7(b26):
    b19 = ''
    b6.append(b26)
    b20 = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    b21 = b20.fit_transform(b6)
    b22 = cosine_similarity(b21[-1], b21)
    b23 = b22.argsort()[0][-2]
    b24 = b22.flatten()
    b24.sort()
    b25 = b24[-2]
    if(b25 = =0):
        b19 = b19+"I am sorry! I don't understand you"
        return b19
    else:
        b19 = b19+b6[b23]
        return b19
def fonk8(b26):
    b19 = ''
    b8.append(b26)
    b20 = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    b21 = b20.fit_transform(b8)
    b22 = cosine_similarity(b21[-1], b21)
    b23 = b22.argsort()[0][-2]
    b24 = b22.flatten()
    b24.sort()
    b25 = b24[-2]
    if(b25 = =0):
        b19 = b19+"I am sorry! I don't understand you"
        return b19
    else:
        b19 = b19+b8[b23]
        return b19
def fonk9(b26):
    b26 = b26.lower()
    b27 = " module "
    b28 = " module"
    b29 = "module "
    if(b26!='bye'):
        if(b26 = ='thanks' or b26=='thank you' ):
            b30 = False
            return "You are welcome.."
        elif(fonk5(b26)!=None):
            return fonk5(b26)
        else:
            if(b26.find(b27) != -1 or b26.find(b28) != -1 or b26.find(b29) != -1):
                return fonk8(b26)
                b8.remove(b26)
            elif(fonk3(b26)!=None):
                return fonk3(b26)
            elif(b26.find("your name") != -1 or b26.find(" your name") != -1 or b26.find("your name ") != -1 or b26.find(" your name ") != -1):
                return fonk6(b26)
            elif(fonk4(b26)!=None):
                return fonk4(b26)
            else:
                return fonk7(b26)
                b6.remove(b26)
    else:
        b30 = False
        return "Bye! take care.."