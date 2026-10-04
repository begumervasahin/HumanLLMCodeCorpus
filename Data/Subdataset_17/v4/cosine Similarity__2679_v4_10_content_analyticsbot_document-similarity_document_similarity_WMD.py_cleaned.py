import os
import pandas as pd
from word_mover_distance import similarity
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def calculate_similarity(file_list, directory_path, verbose=0):
    num_files = len(file_list)
    similarity_matrix = pd.DataFrame(index=file_list, columns=file_list)
    for i, file1 in enumerate(file_list):
        print(file1)
        s1 = read_file(os.path.join(directory_path, file1))
        for j, file2 in enumerate(file_list):
            if i <= j:
                s2 = read_file(os.path.join(directory_path, file2))
                similarity_value = similarity(s1, s2)
                similarity_matrix.loc[file1, file2] = similarity_value
                similarity_matrix.loc[file2, file1] = similarity_value
            if verbose:
                print(f'Currently processing {i}, {j}')
    return similarity_matrix
def main():
    print('All modules imported correctly')
    verbose = 0
    directory_path = 'C:\\Users\\Administrator\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\newuop'
    output_file = 'document_similarity_business.csv'
    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    similarity_df = calculate_similarity(file_list, directory_path, verbose)
    print('All calculations made. Exporting to CSV')
    similarity_df.to_csv(output_file, encoding='utf-8')
    print('Export to CSV done!')
if __name__ == "__main__":
    main()