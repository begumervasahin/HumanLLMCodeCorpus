from FileOperation import FileOperation
def main():
    file_operation = FileOperation()
    zip_file_name = "./data/Aesop_Fables_zip.txt"
    unzip_file_name = "./data/Aesop_Fables_zip_unzip.txt"
    file_operation.unzip_file(zip_file_name, unzip_file_name)
if __name__ == '__main__':
    main()