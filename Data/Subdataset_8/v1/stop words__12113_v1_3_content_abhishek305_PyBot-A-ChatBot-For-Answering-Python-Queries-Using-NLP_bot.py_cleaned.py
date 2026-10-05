import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
f = open('nlp_python_answer_finals.txt', 'r', errors='ignore')
m = open('modules_pythons.txt', 'r', errors='ignore')
raw = f.read().lower()
rawone = m.read().lower()
sent_tokens = nltk.sent_tokenize(raw)
sent_tokensone = nltk.sent_tokenize(rawone)
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
Introduce_Ans = ["My name is PyBot.", "My name is PyBot you can call me Pi.",
                 "I'm PyBot.", "My name is PyBot and my nickname is Pi. I am happy to solve your queries."]
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "hello", "I am glad! You are talking to me"]
Basic_Q = ("what is python?",)
Basic_Ans = ("Python is a high-level, interpreted, interactive and object-oriented scripting programming language."
             " Python is designed to be highly readable. It uses English keywords frequently where as other "
             "languages use punctuation, and it has fewer syntactical constructions than other languages.")
Basic_Om = ("what is module?", "what is module in python?")
Basic_AnsM = ["Consider a module to be the same as a code library.",
              "A file containing a set of functions you want to include in your application.",
              "A module can define functions, classes and variables. A module can also include runnable code. "
              "Grouping related code into a module makes the code easier to understand and use."]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
def basic(sentence):
    if sentence.lower() in Basic_Q:
        return Basic_Ans
def basicM(sentence):
    if sentence.lower() in Basic_Om:
        return random.choice(Basic_AnsM)
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)
def response(user_response, sent_tokens):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response = "I am sorry! I don't understand you"
    else:
        robo_response = sent_tokens[idx]
    return robo_response
def chat(user_response):
    user_response = user_response.lower()
    keyword = "module"
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            return "You are welcome.."
        elif basicM(user_response) is not None:
            return basicM(user_response)
        else:
            if keyword in user_response:
                return response(user_response, sent_tokensone)
            elif greeting(user_response) is not None:
                return greeting(user_response)
            elif "your name" in user_response:
                return IntroduceMe(user_response)
            elif basic(user_response) is not None:
                return basic(user_response)
            else:
                return response(user_response, sent_tokens)
    else:
        return "Bye! take care.."
print("PyBot: Hello! I am PyBot. I will answer your queries about Python. If you want to exit, type Bye.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("PyBot: Bye! Take care..")
        break
    else:
        print("PyBot:", chat(user_input))