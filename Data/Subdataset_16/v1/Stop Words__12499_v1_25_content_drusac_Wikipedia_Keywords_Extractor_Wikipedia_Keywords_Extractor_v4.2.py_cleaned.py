import wikipedia
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import os
b1 = WordNetLemmatizer()
b2 = set(stopwords.b12("english"))
b3 = ['Alfa_Romeo', 'Aston_Martin', 'Audi', 'Automobile_Dacia', 'Bentley']
b4 = int(input('Broj Å¾eljenih najfrekventnijih kljuÄnih rijeÄi po dokumentu: '))
os.makedirs("Generated_txt", b5 = True)
b6 = {}
for page_name in b3:
    b7 = wikipedia.b7(page_name)
    b8 = b7.content
    b9 = os.path.join("Generated_txt", f"{page_name}.txt")
    with open(b9, 'w', b10 = 'utf-8') as file:
        file.write(b8)
    with open(b9, 'r', b10 = 'utf-8') as file:
        b11 = file.read()
    b12 = word_tokenize(b11)
    b13 = [word.lower() for word in b12 if word.isalpha() or word.isnumeric()]
    b14 = [b1.lemmatize(word, pos="v") for word in b13 if word not in b2]
    b15 = os.path.join("Generated_txt", f"{page_name}_Lemmatized.txt")
    with open(b15, 'w', b10 = 'utf-8') as file:
        file.write(", ".join(b14))
    print(f"{page_name:30} Broj rijeÄi: {len(b14)}")
    with open(b15, 'r', b10 = 'utf-8') as file:
        b11 = file.read()
    b16 = TfidfVectorizer(max_features=b4)
    b17 = b16.fit_transform([b11])
    b18 = b16.get_feature_names_out()
    b19 = os.path.join("Generated_txt", f"{page_name}_Weights.txt")
    with open(b19, 'w', b10 = 'utf-8') as file:
        for col in b17.nonzero()[1]:
            file.write(f"{b17[0, col]} - {b18[col]}\n")
    b20 = os.path.join("Generated_txt", f"{page_name}_Top_Keywords.txt")
    with open(b20, 'w', b10 = 'utf-8') as file:
        for col in b17.nonzero()[1]:
            file.write(f"{b18[col]}\n")
    with open(b20, 'r', b10 = 'utf-8') as file:
        b21 = file.read().splitlines()
    b6[page_name] = b21
    print("\n")
print("======================================== b22 = =======================================")
print(f"Preuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za {b4} najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.")
print("======================================== b22 = =======================================")