import json
import utils
b1 = {}
with open("b1.csv", "r") as file:
    for line in file:
        question, b2 = line.strip().split(",")
        b1[question.strip("'")] = b2.strip().strip("'")
b3 = list(b1.keys())
with open("stack-tfidf.json", "r") as file:
    b4 = json.load(file)
while True:
    b5 = input("Please enter a question (or 'exit' to quit): ").strip()
    if b5.lower() == 'exit':
        break
    a1 = -1
    b6 = ""
    print("\n-----------------------")
    print(f"Calculating TF-IDF for the b5 '{b5}' with all b3 as reference ...")
    b7 = utils.getTFIDF(b5, b3)
    print("Calling cosine b8 between the b5 and all b3 to find the best match ...")
    for question in b3:
        b8 = utils.cosineSimilarity(b7, b4[question])
        if b8 > a1:
            a1 = b8
            b6 = question
    print(f"Best question match: '{b6}'")
    print(f"Max b8 score: {a1}")
    print(f"Best b2: {b1[b6]}")
    print("-----------------------\n")
print("Exiting the program.")