import os
import glob
def create_text_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def get_argument_list(directory):
    return " ".join([f'"{file}"' for file in glob.glob(f"{directory}/*.txt")])
def display_menu():
    menu_options =
    print(menu_options)
    return int(input("Enter your choice: "))
def handle_choice(choice, argv):
    if choice == 1:
        os.system(f"python ./createIndex_tf.py {argv}")
        os.system("python ./queryIndex_tfidf.py")
    elif choice == 2:
        os.system("python ./queryIndex_tf.py")
    elif choice == 3:
        os.system("python ./pdftotext.py")
    elif choice == 4:
        search_string = input("Enter the string to search using KMP: ")
        os.system(f"python ./kmp.py {search_string}")
    elif choice == 5:
        os.system(f"python ./time.py {argv}")
    elif choice == 6:
        print("Exiting program...")
        return False
    else:
        print("Invalid option. Please try again.")
    return True
def main():
    text_directory = "Texts"
    create_text_directory(text_directory)
    argv = get_argument_list(text_directory)
    while True:
        choice = display_menu()
        if not handle_choice(choice, argv):
            break
if __name__ == "__main__":
    main()