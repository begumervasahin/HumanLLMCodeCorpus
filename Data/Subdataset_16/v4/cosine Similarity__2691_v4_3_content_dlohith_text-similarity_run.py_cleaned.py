import utils
import json
b1 = {}
b2 = {}
with open("b2.csv", "r") as file:
    for line in file:
        question, b3 = line.strip().split(",")
        b2[question.strip("'")] = b3.strip().strip("'")
b4 = list(b2.keys())
with open("stack-tfidf.json", "r") as file:
    b1 = json.load(file)
while True:
    b5 = input("Please enter a question (or 'exit' to quit): ").strip()
    if b5.lower() == 'exit':
        break
    a1 = -1
    b6 = ""
    print("\n-----------------------")
    print(f"Calculating TF-IDF for the b5 '{b5}' with all b4 as reference ...")
    b7 = utils.getTFIDF(b5, b4)
    print("Calling cosine b8 between the b5 and all b4 to find the best match ...")
    for question in b4:
        b8 = utils.cosineSimilarity(b7, b1[question])
        if b8 > a1:
            a1 = b8
            b6 = question
    print(f"Best question match: '{b6}'")
    print(f"Max b8 score: {a1}")
    print(f"Best b3: {b2[b6]}")
    print("-----------------------\n")
print("Exiting the program.")