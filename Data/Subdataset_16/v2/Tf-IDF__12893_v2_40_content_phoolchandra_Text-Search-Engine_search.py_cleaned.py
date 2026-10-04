import os
import sys
import glob
def fonk1(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def fonk2(directory):
    return " ".join([f'"{arg}"' for arg in glob.glob(f"{directory}/*.txt")])
def fonk3():
    b1 = print(b1)
    return int(input("Enter your b4: "))
def fonk4():
    b2 = "Texts"
    fonk1(b2)
    b3 = fonk2(b2)
    while True:
        b4 = fonk3()
        if b4 = = 1:
            os.system(f"python ./createIndex_tf.py {b3}")
            os.system("python ./queryIndex_tfidf.py")
        elif b4 = = 2:
            os.system("python ./queryIndex_tf.py")
        elif b4 = = 3:
            os.system("python ./pdftotext.py")
        elif b4 = = 4:
            b5 = input("Enter the string to search using KMP: ")
            os.system(f"python ./kmp.py {b5}")
        elif b4 = = 5:
            os.system(f"python ./time.py {b3}")
        elif b4 = = 6:
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")
if b6 = = "__main__":
    fonk4()