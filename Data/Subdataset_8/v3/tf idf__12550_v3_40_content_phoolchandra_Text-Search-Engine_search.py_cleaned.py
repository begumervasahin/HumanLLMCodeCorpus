import os
import glob
TEXT_DIRECTORY = "Texts"
if not os.path.exists(TEXT_DIRECTORY):
    os.makedirs(TEXT_DIRECTORY)
def create_index_and_search_in_folder():
    text_files = glob.glob("./Texts/*.txt")
    args = " ".join(['"' + file + '"' for file in text_files])
    os.system("python ./createIndex_tf.py " + args)
    os.system("python ./queryIndex_tfidf.py ")
def search_in_folder():
    os.system("python ./queryIndex_tf.py ")
def convert_pdf_to_text():
    os.system("python ./pdftotext.py ")
def search_in_file_by_kmp():
    search_term = input("Enter search term: ")
    os.system("python ./kmp.py " + search_term)
def recently_modified_or_created_files():
    text_files = glob.glob("./Texts/*.txt")
    args = " ".join(['"' + file + '"' for file in text_files])
    os.system("python ./time.py " + args)
def display_menu():
    print("1) To create index and search in folder")
    print("2) To search in folder")
    print("3) To convert PDF to text")
    print("4) Search in file by KMP")
    print("5) Recently modified or created files")
    print("6) Exit program")
def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_index_and_search_in_folder()
        elif choice == 2:
            search_in_folder()
        elif choice == 3:
            convert_pdf_to_text()
        elif choice == 4:
            search_in_file_by_kmp()
        elif choice == 5:
            recently_modified_or_created_files()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    main()