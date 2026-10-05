import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
with open('chatbot.txt', 'r', b1 = 'ignore') as file:
    b2 = file.read().lower()
b3 = nltk.sent_tokenize(b2)
b4 = nltk.word_tokenize(b2)
nltk.download('punkt')
nltk.download('wordnet')
b5 = nltk.stem.WordNetLemmatizer()
def fonk1(b6):
    return [b5.lemmatize(token) for token in b6]
def fonk2(text):
    b6 = nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))
    return fonk1(b6)
b7 = ("hello", "hi", "greetings", "sup", "what's up", "hey")
b8 = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def fonk3(sentence):
    for word in sentence.split():
        if word.lower() in b7:
            return random.choice(b8)
def fonk4(b17):
    b9 = ''
    b3.append(b17)
    b10 = TfidfVectorizer(tokenizer=normalize_text, stop_words='english')
    b11 = b10.fit_transform(b3)
    b12 = cosine_similarity(b11[-1], b11)
    b13 = b12.argsort()[0][-2]
    b14 = b12.flatten()
    b14.sort()
    b15 = b14[-2]
    if b15 = = 0:
        b9 = "I am sorry! I don't understand you"
    else:
        b9 = b3[b13]
    return b9
print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type 'Bye'!")
b16 = True
while b16:
    b17 = input().lower()
    if b17 != 'bye':
        if b17 in ['thanks', 'thank you']:
            b16 = False
            print("ROBO: You are welcome..")
        else:
            b18 = fonk3(b17)
            if b18:
                print("ROBO: " + b18)
            else:
                print("ROBO:", b19 = " ")
                print(fonk4(b17))
                b3.remove(b17)
    else:
        b16 = False
        print("ROBO: Bye! Take care..")