import os
import sys
import glob
def create_texts_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def gather_txt_files(directory):
    return glob.glob(os.path.join(directory, "*.txt"))
def display_menu():
    menu_options =
    print(menu_options)
def main():
    text_directory = "Texts"
    create_texts_directory(text_directory)
    arg_list = gather_txt_files(text_directory)
    argv = " ".join(f'"{arg}"' for arg in arg_list)
    display_menu()
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
            search_string = input("Enter search string: ")
            os.system(f"python ./kmp.py {search_string}")
        elif q == 5:
            os.system(f"python ./time.py {argv}")
        else:
            print("Invalid option, please try again.")
        display_menu()
        q = int(input("Choose an option: "))
    print("Exiting program.")
if __name__ == "__main__":
    main()