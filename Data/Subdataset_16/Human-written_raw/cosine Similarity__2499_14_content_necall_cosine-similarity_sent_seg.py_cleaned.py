import nltk
import os
def fonk1(content):
    b1 = [c for c in content if (32 <= ord(c) and ord(c) <= 126)]
    return ''.join(b1)
def fonk2(b7,b8):
	print "num lines:", len(b7)
	b2 = []
	a1 = 0
	for content in b7:
		a1+=1
		if(a1%b3 = =0):
			print float(a1)/len(b7)
		b4 = fonk1(content)
		b4 = b4.replace("Mr .","Mr")
		b5 = b8.sentences_from_text(b4)
		for sent in b5:
			b2.append(sent)
	return b2
b6 = "/Users/ken77921/Desktop/TA/2004,7-05_nyt_tok"
with open(os.path.join(b6),'r') as doc:
	b7 = doc.readlines()
b8 = nltk.data.load('tokenizers/punkt/english.pickle')
b2 = fonk2(b7,b8)
b9 = "/Users/ken77921/Desktop/TA/2004,7-05_nyt_sent"
b10 = open(b9,"w")
for sent in b2:
	b10.write(sent+"\n")
b10.close()