import os
import sys
import glob
text_directory = "Texts"
if not os.path.exists(text_directory):
    os.makedirs(text_directory)
arg_list = glob.glob(os.path.join(text_directory, "*.txt"))
argv = " ".join(f'"{arg}"' for arg in arg_list)
menu_options =
print(menu_options)
q = int(input("Choose an option: "))
while q != 6:
    if q == 1:
        os.system(f"python ./createIndex_tf.py {argv}")
        os.system("python ./queryIndex_tfidf.py")
    elif q == 2:
        os.system("python ./queryIndex_tf.py")
    elif q == 3:
        os.system("python ./pdftotext.py")
    elif q == 4:
        ar = input("Enter search string: ")
        os.system(f"python ./kmp.py {ar}")
    elif q == 5:
        os.system(f"python ./time.py {argv}")
    else:
        print("Invalid option, please try again.")
    print(menu_options)
    q = int(input("Choose an option: "))
print("Exiting program.")