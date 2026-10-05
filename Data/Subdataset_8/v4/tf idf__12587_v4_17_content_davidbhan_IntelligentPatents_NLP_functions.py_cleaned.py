import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
def simplify_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    word_list = nltk.word_tokenize(text)
    filtered_text = [word for word in word_list if word not in stopwords.words('english')]
    lemma = nltk.wordnet.WordNetLemmatizer()
    result = ""
    for word in filtered_text:
        result += lemma.lemmatize(word) + " "
    return result.strip()
def similarity(text1, text2):
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform([text1, text2])
    return (tfidf * tfidf.T).A[0,1]
text1 = "hello I'm David, and I love my little bunny \n asdf fuck this code"
text2 = "hello I'm Juwon, and I love my big bear"
print("Similarity between original texts:", similarity(text1, text2))
simplified_text1 = simplify_text(text1)
simplified_text2 = simplify_text(text2)
print("Similarity between simplified texts:", similarity(simplified_text1, simplified_text2))
print("Simplified text:", simplify_text("hello I'm David, I was born on the best day of the best month because i'm the best of them all!"))