import json
import utils
data = {}
with open("data.csv", "r") as file:
    for line in file:
        question, answer = line.strip().split(",")
        data[question.strip("'")] = answer.strip().strip("'")
questions = list(data.keys())
with open("stack-tfidf.json", "r") as file:
    docTFIDFs = json.load(file)
while True:
    query = input("Please enter a question (or 'exit' to quit): ").strip()
    if query.lower() == 'exit':
        break
    maxSimilarity = -1
    bestQuestion = ""
    print("\n-----------------------")
    print(f"Calculating TF-IDF for the query '{query}' with all questions as reference ...")
    queryTFIDF = utils.getTFIDF(query, questions)
    print("Calling cosine similarity between the query and all questions to find the best match ...")
    for question in questions:
        similarity = utils.cosineSimilarity(queryTFIDF, docTFIDFs[question])
        if similarity > maxSimilarity:
            maxSimilarity = similarity
            bestQuestion = question
    print(f"Best question match: '{bestQuestion}'")
    print(f"Max similarity score: {maxSimilarity}")
    print(f"Best answer: {data[bestQuestion]}")
    print("-----------------------\n")
print("Exiting the program.")