import wikipedia
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import os
b1 = WordNetLemmatizer()
b2 = set(stopwords.b13("english"))
b3 = ['Alfa_Romeo', 'Aston_Martin', 'Audi', 'Automobile_Dacia', 'Bentley']
b4 = "Generated_txt"
os.makedirs(b4, b5 = True)
b6 = int(input('Broj Å¾eljenih najfrekventnijih kljuÄnih rijeÄi po dokumentu: '))
b7 = {}
for page_name in b3:
    b8 = wikipedia.b8(page_name)
    b9 = b8.content
    b10 = os.path.join(b4, f"{page_name}.txt")
    with open(b10, 'w', b11 = 'utf-8') as file:
        file.write(b9)
    with open(b10, "r", b11 = 'utf-8') as file:
        b12 = file.read()
        b13 = word_tokenize(b12)
    b14 = [word.lower() for word in b13 if word.isalpha() or word.isnumeric()]
    b15 = [b1.lemmatize(word, pos="v") for word in b14 if word not in b2]
    b16 = os.path.join(b4, f"{page_name}_Lemmatized.txt")
    with open(b16, 'w', b11 = 'utf-8') as file:
        file.write(", ".join(b15))
    print(f"{page_name:30} Broj rijeÄi: {len(b15):5}")
    b17 = TfidfVectorizer(max_features=b6)
    b18 = b17.fit_transform([" ".join(b15)])
    b19 = os.path.join(b4, f"{page_name}_Weights.txt")
    with open(b19, 'w', b11 = 'utf-8') as file:
        for col in b18.nonzero()[1]:
            file.write(f"{b18[0, col]} - {b17.get_feature_names_out()[col]}\n")
    b20 = os.path.join(b4, f"{page_name}_Top_Keywords.txt")
    b21 = [b17.get_feature_names_out()[col] for col in b18.nonzero()[1]]
    with open(b20, 'w', b11 = 'utf-8') as file:
        file.write("\n".join(b21))
    b7[page_name] = b21
    print("\n".join(b21))
    print("\n")
print("="*88)
print("REPORT")
print("Preuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za", b6, "najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.")
print("="*88)
print("\n\n")