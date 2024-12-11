import os
import time
import nltk
import math
import pylab
b1 = {}
def fonk1():
 global b1
 b2 = open("ClusterNames.csv","r")
 b3 = []
 for line in b2 :
  b3 = line.split(",")
  b1[b3[0]] = b3[1][0:len(b3[1])-1]
def fonk2():
 b2 = open("Hierarchies.csv","r")
 b3 = []
 b4 = []
 b5 = "{\n\"name\": \"Entire Dataset\",\n\"children\": [\n"
 for line in b2 :
  b3 = line.split(",")
  b4 = b3[1].split(" ")[0:-1]
  b5 = b5 + "{\n\"name\": " + "\"" + b3[0] + "\",\n"
  b5 = b5 + "\"children\": [\n"
  for cluster in b4 :
    if b4.index(cluster) != (len(b4)-1) :
     b5 = b5 + "{\"name\": " + "\""+b1[cluster] +"\" , " + "\"size\": " + " 3000 },\n"
    else :
     b5 = b5 + "{\"name\": " + "\""+b1[cluster] +"\" , " + "\"size\": " + " 3000 }\n]\n},\n"
 b5 = b5[0:-2] + "\n]\n}\n"
 print b5
 b2 = open("newjson.json","w")
 b2.write(b5)
 b2.close()
fonk1()
print b1
fonk2()