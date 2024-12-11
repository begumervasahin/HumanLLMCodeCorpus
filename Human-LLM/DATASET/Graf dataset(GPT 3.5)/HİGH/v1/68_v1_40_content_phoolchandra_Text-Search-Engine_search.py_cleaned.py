import os
import sys
import glob
b1 = "Texts"
if not os.path.exists(b1):
    os.makedirs(b1)
def fonk1():
    b2 = glob.glob("./Texts/*.txt")
    b3 = " ".join(['"' + arg + '"' for arg in b2])
    os.system("python ./createIndex_tf.py " + b3)
    os.system("python ./queryIndex_tfidf.py ")
def fonk2():
    os.system("python ./queryIndex_tf.py ")
def fonk3():
    os.system("python ./pdftotext.py ")
def fonk4():
    b4 = input("Enter search term: ")
    os.system("python ./kmp.py " + b4)
def fonk5():
    b2 = glob.glob("./Texts/*.txt")
    b3 = " ".join(['"' + arg + '"' for arg in b2])
    os.system("python ./time.py " + b3)
def fonk6():
    print("1) To create index and search in folder")
    print("2) To search in folder")
    print("3) To convert pdf to text")
    print("4) Search in file by KMP")
    print("5) Recently modified or created files")
    print("6) Exit program")
    while True:
        b5 = int(input("Enter your choice: "))
        if b5 = = 1:
            fonk1()
        elif b5 = = 2:
            fonk2()
        elif b5 = = 3:
            fonk3()
        elif b5 = = 4:
            fonk4()
        elif b5 = = 5:
            fonk5()
        elif b5 = = 6:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if b6 = = "__main__":
    fonk6()