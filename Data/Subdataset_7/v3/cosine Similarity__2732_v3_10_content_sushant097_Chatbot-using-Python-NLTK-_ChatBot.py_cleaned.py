import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('punkt')
nltk.download('wordnet')
with open('chatbot.txt', 'r', b1 = 'ignore') as file:
    b2 = file.read().lower()
b3 = nltk.sent_tokenize(b2)
b4 = nltk.word_tokenize(b2)
b5 = nltk.stem.WordNetLemmatizer()
def fonk1(tokens):
    return [b5.lemmatize(token) for token in tokens]
def fonk2(text):
    return fonk1(nltk.word_tokenize(text.lower().translate(dict((ord(punct), None) for punct in string.punctuation))))
b6 = ("hello", "hi", "greetings", "sup", "what's up", "hey")
b7 = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def fonk3(sentence):
    for word in sentence.split():
        if word.lower() in b6:
            return random.choice(b7)
def fonk4(b16):
    b8 = ''
    b3.append(b16)
    b9 = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    b10 = b9.fit_transform(b3)
    b11 = cosine_similarity(b10[-1], b10)
    b12 = b11.argsort()[0][-2]
    b13 = b11.flatten()
    b13.sort()
    b14 = b13[-2]
    if b14 = = 0:
        b8 = "I am sorry! I don't understand you"
    else:
        b8 = b3[b12]
    return b8
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type 'Bye'!")
b15 = True
while b15:
    b16 = input().lower()
    if b16 != 'bye':
        if b16 in ['thanks', 'thank you']:
            b15 = False
            print("ROBO: You are welcome..")
        else:
            b17 = fonk3(b16)
            if b17:
                print("ROBO: " + b17)
            else:
                print("ROBO:", b18 = " ")
                print(fonk4(b16))
                b3.remove(b16)
    else:
        b15 = False
        print("ROBO: Bye! Take care..")