'''Chatbot In Python Using NLTK'''
import nltk
import numpy as np
import random
import string
b1 = open('chatbot.txt','r',errors = 'ignore')
b2 = b1.read()
b2 = b2.lower()
nltk.download('punkt')
nltk.download('wordnet')
b3 = nltk.sent_tokenize(b2)
b4 = nltk.word_tokenize(b2)
b3[:2]
b4[:2]
b5 = nltk.stem.WordNetLemmatizer()
def fonk1(tokens):
     '''LemTokens which will take as input the tokens and return normalized tokens.'''
     return [b5.lemmatize(token) for token in tokens]
b6 = dict((ord(punct), None) for punct in string.punctuation)
def fonk2(text):
    return fonk1(nltk.word_tokenize(text.lower().translate(b6)))
b7 = ("hello", "hi", "greetings", "sup", "what's up","hey",)
b8 = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def fonk3(sentence):
     for word in sentence.split():
          if word.lower() in b7:
               return random.choice(b8)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def fonk4(b17):
    b9 = ''
    b3.append(b17)
    b10 = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    b11 = b10.fit_transform(b3)
    b12 = cosine_similarity(b11[-1], b11)
    b13 = b12.argsort()[0][-2]
    b14 = b12.flatten()
    b14.sort()
    b15 = b14[-2]
    if(b15 = =0):
        b9 = b9+"I am sorry! I don't understand you"
        return b9
    else:
        b9 = b9+b3[b13]
        return b9
b16 = True
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(b16 = =True):
    b17 = input()
    b17 = b17.lower()
    if(b17!='bye'):
        if(b17 = ='thanks' or b17=='thank you' ):
            b16 = False
            print("ROBO: You are welcome..")
        else:
            if(fonk3(b17)!=None):
                print("ROBO: "+fonk3(b17))
            else:
                print("ROBO: ",b18 = "")
                print(fonk4(b17))
                b3.remove(b17)
    else:
        b16 = False
        print("ROBO: Bye! take care..")