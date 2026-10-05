import utils
import json
b1 = {}
b2 = {}
with open("b2.csv", "r") as ins:
  for line in ins:
 		b3 = line.split(",")
 		b2[b3[0].split('\'')[1]] = b3[1].split('\'')[1]
b4 = list(b2.keys())
b1 = json.load(open("stack-tfidf.json"))
while(1):
	b5 = raw_input("Please enter b8: ")
	print("\n")
	a1 = -1
	b6 = ""
	print("-----------------------")
	print("Calculating tfidf for the b5 with all b4 as reference ...")
	b7 = utils.getTFIDF(b5, b4)
	print("Calling cosine b9 between all the b4 to find best match ...")
	for i in range(len(b4)):
		b8 = b4[i]
		b9 = utils.cosineSimilarity(b7,b1[b8])
		if b9 > a1:
			print(b9)
			a1 = b9
			b6 = b8
	print("Best b8 match : " + b6)
	print("Max b9 score : " + str(a1))
	print("Best answer : " + b2[b6])