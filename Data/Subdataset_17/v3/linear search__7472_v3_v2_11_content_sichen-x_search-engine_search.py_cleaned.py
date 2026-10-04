import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def main():
    if not validate_arguments():
        print_usage_instructions()
        return
    search_impl = sys.argv[1]
    root_directory = sys.argv[2]
    files = filelist(root_directory)
    print(f"{len(files)} files found in the directory {root_directory}")
    search_index = None
    while True:
        search_terms = input("Enter search terms: ")
        terms = words(search_terms)
        documents, search_index = perform_search(search_impl, files, terms, search_index)
        if documents is None:
            print(f"Invalid search type: {search_impl}")
            break
        display_results(documents, terms)
def validate_arguments():
    return len(sys.argv) == 3
def print_usage_instructions():
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py index ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
def perform_search(search_impl, files, terms, search_index):
    if search_impl == 'linear':
        documents = linear_search(files, terms)
    elif search_impl == 'index':
        if search_index is None:
            search_index = create_index(files)
            print("Index creation complete")
        documents = index_search(files, search_index, terms)
    elif search_impl == 'myhtable':
        if search_index is None:
            search_index = myhtable_create_index(files)
            print("Hash table index creation complete")
        documents = myhtable_index_search(files, search_index, terms)
    else:
        return None, search_index
    return documents, search_index
def display_results(documents, terms):
    results_page = results(documents, terms)
    results_file_path = "/tmp/results.html"
    with open(results_file_path, "w") as results_file:
        results_file.write(results_page)
    webbrowser.open_new_tab(f"file:
if __name__ == "__main__":
    main()