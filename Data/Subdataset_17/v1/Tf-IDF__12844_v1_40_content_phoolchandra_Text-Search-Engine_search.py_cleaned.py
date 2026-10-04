import os
import sys
import glob
text_directory = "Texts"
if not os.path.exists(text_directory):
    os.makedirs(text_directory)
arg_list = glob.glob("./Texts/*.txt")
argv = " ".join([f'"{arg}"' for arg in arg_list])
menu_options =
def display_menu():
    print(menu_options)
    return int(input())
q = display_menu()
while q != 6:
    if q == 1:
        os.system(f"python ./createIndex_tf.py {argv}")
        os.system("python ./queryIndex_tfidf.py")
    elif q == 2:
        os.system("python ./queryIndex_tf.py")
    elif q == 3:
        os.system("python ./pdftotext.py")
    elif q == 4:
        ar = input("Enter the string to search using KMP: ")
        os.system(f"python ./kmp.py {ar}")
    elif q == 5:
        os.system(f"python ./time.py {argv}")
    else:
        print("Invalid option. Please try again.")
    q = display_menu()
print("Exiting program...")