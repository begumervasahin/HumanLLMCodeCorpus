import os
import glob
b1 = "Texts"
b2 = {
    1: "To create index and search in folder",
    2: "To search in folder",
    3: "To convert PDF to text",
    4: "Search in file by KMP",
    5: "Recently modified or created files",
    6: "Exit program"
}
def fonk1():
    if not os.path.exists(b1):
        os.makedirs(b1)
def fonk2(directory):
    return glob.glob(directory)
def fonk3(options):
    for key, value in options.items():
        print(f"{key}) {value}")
    print()
def fonk4():
    fonk1()
    while True:
        fonk3(b2)
        b3 = int(input("Enter your b3: "))
        if b3 = = 6:
            print("Exiting program...")
            break
        if b3 = = 1:
            b4 = fonk2("./Texts/*.txt")
            b5 = " ".join(f"\"{file}\"" for file in b4)
            os.system(f"python ./createIndex_tf.py {b5}")
            os.system("python ./queryIndex_tfidf.py")
        elif b3 = = 2:
            os.system("python ./queryIndex_tf.py")
        elif b3 = = 3:
            os.system("python ./pdftotext.py")
        elif b3 = = 4:
            b6 = input("Enter the search b6: ")
            os.system(f"python ./kmp.py \"{b6}\"")
        elif b3 = = 5:
            b4 = fonk2("./Texts/*.txt")
            b5 = " ".join(f"\"{file}\"" for file in b4)
            os.system(f"python ./time.py {b5}")
if b7 = = "__main__":
    fonk4()