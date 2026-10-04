import wikipedia
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import os
b1 = WordNetLemmatizer()
b2 = set(stopwords.b9("english"))
b3 = ['Alfa_Romeo', 'Aston_Martin', 'Audi', 'Automobile_Dacia', 'Bentley']
b4 = int(input('Broj Å¾eljenih najfrekventnijih kljuÄnih rijeÄi po dokumentu: '))
os.makedirs("Generated_txt", b5 = True)
b6 = {}
def fonk1(page_name):
    b7 = wikipedia.b7(page_name)
    return b7.content
def fonk2(file_path, content):
    with open(file_path, 'w', b8 = 'utf-8') as file:
        file.write(content)
def fonk3(file_path):
    with open(file_path, 'r', b8 = 'utf-8') as file:
        return file.read()
def fonk4(text):
    b9 = word_tokenize(text)
    b10 = [word.lower() for word in b9 if word.isalpha() or word.isnumeric()]
    b11 = [b1.lemmatize(word, pos="v") for word in b10 if word not in b2]
    return b11
def fonk5(text, max_features):
    b12 = TfidfVectorizer(max_features=max_features)
    b13 = b12.fit_transform([text])
    b14 = b12.get_feature_names_out()
    return b13, b14
def fonk6(file_path, b13, b14):
    with open(file_path, 'w', b8 = 'utf-8') as file:
        for col in b13.nonzero()[1]:
            file.write(f"{b13[0, col]} - {b14[col]}\n")
def fonk7(file_path, b14, b13):
    with open(file_path, 'w', b8 = 'utf-8') as file:
        for col in b13.nonzero()[1]:
            file.write(f"{b14[col]}\n")
for page_name in b3:
    b15 = fonk1(page_name)
    b16 = os.path.join("Generated_txt", f"{page_name}.txt")
    fonk2(b16, b15)
    b17 = fonk3(b16)
    b11 = fonk4(b17)
    b18 = ", ".join(b11)
    b19 = os.path.join("Generated_txt", f"{page_name}_Lemmatized.txt")
    fonk2(b19, b18)
    print(f"{page_name:30} Broj rijeÄi: {len(b11)}")
    b13, b14 = fonk5(b18, b4)
    b20 = os.path.join("Generated_txt", f"{page_name}_Weights.txt")
    fonk6(b20, b13, b14)
    b21 = os.path.join("Generated_txt", f"{page_name}_Top_Keywords.txt")
    fonk7(b21, b14, b13)
    b22 = fonk3(b21).splitlines()
    b6[page_name] = b22
    print("\n")
print("======================================== b23 = =======================================")
print(f"Preuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za {b4} najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.")
print("======================================== b23 = =======================================")