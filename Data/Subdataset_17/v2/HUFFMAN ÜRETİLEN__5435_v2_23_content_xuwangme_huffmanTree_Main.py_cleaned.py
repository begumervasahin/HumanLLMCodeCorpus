from FileOperation import FileOperation
def main():
    file_operation = FileOperation()
    zip_file_path = "./data/Aesop_Fables_zip.txt"
    unzip_file_path = "./data/Aesop_Fables_zip_unzip.txt"
    file_operation.unzipFile(zipFileName=zip_file_path, unzipFileName=unzip_file_path)
if __name__ == "__main__":
    main()