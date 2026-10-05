import utils
import json
def load_data_from_csv(file_path):
    data = {}
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split(",")
            data[parts[0].strip("'")] = parts[1].strip("'")
    return data
def load_tfidfs_from_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
def find_best_match(query, questions, doc_tfidfs, data):
    max_similarity = -1
    best_question = ""
    print("Calculating TF-IDF for the query with all questions as reference ...")
    query_tfidf = utils.getTFIDF(query, questions)
    print("Calling cosine similarity between all the questions to find the best match ...")
    for question in questions:
        similarity = utils.cosineSimilarity(query_tfidf, doc_tfidfs[question])
        if similarity > max_similarity:
            max_similarity = similarity
            best_question = question
    return best_question, max_similarity, data[best_question]
data = load_data_from_csv("data.csv")
questions = list(data.keys())
doc_tfidfs = load_tfidfs_from_json("stack-tfidf.json")
while True:
    query = input("Please enter a question: ")
    print("\n")
    best_question, max_similarity, best_answer = find_best_match(query, questions, doc_tfidfs, data)
    print("-----------------------")
    print("Best question match:", best_question)
    print("Max similarity score:", max_similarity)
    print("Best answer:", best_answer)