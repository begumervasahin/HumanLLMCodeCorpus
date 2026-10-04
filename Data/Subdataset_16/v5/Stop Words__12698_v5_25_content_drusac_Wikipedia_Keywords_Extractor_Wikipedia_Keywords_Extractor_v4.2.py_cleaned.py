import wikipedia
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import os
b1 = WordNetLemmatizer()
b2 = set(stopwords.b9("english"))
b3 = ['Alfa_Romeo', 'Aston_Martin', 'Audi', 'Automobile_Dacia', 'Bentley']
b4 = "Generated_txt"
os.makedirs(b4, b5 = True)
b6 = int(input('Broj Å¾eljenih najfrekventnijih kljuÄnih rijeÄi po dokumentu: '))
b7 = {}
def fonk1(file_path, text):
    with open(file_path, 'w', b8 = 'utf-8') as file:
        file.write(text)
def fonk2(file_path):
    with open(file_path, 'r', b8 = 'utf-8') as file:
        return file.read()
def fonk3(text):
    b9 = word_tokenize(text)
    return [word.lower() for word in b9 if word.isalpha() or word.isnumeric()]
def fonk4(b9):
    return [b1.lemmatize(word, b10 = "v") for word in b9 if word not in b2]
def fonk5(text, num_keywords):
    b11 = TfidfVectorizer(max_features=num_keywords)
    b12 = b11.fit_transform([text])
    b13 = b11.get_feature_names_out()
    b14 = [b13[col] for col in b12.nonzero()[1]]
    b15 = {b13[col]: b12[0, col] for col in b12.nonzero()[1]}
    return b14, b15
for page_name in b3:
    b16 = wikipedia.b16(page_name)
    b17 = b16.content
    b18 = os.path.join(b4, f"{page_name}.txt")
    fonk1(b18, b17)
    b19 = fonk2(b18)
    b20 = fonk3(b19)
    b21 = fonk4(b20)
    b22 = os.path.join(b4, f"{page_name}_Lemmatized.txt")
    fonk1(b22, ", ".join(b21))
    print(f"{page_name:30} Broj rijeÄi: {len(b21):5}")
    b14, b15 = fonk5(" ".join(b21), b6)
    b23 = os.path.join(b4, f"{page_name}_Weights.txt")
    fonk1(b23, "\n".join([f"{weight} - {word}" for word, weight in b15.items()]))
    b24 = os.path.join(b4, f"{page_name}_Top_Keywords.txt")
    fonk1(b24, "\n".join(b14))
    b7[page_name] = b14
    print("\n".join(b14))
    print("\n")
print("=" * 88)
print("REPORT")
print(f"Preuzet tekst pojedine stranice sa Wikipedije, odraÄena lematizacija i izbacivanje stop rijeÄi, izraÄunate teÅ¾ine za {b6} najfrekventnijih kljuÄnih rijeÄi. Generirano 4 .txt dokumenta za pojedinu Wikipedia stranicu.")
print("=" * 88)
print("\n\n")