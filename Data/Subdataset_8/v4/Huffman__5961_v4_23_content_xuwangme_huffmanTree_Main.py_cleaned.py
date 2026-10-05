
from FileOperation import FileOperation
if __name__ == '__main__':
    file_operation = FileOperation()
    zip_file_name = "./data/Aesop_Fables_zip.txt"
    unzip_file_name = "./data/Aesop_Fables_zip_unzip.txt"
    file_operation.unzipFile(zipFileName=zip_file_name, unzipFileName=unzip_file_name)