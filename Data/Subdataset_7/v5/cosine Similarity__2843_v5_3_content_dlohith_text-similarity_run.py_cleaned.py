import utils
import json
def fonk1(file_path):
    b1 = {}
    with open(file_path, "r") as file:
        for line in file:
            b2 = line.split(",")
            b1[b2[0].strip("'")] = b2[1].strip("'")
    return b1
def fonk2(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
def fonk3(b8, b6, b7, b1):
    a1 = -1
    b3 = ""
    print("Calculating TF-IDF for the b8 with all b6 as reference ...")
    b4 = utils.getTFIDF(b8, b6)
    print("Calling cosine b5 between all the b6 to find the best match ...")
    for question in b6:
        b5 = utils.cosineSimilarity(b4, b7[question])
        if b5 > a1:
            a1 = b5
            b3 = question
    return b3, a1, b1[b3]
b1 = fonk1("b1.csv")
b6 = list(b1.keys())
b7 = fonk2("stack-tfidf.json")
while True:
    b8 = input("Please enter a question: ")
    print("\n")
    b3, a1, b9 = fonk3(b8, b6, b7, b1)
    print("-----------------------")
    print("Best question match:", b3)
    print("Max b5 score:", a1)
    print("Best answer:", b9)