import nltk
import re
from nltk.corpus import stopwords
def create_bow(tokenized, bags):
    for word in tokenized:
        if word not in bags:
            bags[word] = 1
        else:
            bags[word] += 1
    return bags
def calculate_matching(bags_dict, user_bags):
    matched = {}
    for faq in bags_dict:
        matched[faq] = []
        for word in user_bags:
            weight = 0
            if word in bags_dict[faq]:
                weight = float(user_bags[word] * bags_dict[faq][word]) / sum(bags_dict[faq].values())
            else:
                weight = 0.0
            matched[faq].append(weight)
    return matched
def preprocess_faq_data(table, bags_dict, regexp):
    with open("data.txt") as data_file:
        for line in data_file:
            question, answer = line.rstrip("\n").split("?")
            table[question] = answer
    for question in table:
        bags = {}
        processed_question = regexp.sub(' ', question)
        processed_answer = regexp.sub(' ', table[question])
        combined_text = processed_question.lower() + " " + processed_answer.lower()
        tokenized_text = nltk.word_tokenize(combined_text)
        bags_dict[question] = create_bow(tokenized_text, bags)
def calculate_tfidf(matched_weight, user_bow_keys, bags_dict):
    matching_results = {}
    for question in matched_weight:
        tfidf_score = 0.0
        for i in range(len(user_bow_keys)):
            idf = 0
            for bow in bags_dict.values():
                if user_bow_keys[i] in bow:
                    idf += 1
            if idf != 0:
                idf = 50.0 / idf
            tfidf_score += matched_weight[question][i] * idf
        matching_results[question] = tfidf_score
    return matching_results
def print_top_ten(matched_weight_sorted, table):
    matched_count = 0
    for question in matched_weight_sorted:
        if matched_count == 10:
            break
        print("\nQuestion: " + question + "\nMatching Score: " + str(matched_weight_next[question]))
        print("Answer: " + table[question])
        print("---")
        matched_count += 1
regexp = re.compile('[^a-zA-Z]')
faq_table = {}
faq_bags_dict = {}
stop_words = set(stopwords.words('english'))
preprocess_faq_data(faq_table, faq_bags_dict, regexp)
user_input = input("Enter a FAQ related to TOEFL: ")
user_tokenized = regexp.sub(' ', user_input)
user_tokenized1 = nltk.word_tokenize(user_tokenized.lower())
user_bow = create_bow(user_tokenized1, {})
matched_weight = calculate_matching(faq_bags_dict, user_bow)
matched_weight_next = calculate_tfidf(matched_weight, user_bow.keys(), faq_bags_dict)
matched_weight_sorted = sorted(matched_weight_next, key=matched_weight_next.get, reverse=True)
print("\n+++++++++++++++++++++++++++")
print("+Top 10 results for Task 2+")
print("+++++++++++++++++++++++++++")
print_top_ten(matched_weight_sorted, faq_table)