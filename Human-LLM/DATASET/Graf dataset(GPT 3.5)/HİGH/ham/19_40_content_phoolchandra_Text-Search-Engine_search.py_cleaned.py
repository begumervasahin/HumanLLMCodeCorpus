import os
import sys
import glob
import string
b1 = "Texts"
if not os.path.exists(b1):
	os.makedirs(b1)
b2 = ""
b3 = glob.glob("./Texts/*.txt")
for arg in b3:
	b2 += "\""+arg+"\" "
b4 = glob.glob("./Text/*.txt")
print "1)to create index and search in folder\n2)to search in folder\n3)to convert pdf to text\n4)search in file by kmp\n5)recently modified or created files\n6)exit program\n"
b5 = int(input())
while b5 != 6:
	if b5 = =1:
    	 os.system("python ./createIndex_tf.py "+b2)
    	 os.system("python ./queryIndex_tfidf.py ")
	if b5 = =2:
    	 os.system("python ./queryIndex_tf.py ")
	if b5 = =3:
    	 os.system("python ./pdftotext.py ")
	if b5 = =4:
		 b6 = sys.stdin.readline()
		 os.system("python ./kmp.py "+b6)
	if b5 = =5:
    	 os.system("python ./time.py "+b2)
	print "\n1)to create index and search in folder\n2)to search in folder\n3)to convert pdf to text\n4)search in file by kmp\n5)recently modified or created files\n6)exit program\n"
	b5 = int(input())