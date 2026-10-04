import os
import json
import operator
def fonk1(dir):
    b1 = []
    b2 = [x[0] for x in os.walk(dir)]
    for subdir in b2:
        b3 = os.walk(subdir).next()[2]
        if (len(b3) > 0):
            for file in b3:
                b1.append(subdir + "/" + file)
    return b1
b4 = fonk1('extracted')
b4 = ['out.txt']
b5 = {}
a1 = 0
b6 = {}
b7 = {}
b8 = {}
a2 = 0
for file in b4:
	with open(file) as f:
		for line in f:
                        b9 = json.loads(line)
			b10 = b9['desc']
                        b6 = {}
			a1+=1
                        a2 = 0
                        b8 = {}
			if b10 != None:
				for word in b10.split():
                                        a2+=1.0
					if not "," in word and not "-" in word and word in b5:
						b5[word]+=1
					elif not "," in word and not "-" in word:
						b5[word]=1
					if not "," in word and not "-" in word and word in b6:
						b6[word]+=1
					elif not "," in word and not "-" in word:
						b6[word]=1
                                for a in b6:
                                    if a in b7:
                                        b7[a]+=1
                                    else:
                                        b7[a]=1
b11 = {}
for a in b7:
    b11[a]=b5[a]*b7[a]*b7[a]
b12 = sorted(b11.items(), key=operator.itemgetter(1), reverse=True)
a1 = 50
for d in b12:
    a1-=1
    if a1<0:
        break
    print d[0]