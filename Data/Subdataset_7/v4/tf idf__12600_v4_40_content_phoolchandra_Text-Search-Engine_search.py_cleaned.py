import os
import sys
import glob
b1 = "Texts"
if not os.path.exists(b1):
    os.makedirs(b1)
b2 = glob.glob("./Texts/*.txt")
b3 = " ".join("\"" + arg + "\"" for arg in b2)
b4 = glob.glob("./Text/*.txt")
print("1) To create index and search in folder")
print("2) To search in folder")
print("3) To convert PDF to text")
print("4) Search in file by KMP")
print("5) Recently modified or created files")
print("6) Exit program\n")
b5 = int(input())
while b5 != 6:
    if b5 = = 1:
        os.system("python ./createIndex_tf.py " + b3)
        os.system("python ./queryIndex_tfidf.py ")
    elif b5 = = 2:
        os.system("python ./queryIndex_tf.py ")
    elif b5 = = 3:
        os.system("python ./pdftotext.py ")
    elif b5 = = 4:
        b6 = sys.stdin.readline()
        os.system("python ./kmp.py " + b6)
    elif b5 = = 5:
        os.system("python ./time.py " + b3)
    print("\n1) To create index and search in folder")
    print("2) To search in folder")
    print("3) To convert PDF to text")
    print("4) Search in file by KMP")
    print("5) Recently modified or created files")
    print("6) Exit program\n")
    b5 = int(input())
print("Exiting program...")