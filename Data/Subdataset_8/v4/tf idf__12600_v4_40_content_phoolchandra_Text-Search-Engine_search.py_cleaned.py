import os
import sys
import glob
text_directory = "Texts"
if not os.path.exists(text_directory):
    os.makedirs(text_directory)
arg_list = glob.glob("./Texts/*.txt")
argv = " ".join("\"" + arg + "\"" for arg in arg_list)
file_list = glob.glob("./Text/*.txt")
print("1) To create index and search in folder")
print("2) To search in folder")
print("3) To convert PDF to text")
print("4) Search in file by KMP")
print("5) Recently modified or created files")
print("6) Exit program\n")
q = int(input())
while q != 6:
    if q == 1:
        os.system("python ./createIndex_tf.py " + argv)
        os.system("python ./queryIndex_tfidf.py ")
    elif q == 2:
        os.system("python ./queryIndex_tf.py ")
    elif q == 3:
        os.system("python ./pdftotext.py ")
    elif q == 4:
        ar = sys.stdin.readline()
        os.system("python ./kmp.py " + ar)
    elif q == 5:
        os.system("python ./time.py " + argv)
    print("\n1) To create index and search in folder")
    print("2) To search in folder")
    print("3) To convert PDF to text")
    print("4) Search in file by KMP")
    print("5) Recently modified or created files")
    print("6) Exit program\n")
    q = int(input())
print("Exiting program...")