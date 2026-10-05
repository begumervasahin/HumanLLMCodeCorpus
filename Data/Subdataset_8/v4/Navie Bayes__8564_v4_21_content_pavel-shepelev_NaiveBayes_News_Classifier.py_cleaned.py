from collections import Counter
trainsize = 6000
testsize = 15000
fname = "news_train.txt"
testfname = "news_test.txt"
category = []
content = []
names = []
with open(fname, encoding='utf-8') as f:
    articles = f.readlines()
    for article in articles:
        category.append(article.split("\t", 1)[0])
        content.append(article.split("\t", 1)[1].strip())
names = list(set(category))
def IndexSelect(name):
    indices = []
    for i in range(trainsize):
        if category[i] == name:
            indices.append(i)
    return indices
def CommonWords(categ, testdic):
    testcounts = dict.fromkeys(testdic, 0)
    for i in IndexSelect(categ):
        traindic = dict(Counter(content[i].split()))
        for key in traindic:
            if key in testdic:
                testcounts[key] += traindic[key]
    return testcounts
def Prior(categ):
    return len(IndexSelect(categ)) / len(category)
def WordsnVoc(categ):
    totalwords = 0
    voc = []
    for i in IndexSelect(categ):
        traindic = dict(Counter(content[i].split()))
        totalwords += len(traindic.keys())
        voc = list(set(voc + list(traindic.keys())))
    return totalwords, voc
values = []
voc = []
for categ in names:
    voc = list(set(WordsnVoc(categ)[1] + voc))
    values.append(WordsnVoc(categ)[0])
totalwords = dict(zip(names, values))
voclength = len(voc)
def Main(testdic):
    probs = []
    for categ in names:
        testcounts = CommonWords(categ, testdic)
        condprob = dict.fromkeys(testcounts, 0)
        p = 1
        for word in testcounts:
            condprob[word] = 10000 * (testcounts[word] + 1) / (totalwords[categ] + voclength)
            p *= condprob[word]
        p *= Prior(categ)
        probs.append(p)
    val, idx = max((val, idx) for (idx, val) in enumerate(probs))
    return names[idx]
tcontent = []
with open(testfname, encoding='utf-8') as f:
    tarticles = f.readlines()
with open('answer.txt', 'w', encoding="utf8") as answerfile:
    for i in range(testsize):
        testdict = dict(Counter(tarticles[i].split()))
        answer = Main(testdict)
        answerfile.write(answer + '\n')