import os
import sys
import glob
b1 = "Texts"
if not os.path.exists(b1):
    os.makedirs(b1)
b2 = glob.glob("./Texts/*.txt")
b3 = " ".join([f'"{arg}"' for arg in b2])
b4 = def fonk1():
    print(b4)
    return int(input())
b5 = fonk1()
while b5 != 6:
    if b5 = = 1:
        os.system(f"python ./createIndex_tf.py {b3}")
        os.system("python ./queryIndex_tfidf.py")
    elif b5 = = 2:
        os.system("python ./queryIndex_tf.py")
    elif b5 = = 3:
        os.system("python ./pdftotext.py")
    elif b5 = = 4:
        b6 = input("Enter the string to search using KMP: ")
        os.system(f"python ./kmp.py {b6}")
    elif b5 = = 5:
        os.system(f"python ./time.py {b3}")
    else:
        print("Invalid option. Please try again.")
    b5 = fonk1()
print("Exiting program...")