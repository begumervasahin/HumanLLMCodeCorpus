import os
import sys
import glob
def fonk1(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def fonk2(directory):
    return glob.glob(os.path.join(directory, "*.txt"))
def fonk3():
    b1 = print(b1)
def fonk4():
    b2 = "Texts"
    fonk1(b2)
    b3 = fonk2(b2)
    b4 = " ".join(f'"{arg}"' for arg in b3)
    fonk3()
    b5 = int(input("Choose an option: "))
    while b5 != 6:
        if b5 = = 1:
            os.system(f"python ./createIndex_tf.py {b4}")
            os.system("python ./queryIndex_tfidf.py")
        elif b5 = = 2:
            os.system("python ./queryIndex_tf.py")
        elif b5 = = 3:
            os.system("python ./pdftotext.py")
        elif b5 = = 4:
            b6 = input("Enter search string: ")
            os.system(f"python ./kmp.py {b6}")
        elif b5 = = 5:
            os.system(f"python ./time.py {b4}")
        else:
            print("Invalid option, please try again.")
        fonk3()
        b5 = int(input("Choose an option: "))
    print("Exiting program.")
if b7 = = "__main__":
    fonk4()