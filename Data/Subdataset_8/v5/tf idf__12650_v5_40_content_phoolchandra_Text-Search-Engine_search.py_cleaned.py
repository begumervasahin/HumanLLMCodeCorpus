import os
import glob
TEXT_DIRECTORY = "Texts"
MENU_OPTIONS = {
    1: "To create index and search in folder",
    2: "To search in folder",
    3: "To convert PDF to text",
    4: "Search in file by KMP",
    5: "Recently modified or created files",
    6: "Exit program"
}
def create_text_directory():
    if not os.path.exists(TEXT_DIRECTORY):
        os.makedirs(TEXT_DIRECTORY)
def get_text_files(directory):
    return glob.glob(directory)
def display_menu_options(options):
    for key, value in options.items():
        print(f"{key}) {value}")
    print()
def main():
    create_text_directory()
    while True:
        display_menu_options(MENU_OPTIONS)
        choice = int(input("Enter your choice: "))
        if choice == 6:
            print("Exiting program...")
            break
        if choice == 1:
            text_files = get_text_files("./Texts/*.txt")
            arguments = " ".join(f"\"{file}\"" for file in text_files)
            os.system(f"python ./createIndex_tf.py {arguments}")
            os.system("python ./queryIndex_tfidf.py")
        elif choice == 2:
            os.system("python ./queryIndex_tf.py")
        elif choice == 3:
            os.system("python ./pdftotext.py")
        elif choice == 4:
            pattern = input("Enter the search pattern: ")
            os.system(f"python ./kmp.py \"{pattern}\"")
        elif choice == 5:
            text_files = get_text_files("./Texts/*.txt")
            arguments = " ".join(f"\"{file}\"" for file in text_files)
            os.system(f"python ./time.py {arguments}")
if __name__ == "__main__":
    main()