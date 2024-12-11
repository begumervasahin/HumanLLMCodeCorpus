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
b5 = {}
a1 = 0
b6 = {}
b7 = {}
for file in b4:
	with open(file) as f:
		for line in f:
			b6 = {}
			b8 = json.loads(line)
			b9 = b8['b9']
			a1+=1
			if b9 != None:
				for word in b9.split():
					if word in b5:
						b5[word]+=1
					else:
						b5[word]=1
					if word in b6:
						b6[word]+=1
					else:
						b6[word]=1
        	for a in b6:
				if a in b7:
					b7[a]+=1
				else:
					b7[a]=1
b10 = {}
for a in b7:
    b10[a]=b5[a]*b7[a]*b7[a]
b11 = sorted(b10.items(), key=operator.itemgetter(1), reverse=True)
a1 = 50
for d in b11:
    a1-=1
    if a1<0:
        break
    print d[0],':',d[1]
a1 = 50
for d in b11:
    a1-=1
    if a1<0:
        break
    print d[0]