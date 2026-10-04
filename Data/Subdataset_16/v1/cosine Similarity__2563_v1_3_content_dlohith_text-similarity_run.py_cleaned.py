import json
import utils
b1 = {}
with open("b1.csv", "r") as ins:
    for line in ins:
        b2 = line.split(",")
        b1[b2[0].split('\'')[1]] = b2[1].split('\'')[1]
b3 = list(b1.keys())
with open("stack-tfidf.json", "r") as f:
    b4 = json.load(f)
while True:
    b5 = input("Please enter a question (or 'exit' to quit): ")
    print("\n")
    if b5.lower() == 'exit':
        break
    a1 = -1
    b6 = ""
    print("-----------------------")
    print("Calculating TF-IDF for the b5 with all b3 as reference ...")
    b7 = utils.getTFIDF(b5, b3)
    print("Calling cosine b8 between the b5 and all b3 to find best match ...")
    for question in b3:
        b8 = utils.cosineSimilarity(b7, b4[question])
        if b8 > a1:
            a1 = b8
            b6 = question
    print("Best question match : " + b6)
    print("Max b8 score : " + str(a1))
    print("Best answer : " + b1[b6])
    print("-----------------------\n")
print("Exiting the program.")