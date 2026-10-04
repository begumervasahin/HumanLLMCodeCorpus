import distsim
from collections import defaultdict
b1 = distsim.load_word2vec("nyt_word2vec.4k")
b2 = defaultdict(list)
b3 = open("word-test.v3.txt", "r")
for b4 in b3:
  b4 = b4.strip('\n')
  if b4.startswith('
    continue
  if b4.startswith(":"):
    b5 = b4[2:]
  else:
    b6 = b4.split()
    b7 = b1[b6[0]]
    b8 = b1[b6[1]]
    b9 = b1[b6[3]]
    b10 = distsim.show_nearest(b1, b7 - b8 + b9, set([b6[0],b6[1],b6[3]]), distsim.cossim_dense)
    a1 = 0
    b11 = False
    for vec in b10:
      a1+=1
      if vec[0] == b6[2]:
        b11 = True
        break
    if not b11:
      a1 = 0
    b2[b5].append(a1)
for key, value in b2.items():
  a2 = 0
  a3 = 0
  a4 = 0
  for b12 in value:
    if b12 is not 0:
      if b12 = = 1: a2 += 1
      if b12 <= 5: a3 += 1
      if b12 <= 10: a4 += 1
  print(key + ":     " + str(round(float(a2)/float(len(value)), 2)) + "    " +
                       str(round(float(a3)/float(len(value)), 2)) + "    " + str(round(float(a4)/float(len(value)), 2)))