import os
import pandas as pd
import distance
def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        content = ' '.join(file.read().strip().split()[1:])
    return content
def calculate_similarity(file_contents):
    num_files = len(file_contents)
    similarity_matrix = pd.DataFrame(index=range(num_files), columns=range(num_files))
    for i, content1 in enumerate(file_contents):
        for j, content2 in enumerate(file_contents):
            if i <= j:
                distance_value = distance.nlevenshtein(content1.lower().strip(), content2.lower().strip(), method=2)
                similarity_matrix.iloc[i, j] = distance_value
                similarity_matrix.iloc[j, i] = distance_value
            if verbose and (j % 100 == 0):
                print(f'Currently processing file {i+1} with file {j+1}')
    return similarity_matrix
def main():
    print('All modules imported correctly')
    verbose = 0
    mypath = 'C:\\Users\\Hari\\Dropbox\\IPO analysis sourcecode\\IPO Project\\Data\\Individual Sections of IPO documents\\business'
    output_file = 'document_similarity_levenstein_business.csv'
    file_list = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))][:3]
    file_contents = [read_file_contents(os.path.join(mypath, file_name)) for file_name in file_list]
    similarity_df = calculate_similarity(file_contents)
    similarity_df.columns = file_list
    similarity_df.index = file_list
    print('All calculations made. Exporting to CSV')
    similarity_df.to_csv(output_file, encoding='utf-8')
    print('Export to CSV done!')
if __name__ == "__main__":
    main()