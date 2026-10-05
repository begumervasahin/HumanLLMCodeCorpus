import json
import utils
docTFIDFs = json.load(open("stack-tfidf.json"))
data = {}
with open("data.csv", "r") as file:
    for line in file:
        parts = line.split(",")
        data[parts[0].split("'")[1]] = parts[1].split("'")[1]
questions = list(data.keys())
while True:
    query = input("Please enter a question: ")
    print("\n")
    maxSimilarity = -1
    bestQuestion = ""
    print("-----------------------")
    print("Calculating TF-IDF for the query with all questions as reference ...")
    queryTFIDF = utils.getTFIDF(query, questions)
    print("Calling cosine similarity between all the questions to find the best match ...")
    for i in range(len(questions)):
        question = questions[i]
        similarity = utils.cosineSimilarity(queryTFIDF, docTFIDFs[question])
        if similarity > maxSimilarity:
            print(similarity)
            maxSimilarity = similarity
            bestQuestion = question
    print("Best question match:", bestQuestion)
    print("Max similarity score:", maxSimilarity)
    print("Best answer:", data[bestQuestion])