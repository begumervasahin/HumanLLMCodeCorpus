import json
import utils
with open("stack-tfidf.json", "r") as tfidf_file:
    doc_tfidfs = json.load(tfidf_file)
data = {}
with open("data.csv", "r") as data_file:
    for line in data_file:
        key, value = line.strip().split(",")
        data[key.strip("'")] = value.strip("'")
questions = list(data.keys())
while True:
    query = input("Please enter a question: ")
    print("\n")
    max_similarity = -1
    best_question = ""
    print("-----------------------")
    print("Calculating TF-IDF for the query with all questions as reference ...")
    query_tfidf = utils.getTFIDF(query, questions)
    print("Calling cosine similarity between all the questions to find the best match ...")
    for question in questions:
        similarity = utils.cosineSimilarity(query_tfidf, doc_tfidfs[question])
        if similarity > max_similarity:
            print(similarity)
            max_similarity = similarity
            best_question = question
    print("Best question match:", best_question)
    print("Max similarity score:", max_similarity)
    print("Best answer:", data[best_question])