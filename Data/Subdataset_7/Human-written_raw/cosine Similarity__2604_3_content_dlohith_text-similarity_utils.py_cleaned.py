import math
from scipy import spatial
def fonk1(term, allDocuments):
  a1 = 0
  for doc in allDocuments:
    if term.lower() in doc.lower().split():
      a1 = a1 + 1
  if a1 > 0:
    return 1.0 + math.log(float(len(allDocuments)) / a1)
  else:
    return 1.0
def fonk2(term, document):
  b1 = document.lower().split()
  return b1.count(term.lower()) / float(len(b1))
def fonk3(document, allDocuments):
  b2 = document.lower().split()
  b3 = []
  for term in b2:
    b4 = fonk2(term, document)
    b5 = fonk1(term, allDocuments)
    b6 = b4 * b5
    b3.append(b6)
  return b3
def fonk4(query,document):
  b7 = abs(len(query) - len(document))
  b8 = [0] * b7
  if(len(query) > len(document)):
    document.extend(b8)
  elif(len(document) > len(query)):
    query.extend(b8)
  return 1 - spatial.distance.cosine(query, document)