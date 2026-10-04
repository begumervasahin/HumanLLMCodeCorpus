import os
import glob
def fonk1(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def fonk2(directory):
    return " ".join([f'"{file}"' for file in glob.glob(f"{directory}/*.txt")])
def fonk3():
    b1 = print(b1)
    return int(input("Enter your b2: "))
def fonk4(b2, b5):
    if b2 = = 1:
        os.system(f"python ./createIndex_tf.py {b5}")
        os.system("python ./queryIndex_tfidf.py")
    elif b2 = = 2:
        os.system("python ./queryIndex_tf.py")
    elif b2 = = 3:
        os.system("python ./pdftotext.py")
    elif b2 = = 4:
        b3 = input("Enter the string to search using KMP: ")
        os.system(f"python ./kmp.py {b3}")
    elif b2 = = 5:
        os.system(f"python ./time.py {b5}")
    elif b2 = = 6:
        print("Exiting program...")
        return False
    else:
        print("Invalid option. Please try again.")
    return True
def fonk5():
    b4 = "Texts"
    fonk1(b4)
    b5 = fonk2(b4)
    while True:
        b2 = fonk3()
        if not fonk4(b2, b5):
            break
if b6 = = "__main__":
    fonk5()