import zipfile
def crack_zip_password(zip_file_path, dictionary_file_path):
    try:
        with zipfile.ZipFile(zip_file_path) as zip_file:
            passwords = [line.strip() for line in open(dictionary_file_path, 'r')]
            for password in passwords:
                try:
                    zip_file.extractall(pwd=password.encode())
                    print('Password cracked with: ', password)
                    return
                except Exception:
                    pass
            print('Password not found')
    except zipfile.BadZipfile:
        print("ERROR: Invalid ZIP file")
        return
if __name__ == "__main__":
    zip_file_path = 'test_zip.zip'
    dictionary_file_path = 'english.txt'
    crack_zip_password(zip_file_path, dictionary_file_path)