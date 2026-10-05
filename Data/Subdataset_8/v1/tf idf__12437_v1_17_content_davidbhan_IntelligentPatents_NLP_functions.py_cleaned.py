import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
def simplifyText(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    word_list = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_text = [word for word in word_list if word not in stop_words]
    lemma = nltk.wordnet.WordNetLemmatizer()
    result = " ".join([lemma.lemmatize(word) for word in filtered_text])
    return result
def similarity(text1, text2):
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform([text1, text2])
    return (tfidf * tfidf.T).A[0,1]
text1 = "hello I'm David, and I love my little bunny \n asdf fuck this code"
text2 = "hello I'm Juwon, and I love my big bear"
print(similarity(text1, text2))
print(similarity(simplifyText(text1), simplifyText(text2)))
print(simplifyText("hello I'm David, I was born on the best day of the best month because i'm the best of them all!"))