import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
def simplify_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    word_list = nltk.word_tokenize(text)
    filtered_text = [word for word in word_list if word not in stopwords.words('english')]
    lemma = nltk.wordnet.WordNetLemmatizer()
    simplified_text = " ".join(lemma.lemmatize(word) for word in filtered_text)
    return simplified_text
def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity_score = (tfidf_matrix * tfidf_matrix.T).A[0, 1]
    return similarity_score
text1 = "hello I'm David, and I love my little bunny \n asdf fuck this code"
text2 = "hello I'm Juwon, and I love my big bear"
print("Similarity between original texts:", calculate_similarity(text1, text2))
simplified_text1 = simplify_text(text1)
simplified_text2 = simplify_text(text2)
print("Similarity between simplified texts:", calculate_similarity(simplified_text1, simplified_text2))
print("Simplified text:", simplify_text("hello I'm David, I was born on the best day of the best month because i'm the best of them all!"))