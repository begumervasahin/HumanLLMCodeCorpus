import utils
import json
doc_tfidfs = {}
data = {}
with open("data.csv", "r") as file:
    for line in file:
        parts = line.split(",")
        data[parts[0].strip("'")] = parts[1].strip("'")
questions = list(data.keys())
with open("stack-tfidf.json", "r") as file:
    doc_tfidfs = json.load(file)
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