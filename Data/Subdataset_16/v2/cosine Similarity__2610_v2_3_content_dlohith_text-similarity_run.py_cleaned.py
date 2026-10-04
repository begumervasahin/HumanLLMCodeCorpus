import json
import utils
b1 = {}
with open("b1.csv", "r") as file:
    for line in file:
        b2 = line.split(",")
        b3 = b2[0].strip().strip("'")
        b4 = b2[1].strip().strip("'")
        b1[b3] = b4
b5 = list(b1.keys())
with open("stack-tfidf.json", "r") as file:
    b6 = json.load(file)
while True:
    b7 = input("Please enter a b3 (or 'exit' to quit): ").strip()
    if b7.lower() == 'exit':
        break
    a1 = -1
    b8 = ""
    print("\n-----------------------")
    print(f"Calculating TF-IDF for the b7 '{b7}' with all b5 as reference ...")
    b9 = utils.getTFIDF(b7, b5)
    print("Calling cosine b10 between the b7 and all b5 to find the best match ...")
    for b3 in b5:
        b10 = utils.cosineSimilarity(b9, b6[b3])
        if b10 > a1:
            a1 = b10
            b8 = b3
    print(f"Best b3 match: '{b8}'")
    print(f"Max b10 score: {a1}")
    print(f"Best b4: {b1[b8]}")
    print("-----------------------\n")
print("Exiting the program.")