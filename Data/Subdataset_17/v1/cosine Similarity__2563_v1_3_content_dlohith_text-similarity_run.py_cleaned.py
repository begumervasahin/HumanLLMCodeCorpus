import json
import utils
data = {}
with open("data.csv", "r") as ins:
    for line in ins:
        arr = line.split(",")
        data[arr[0].split('\'')[1]] = arr[1].split('\'')[1]
questions = list(data.keys())
with open("stack-tfidf.json", "r") as f:
    docTFIDFs = json.load(f)
while True:
    query = input("Please enter a question (or 'exit' to quit): ")
    print("\n")
    if query.lower() == 'exit':
        break
    maxSimilarity = -1
    bestQuestion = ""
    print("-----------------------")
    print("Calculating TF-IDF for the query with all questions as reference ...")
    queryTFIDF = utils.getTFIDF(query, questions)
    print("Calling cosine similarity between the query and all questions to find best match ...")
    for question in questions:
        similarity = utils.cosineSimilarity(queryTFIDF, docTFIDFs[question])
        if similarity > maxSimilarity:
            maxSimilarity = similarity
            bestQuestion = question
    print("Best question match : " + bestQuestion)
    print("Max similarity score : " + str(maxSimilarity))
    print("Best answer : " + data[bestQuestion])
    print("-----------------------\n")
print("Exiting the program.")