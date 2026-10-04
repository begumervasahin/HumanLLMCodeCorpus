import zipfile
def extract_zip_with_password(zip_path, password_file):
    try:
        with zipfile.ZipFile(zip_path) as myzip:
            with open(password_file, 'r') as f:
                passwords = f.readlines()
                for password in passwords:
                    password = password.strip()
                    try:
                        print(f"Trying password: {password}")
                        myzip.extractall(pwd=password.encode())
                        print(f"Password cracked with: {password}")
                        return
                    except (RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile):
                        continue
                print("Password not found")
    except zipfile.BadZipFile:
        print("ERROR: Not a valid zip file")
        return
def main():
    zip_path = 'test_zip.zip'
    password_file = 'english.txt'
    extract_zip_with_password(zip_path, password_file)
if __name__ == "__main__":
    main()