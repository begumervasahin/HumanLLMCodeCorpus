import nltk
import re
from nltk.corpus import stopwords
def get_word_frequency(tokenized_text):
    word_frequency = {}
    for word in tokenized_text:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency
def calculate_weights(bags_dict, user_bags):
    weights = {}
    for faq in bags_dict:
        weights[faq] = []
        for word in user_bags:
            weight = 0
            if word in bags_dict[faq]:
                weight = (user_bags[word] * bags_dict[faq][word]) / sum(bags_dict[faq].values())
            weights[faq].append(weight)
    return weights
def preprocess_data(file_path, bags_dict, regexp):
    with open(file_path) as data:
        for line in data:
            question, answer = line.rstrip("\n").split("?")
            question = regexp.sub(' ', question)
            answer = regexp.sub(' ', answer)
            tmp = (question.lower() + " " + answer.lower()).split()
            tokenized_text = nltk.word_tokenize(" ".join(tmp))
            bags_dict[question] = get_word_frequency(tokenized_text)
def calculate_tfidf(matched_weights, user_bow_keys, bags_dict):
    tfidf_scores = {}
    for question in matched_weights:
        tfidf = 0.0
        for word in user_bow_keys:
            idf = sum(1 for bow in bags_dict.values() if word in bow)
            if idf != 0:
                idf = 50.0 / idf
            tfidf += matched_weights[question][user_bow_keys.index(word)] * idf
        tfidf_scores[question] = tfidf
    return tfidf_scores
def print_top_ten(matched_weight_sorted, table):
    for i, question in enumerate(matched_weight_sorted):
        if i == 10:
            break
        print("\n" + question + "? " + str(matched_weight_sorted[question]))
        print(table[question])
        print("---")
regexp = re.compile('[^a-zA-Z]')
table = {}
bags_dict = {}
stopwords_set = set(stopwords.words('english'))
preprocess_data("data.txt", bags_dict, regexp)
user_input = input("Enter a FAQ related to TOEFL: ")
user_tokenized = regexp.sub(' ', user_input)
user_tokenized = nltk.word_tokenize(user_tokenized.lower())
user_bow = get_word_frequency(user_tokenized)
matched_weights = calculate_weights(bags_dict, user_bow)
tfidf_scores = calculate_tfidf(matched_weights, user_bow.keys(), bags_dict)
sorted_tfidf_scores = dict(sorted(tfidf_scores.items(), key=lambda item: item[1], reverse=True))
print("\n+++++++++++++++++++++++++++")
print("+ Top 10 results for Task 2 +")
print("+++++++++++++++++++++++++++")
print_top_ten(sorted_tfidf_scores, table)