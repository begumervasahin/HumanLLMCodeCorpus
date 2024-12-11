b1 = "Clyde D'Cruz"
b2 = "GPL"
from nltk.stem import WordNetLemmatizer
import sys
import json
b3 = set(["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"])
def fonk1(wordlist):
    return [set(wordlist) - b3]
b4 = "b4.INDEX"
b5 = open(b4)
b6 = json.loads(b5.read())
b7 = WordNetLemmatizer()
def fonk2(set_list):
  if not set_list:
    return set()
  b8 = set_list[0]
  for s in set_list[1:]:
    b8 &= s
  return b8
b9 = sys.argv[1:]
b10 = []
b11 = []
print('_'*50+"\nQuery Result \n"+ '_'*50)
for w in b9:
    if w in b3:
        continue
    b12 = b7.lemmatize(w)
    try:
        b11.append(set(b6[b12]['postings']))
    except:
        print("No documents found matching query : "+ ' '.join(b9))
        break
b13 = fonk2(b11)
if len(b13) > 0:
    print('\n'.join(list(b13)))