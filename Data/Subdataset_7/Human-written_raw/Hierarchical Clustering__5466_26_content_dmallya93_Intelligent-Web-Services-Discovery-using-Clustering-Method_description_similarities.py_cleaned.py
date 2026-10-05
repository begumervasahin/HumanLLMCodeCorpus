import os
import nltk
import time
import pylab
import networkx
import re
from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
def fonk1(text):
 b1 = text.split(" ")
 b2 = []
 for word in b1 :
  if word in sw.b1():
    b1.remove(word)
  b2 = b2 + [word.lower()]
 b3 = nltk.PorterStemmer()
 b4 = [b3.stem(t) for t in b1]
 return b2
def fonk2(text):
 b1 = fonk1(text)
 return b1
def fonk3(wsi,wsj):
 print wsi
 print wsj
 a1 = 0
 a2 = 0
 b5 = object()
 b6 = object()
 b7 = object()
 try :
  for word1 in wsi:
   print word1
   b5 = wn.synsets(word1.strip("\\n"))
   if len(b5) > 0:
    b5 = b5[0]
    for word2 in wsj:
     b6 = wn.synsets(word2.strip("\\n"))
     if len(b6) > 0 :
      b6 = b6[0]
      b7 = str(type(b5.path_similarity(b6))).split(" ")[1]
      if re.search("None",b7):
       a2 = 0
      else :
       a2 = b5.path_similarity(b6)
      a1 = a1+a2
 except Exception,e:
  print str(e)
 a1 = a1/(len(wsi)*len(wsj) + 0.0)
 print a1
fonk3("I am loved by everyone","Everyone loves me")