import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter
def calculate_idf(token, doc_freq):
    if any(char.isupper() for char in token):
        return -1.0
    if token in doc_freq:
        return doc_freq[token]
    else:
        return -1.0
def generate_query_vector(query_string, stop_words, stemmer, doc_freq):
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokens = tokenizer.tokenize(query_string.lower())
    filtered_tokens = [token for token in tokens if token not in stop_words]
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    token_freq = Counter(stemmed_tokens)
    query_vector = {}
    for token, freq in token_freq.items():
        idf = calculate_idf(token, doc_freq)
        if idf != -1.0:
            tf_idf = 1 + math.log(freq, 10)
            query_vector[token] = tf_idf * idf
    sum_sq = sum(query_vector[token] ** 2 for token in query_vector)
    query_vector_norm = {token: value / math.sqrt(sum_sq) for token, value in query_vector.items()}
    return query_vector_norm
def find_most_similar_paragraph(query_string, tf_idf_weights, debate_transcript):
    query_vector = generate_query_vector(query_string, stop_words, stemmer, doc_freq)
    paragraph_similarity = {}
    for para_id, weights in tf_idf_weights.items():
        similarity = sum(query_vector[token] * weights.get(token, 0) for token in query_vector)
        paragraph_similarity[para_id] = similarity
    max_similarity_value = max(paragraph_similarity.values())
    most_similar_para_id = max(paragraph_similarity, key=paragraph_similarity.get)
    if max_similarity_value == 0:
        return "NO MATCH\n", max_similarity_value
    else:
        return debate_transcript[most_similar_para_id], max_similarity_value
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
filename = './debate.txt'
file = open(filename, "r", encoding='UTF-8')
doc = file.readlines()
file.close()
debate_transcript = {}
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
stemmer = PorterStemmer()
for line in doc:
    if not line.isspace():
        tokens = tokenizer.tokenize(line.lower())
        filtered_tokens = [token for token in tokens if token not in stop_words]
        stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
        para_id = f"para {len(debate_transcript) + 1}"
        debate_transcript[para_id] = stemmed_tokens
tf = {para_id: Counter(tokens) for para_id, tokens in debate_transcript.items()}
N = len(debate_transcript)
doc_freq = {token: math.log(N / sum(1 for tokens in debate_transcript.values() if token in tokens), 10) for tokens in set(token for tokens in debate_transcript.values() for token in tokens)}
tf_idf_weights = {para_id: {token: tf[para_id][token] * doc_freq[token] for token in tf[para_id]} for para_id in debate_transcript}
for para_id in tf_idf_weights:
    sum_weights = math.sqrt(sum(weight ** 2 for weight in tf_idf_weights[para_id].values()))
    tf_idf_weights[para_id] = {token: weight / sum_weights for token, weight in tf_idf_weights[para_id].items()}
query_string = "What are the benefits of renewable energy?"
result, similarity_score = find_most_similar_paragraph(query_string, tf_idf_weights, debate_transcript)
print("Most similar paragraph:")
print(result)
print("Similarity score:", similarity_score)