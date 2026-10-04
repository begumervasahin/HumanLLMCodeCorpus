import wikipedia
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import networkx as nx
import matplotlib.pyplot as plt
b1 = WordNetLemmatizer()
b2 = set(stopwords.b11("english"))
b3 = ['Alfa_Romeo', 'Aston_Martin', 'Audi', 'Automobile_Dacia', 'Bentley']
print("\n")
b4 = int(input('Broj Å¾eljenih najfrekventnijih kljuÄnih rijeÄi po dokumentu: '))
a1 = 0
b5 = {}
for i in b3:
    b6 = wikipedia.b6(i)
    b7 = b6.content
    b8 = str(i) + ".txt"
    b9 = open("Generated_txt/" + b8, 'w', encoding = 'utf-8')
    b9.write(b7)
    b9.close()
    b9 = open("Generated_txt/" + b8, "r", encoding = 'utf-8')
    b10 = b9.read()
    b11 = word_tokenize(b10)
    b9.close()
    b12 = [word.lower() for word in b11 if word.isalpha() or word.isnumeric()]
    b13 = str(i) + "_Lemmatized.txt"
    b9 = open("Generated_txt/" + b13, 'w', encoding = 'utf-8')
    a2 = 0
    for word in b12:
        b14 = b1.lemmatize(word, pos = "v")
        if b14 not in b2:
            b9.write(b14)
            b9.write(", ")
            a2 += 1
    b9.close()
    print("{0:30}{1:5}{2:7}".format(i, "Broj rijeÄi:", a2))
    b9 = open("Generated_txt/" + b13, 'r', encoding = 'utf-8')
    b10 = b9.read()
    b15 = TfidfVectorizer(max_features = b4)
    b16 = b15.fit_transform([b10])
    b9.close()
    b17 = str(i) + "_Weights.txt"
    b9 = open("Generated_txt/" + b17, 'w', encoding = 'utf-8')
    b18 = str(i) + "_Top_Keywords.txt"
    b9 = open("Generated_txt/" + b18, 'w', encoding = 'utf-8')
    b19 = b15.get_feature_names()
    for col in b16.nonzero()[1]:
        print (b19[col], ' - ', b16[0, col])
    with open("Generated_txt/" + b17, 'w') as f:
        for col in b16.nonzero()[1]:
            print(b16[0, col], ' - ', b19[col], b9 = f)
    with open("Generated_txt/" + b18, 'w') as f:
        for col in b16.nonzero()[1]:
            print(b19[col], b9 = f)
    b9 = open("Generated_txt/" + b18, 'r')
    b20 = b9.read().splitlines()
    print("\n")
    b5["{}".format(i)]= b20
    b9.close()
print("======================================== b21 = =======================================\nPreuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za", b4, "najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.\n======================================== b21 ========================================")
print("\n\n")
print("\n\n")
print("\n\n")