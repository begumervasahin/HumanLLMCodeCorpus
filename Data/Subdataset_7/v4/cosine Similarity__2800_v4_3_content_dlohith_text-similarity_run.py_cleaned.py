import utils
import json
b1 = {}
b2 = {}
with open("b2.csv", "r") as file:
    for line in file:
        b3 = line.split(",")
        b2[b3[0].strip("'")] = b3[1].strip("'")
b4 = list(b2.keys())
with open("stack-tfidf.json", "r") as file:
    b1 = json.load(file)
while True:
    b5 = input("Please enter a question: ")
    print("\n")
    a1 = -1
    b6 = ""
    print("-----------------------")
    print("Calculating TF-IDF for the b5 with all b4 as reference ...")
    b7 = utils.getTFIDF(b5, b4)
    print("Calling cosine b8 between all the b4 to find the best match ...")
    for question in b4:
        b8 = utils.cosineSimilarity(b7, b1[question])
        if b8 > a1:
            print(b8)
            a1 = b8
            b6 = question
    print("Best question match:", b6)
    print("Max b8 score:", a1)
    print("Best answer:", b2[b6])